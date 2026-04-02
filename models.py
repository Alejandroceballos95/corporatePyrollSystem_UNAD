"""
Module: models.py
Description: Contains the business logic and Object-Oriented models for the Corporate Payroll System.
"""


class Bonifiable:
    """
    Base class representing an entity that can receive a bonus.
    This class will be used alongside 'Employee' to demostrate multiple inheritance.
    """

    def __init__(self, bonus_porcentage=0.0):
        self.bonus_porcentage = bonus_porcentage

    def calculate_bonus(self, base_amount):
        """
        Calculates the bonus based on a base amount.
        """
        return base_amount * (self.bonus_porcentage / 100)


class Employee:
    """
    Base class representing a generic employee.
    """

    def __init__(self, emp_id, name, base_salary):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        """
        Calculates the total salary.
        This method is meant to be overridden by child classes (Polymorphism).
        """
        # Usamos NotImplementedError para obligar a que las clases hijas (Tiempo completo, horas, etc.) tengan que crear su propia versión de este método.
        raise NotImplementedError(
            "Subclasses must implemnent the calculate_salary method.")

    def get_details(self):
        """
        Returns a formatted string with basic employee details.
        """
        return f"ID: {self.emp_id} | Name: {self.name} | Base Salary: ${self.base_salary:.2f}"


class FullTimeEmployee(Employee, Bonifiable):
    """
    Class representing a full-time employee.
    Demostrates Multiple Inheritance (Employee, Bonifiable) and Polymorphism.
    """

    def __init__(self, emp_id, name, base_salary, bonus_porcentage=0.0):
        # Initializing both parent classes explicitly for Multiple Inheritance
        Employee.__init__(self, emp_id, name, base_salary)
        Bonifiable.__init__(self, bonus_porcentage)

    def calculate_salary(self):
        """
        Overrides the parent method.
        Total salary = base_salary + calculated bonus.
        """
        bonus = self.calculate_bonus(self.base_salary)
        return self.base_salary + bonus


class HourlyEmployee(Employee):
    """
    Class representing an hourly employee.
    Demostrates Single Inheritance and Polymorphism.
    """

    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        # Initializing the parent class (base_salary is set to 0 initially)
        super().__init__(emp_id, name, base_salary=0.0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        """
        Overrides the parent method.
        Total salary = hourly_rate * hours_worked.
        """
        return self.hourly_rate * self.hours_worked


class CommissionedEmployee(Employee, Bonifiable):
    """
    Class representing a commissioned-based employee.
    Demostrates Multiple Inheritance and Polymorphism.
    """

    def __init__(self, emp_id, name, base_salary, commission_rate, sales_amount, bonus_porcentage=0.0):
        Employee.__init__(self, emp_id, name, base_salary)
        Bonifiable.__init__(self, bonus_porcentage)
        self.commission_rate = commission_rate
        self.sales_amount = sales_amount

    def calculate_salary(self):
        """
        Overrides the parent method.
        Total salary = base_salary + (sales * commission_rate) + bonus
        """
        commission = self.sales_amount * (self.commission_rate / 100)
        bonus = self.calculate_bonus(self.base_salary)
        return self.base_salary + commission + bonus
