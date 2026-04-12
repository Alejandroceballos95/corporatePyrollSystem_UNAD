"""
Universidad Nacional Abierta y a Distancia - UNAD
Curso: Programación (213023)
Fase 3 - Modelos de herencia, polimorfismo y gestión de métodos
Estudiante: Jhon Alejandro Ceballos Tobón
Grupo: 213023_109
Fecha: Abril de 2026
Proyecto: Ejercicio 3 - Sistema de Nómina Empresarial (Corporate Payroll System)
"""

import tkinter as tk
from tkinter import ttk, messagebox

# 1. MODELS (Cerebro del programa)


class Bonifiable:
    def __init__(self, bonus_percentage=0.0):
        self.bonus_percentage = bonus_percentage

    def calculate_bonus(self, base_amount):
        return base_amount * (self.bonus_percentage / 100)


class Employee:
    def __init__(self, emp_id, name, base_salary):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        raise NotImplementedError("Subclasses must implement calculate_salary")

    def get_details(self):
        return f"ID: {self.emp_id} | Name: {self.name}"


class FullTimeEmployee(Employee, Bonifiable):
    def __init__(self, emp_id, name, base_salary, bonus_percentage):
        Employee.__init__(self, emp_id, name, base_salary)
        Bonifiable.__init__(self, bonus_percentage)

    def calculate_salary(self):
        bonus = self.calculate_bonus(self.base_salary)
        return self.base_salary + bonus


class HourlyEmployee(Employee):
    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        super().__init__(emp_id, name, base_salary=0.0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


class CommissionedEmployee(Employee, Bonifiable):
    def __init__(self, emp_id, name, base_salary, commission_rate, sales_amount, bonus_percentage=0.0):
        Employee.__init__(self, emp_id, name, base_salary)
        Bonifiable.__init__(self, bonus_percentage)
        self.commission_rate = commission_rate
        self.sales_amount = sales_amount

    def calculate_salary(self):
        commission = self.sales_amount * (self.commission_rate / 100)
        bonus = self.calculate_bonus(self.base_salary)
        return self.base_salary + commission + bonus

# 2. GUI (Interfaz Gráfica)


class PayrollApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Corporate Payroll System")
        self.root.geometry("500x550")
        self.root.config(padx=20, pady=20)

        # Título
        tk.Label(self.root, text="Employee Payroll Calculator",
                 font=("Helvetica", 16, "bold")).pack(pady=(0, 20))

        # Selección de tipo de empleado
        self.type_frame = tk.Frame(self.root)
        self.type_frame.pack(fill="x")
        tk.Label(self.type_frame, text="Select Employee Type:",
                 font=("Arial", 10, "bold")).pack(anchor="w")

        self.employee_type_var = tk.StringVar()
        self.combo_type = ttk.Combobox(
            self.type_frame, textvariable=self.employee_type_var, state="readonly")
        self.combo_type['values'] = (
            "Full-Time Employee", "Hourly Employee", "Commission Employee")
        self.combo_type.pack(fill="x", pady=5)
        # Evento: Cuando cambie la selección, limpiar campos automáticamente
        self.combo_type.bind("<<ComboboxSelected>>",
                             lambda e: self.clear_fields())

        # Inputs
        self.input_frame = tk.LabelFrame(
            self.root, text="Employee Data", padx=10, pady=10)
        self.input_frame.pack(fill="x", pady=10)

        # Labels y Entries
        tk.Label(self.input_frame, text="Employee ID:").grid(
            row=0, column=0, sticky="w")
        self.entry_id = tk.Entry(self.input_frame)
        self.entry_id.grid(row=0, column=1, pady=5)

        tk.Label(self.input_frame, text="Full Name:").grid(
            row=1, column=0, sticky="w")
        self.entry_name = tk.Entry(self.input_frame)
        self.entry_name.grid(row=1, column=1, pady=5)

        tk.Label(self.input_frame,
                 text="Base Salary / Hourly Rate ($):").grid(row=2, column=0, sticky="w")
        self.entry_salary = tk.Entry(self.input_frame)
        self.entry_salary.grid(row=2, column=1, pady=5)

        tk.Label(self.input_frame,
                 text="Hours Worked / Sales Amount:").grid(row=3, column=0, sticky="w")
        self.entry_extra = tk.Entry(self.input_frame)
        self.entry_extra.grid(row=3, column=1, pady=5)

        tk.Label(self.input_frame,
                 text="Bonus / Commission Rate (%):").grid(row=4, column=0, sticky="w")
        self.entry_rate = tk.Entry(self.input_frame)
        self.entry_rate.grid(row=4, column=1, pady=5)

        # Botones
        self.calc_button = tk.Button(self.root, text="Calculate Salary", font=(
            "Arial", 10, "bold"), command=self.calculate_payroll)
        self.calc_button.pack(pady=10)

        self.clear_button = tk.Button(
            self.root, text="Clear Form", command=self.clear_fields)
        self.clear_button.pack()

        # Resultados
        self.result_label = tk.Label(
            self.root, text="", font=("Arial", 11, "bold"), fg="green")
        self.result_label.pack(pady=20)

    def clear_fields(self):
        """Borra todos los campos de entrada y el resultado anterior"""
        self.entry_id.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_salary.delete(0, tk.END)
        self.entry_extra.delete(0, tk.END)
        self.entry_rate.delete(0, tk.END)
        self.result_label.config(text="")

    def calculate_payroll(self):
        try:
            emp_id = self.entry_id.get()
            name = self.entry_name.get()
            if not emp_id or not name:
                messagebox.showwarning("Warning", "Please enter ID and Name.")
                return

            val_salary = float(self.entry_salary.get() or 0)
            val_extra = float(self.entry_extra.get() or 0)
            val_rate = float(self.entry_rate.get() or 0)
            emp_type = self.employee_type_var.get()

            if emp_type == "Full-Time Employee":
                employee = FullTimeEmployee(emp_id, name, val_salary, val_rate)
            elif emp_type == "Hourly Employee":
                employee = HourlyEmployee(emp_id, name, val_salary, val_extra)
            elif emp_type == "Commission Employee":
                employee = CommissionedEmployee(
                    emp_id, name, val_salary, val_rate, val_extra)
            else:
                messagebox.showerror("Error", "Select an employee type.")
                return

            total = employee.calculate_salary()
            self.result_label.config(
                text=f"{employee.get_details()}\nTotal Salary: ${total:.2f}")

            # self.clear_fields()

        except ValueError:
            messagebox.showerror("Error", "Invalid numeric input.")

# 3. MAIN (Punto de entrada)


if __name__ == "__main__":
    root = tk.Tk()
    app = PayrollApp(root)
    root.mainloop()
