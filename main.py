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
from gui import PayrollApp


def main():
    # Creamos la ventana principal de Tkinter
    root = tk.Tk()

    # Instanciamos nuestra aplicación gráfica pasándole la ventana principal
    app = PayrollApp(root)

    # Iniciamos el "bucle principal" para que la ventana se quede abierta esperando interacciones
    root.mainloop()


if __name__ == "__main__":
    main()
