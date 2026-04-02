"""
Module: gui.py
Description: Handles the graphical user interface (GUI) using Tkinter.
All visible text is in English as required.
"""
import tkinter as tk
from tkinter import ttk, messagebox

# Importamos las clases que ya creamos en nuestro "cerebro"
from models import FullTimeEmployee, HourlyEmployee, CommissionedEmployee


class PayrollApp:
    """
    Main class for the GUI application.
    """

    def __init__(self, root):
        self.root = root
        # Configuramos la ventana principal
        self.root.title("Corporate Payroll System")  # Título de la ventana
        self.root.geometry("500x500")  # Tamaño inicial
        # Margenes internos para que no quede tan pegado a los bordes
        self.root.config(padx=20, pady=20)

        # Título principal
        self.title_Label = tk.Label(
            self.root,
            text="Employee Payroll Calculator",
            font=("Helvetica", 16, "bold")
        )
        self.title_Label.pack(pady=(0, 20))

        # Selección de tipo de empleado
        self.type_frame = tk.Frame(self.root)
        self.type_frame.pack(fill="x")

        tk.Label(self.type_frame, text="Select Employee Type:",
                 font=("Arial", 10, "bold")).pack(anchor="w")

        # Usamos un Combobox (Lista desplegable) para elegir el tipo de contrato
        self.employee_type_var = tk.StringVar()
        self.combo_type = ttk.Combobox(
            self.type_frame,
            textvariable=self.employee_type_var,
            state="readonly",
            values=["Full-Time Employee",
                    "Hourly Employee", "Commissioned Employee"]
        )
        self.combo_type.pack(fill="x", pady=5)
        self.combo_type.current(0)  # Seleccionamos el primer tipo por defecto

        # Campos de entrada
        # Creamos un "Frame" (una caja invisible) para organizar los campos de texxto
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(fill="x", pady=10)

        # 1. ID del empleado
        tk.Label(self.input_frame, text="Employee ID:").grid(
            row=0, column=0, sticky="w", pady=5)
        self.entry_id = tk.Entry(self.input_frame)
        self.entry_id.grid(row=0, column=1, pady=5, padx=5)

        # 2. Nombre del empleado
        tk.Label(self.input_frame, text="Name:").grid(
            row=1, column=0, sticky="w", pady=5)
        self.entry_name = tk.Entry(self.input_frame)
        self.entry_name.grid(row=1, column=1, pady=5, padx=5)

        # 3. Salario base (Aplica para tiempo completo y comisionados)
        tk.Label(self.input_frame, text="Base Salary / Hourly Rate ($):").grid(
            row=2, column=0, sticky="w", pady=5)
        self.entry_salary = tk.Entry(self.input_frame)
        self.entry_salary.grid(row=2, column=1, pady=5, padx=5)

        # 4. Campo dinámico (Puede ser horas trabajadas o ventas totales)
        tk.Label(self.input_frame, text="Hours Worked / Total Sales ($):").grid(
            row=3, column=0, sticky="w", pady=5)
        self.entry_extra = tk.Entry(self.input_frame)
        self.entry_extra.grid(row=3, column=1, pady=5, padx=5)

        # 5. Campo dinámico de porcentajes (Bono o Comisión)
        tk.Label(self.input_frame, text="Bonus / Commission Rate (%):").grid(
            row=4, column=0, sticky="w", pady=5)
        self.entry_rate = tk.Entry(self.input_frame)
        self.entry_rate.grid(row=4, column=1, pady=5, padx=5)

        # Botón de calcular
        self.calc_button = tk.Button(
            self.root,
            text="Calculate Salary",
            font=("Arial", 10, "bold"),
            # Esta es la función que se ejecutará al hacer clic en el botón
            command=self.calculate_payroll
        )
        self.calc_button.pack(pady=15)

        # Área de resultados
        self.result_label = tk.Label(
            self.root,
            text="Result will appeart here...",
            font=("Arial", 11, "italic"),
            fg="blue"
        )
        self.result_label.pack(pady=10)

    def calculate_payroll(self):
        """
        Retrieves data from the GUI, uses the Object-Oriented models to calculate 
        the salary based on the employee type, and displays the result.
        """
        try:
            # 1. Obtenemos los textos básicos (ID y Nombre)
            emp_id = self.entry_id.get()
            name = self.entry_name.get()

            # Validamos que no estén vacíos
            if not emp_id or not name:
                messagebox.showwarning(
                    "Input Error", "Please enter ID and Name.")
                return

            # 2. Convertimos los textos numéricos a decimales (float)
            # Si el campo está vacío, le ponemos un '0' por defecto
            val_salary = float(self.entry_salary.get() or 0)
            val_extra = float(self.entry_extra.get() or 0)
            val_rate = float(self.entry_rate.get() or 0)

            # 3. Identificamos qué tipo de empleado seleccionó el usuario
            emp_type = self.employee_type_var.get()
            employee = None

            # 4. Instanciamos la clase hija correspondiente
            if emp_type == "Full-Time Employee":
                # args: emp_id, name, base_salary, bonus_percentage
                employee = FullTimeEmployee(emp_id, name, val_salary, val_rate)

            elif emp_type == "Hourly Employee":
                # args: emp_id, name, hourly_rate, hours_worked
                employee = HourlyEmployee(emp_id, name, val_salary, val_extra)

            elif emp_type == "Commission Employee":
                # args: emp_id, name, base_salary, commission_rate, sales_amount
                employee = CommissionedEmployee(
                    emp_id, name, val_salary, val_rate, val_extra)

            else:
                messagebox.showerror(
                    "Error", "Please select a valid employee type.")
                return

            # 5. Aplicamos el poliformismo.
            # No nos importa qué tipo de empleado sea, solo le decimos "calcula tu salario".
            # Python sabrá qué fórmula matemática usar.
            total_salary = employee.calculate_salary()
            details = employee.get_details()

            # 6. Mostramos el resultado en la pantalla
            result_text = f"{details}\nTotal Calculated Salary: ${total_salary:.2f}"
            self.result_label.config(text=result_text, fg="green")

        except ValueError:
            # Si el usuario escribe letras en lugar de números en el salario, evitamos que el programa explote.
            messagebox.showerror(
                "Input Error", "Please enter valid numbers for salary, hours, sales, or rates.")
