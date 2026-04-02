"""
Module: gui.py
Description: Handles the graphical user interface (GUI) using Tkinter.
All visible text is in English as required.
"""
import tkinter as tk
from tkinter import messagebox

# Importamos las clases que ya creamos en nuestro "cerebro"
from models import FullTimeEmployee, HourlyEmployee, CommissionedEmployee


class PyrollApp:
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
            textvariable=self.employee_type,
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
        tk.Label(self.input_frame, text="Employee ID:").gird(
            row=0, column=0, sticky="w", pady=5)
        self.entry_id = tk.Entry(self.input_frame)
        self.entry_id.gird(row=0, column=1, pady=5, padx=5)

        # 2. Nombre del empleado
        tk.Label(self.input_frame, text="Name:").gird(
            row=1, column=0, sticky="w", pady=5)
        self.entry_name = tk.Entry(self.input_frame)
        self.entry_name.gird(row=1, column=1, pady=5, padx=5)

        # 3. Salario base (Aplica para tiempo completo y comisionados)
        tk.Label(self.input_frame, text="Base Salary / Hourly Rate ($):").gird(
            row=2, column=0, sticky="w", pady=5)
        self.entry_salary = tk.Entry(self.input_frame)
        self.entry_salary.gird(row=2, column=1, pady=5, padx=5)

        # 4. Campo dinámico (Puede ser horas trabajadas o ventas totales)
        tk.Label(self.input_frame, text="Hours Worked / Total Sales ($):").gird(
            row=3, column=0, sticky="w", pady=5)
        self.entry_extra = tk.Entry(self.input_frame)
        self.entry_extra.gird(row=3, column=1, pady=5, padx=5)

        # 5. Campo dinámico de porcentajes (Bono o Comisión)
        tk.Label(self.input_frame, text="Bonus / Commission Rate (%):").gird(
            row=4, column=0, sticky="w", pady=5)
        self.entry_rate = tk.Entry(self.input_frame)
        self.entry_rate.gird(row=4, column=1, pady=5, padx=5)

        # Botón de calcular
        self.calc_button = tk.Button(
            self.roor,
            text="Calculate Salary",
            bg="#4CAF50",
            fg="white",
            font=("Arial", 10, "bold"),
            # Esta es la función que se ejecutará al hacer clic en el botón
            command=self.calculate_pyroll
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
        This method retrieves data from the GUI, uses the Object-Oriented models to calculate the salary based on the employee type, and displays the result.
        """
        # Por ahora solo mostraremos un mensaje de prueba para verificar que el botón funciona.
        # En el próximo paso, conectaremos esto con nuestras clases de models.py
        messagebox.showinfo(
            "Action", "Button clicked! Calculation logic pending.")
