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
