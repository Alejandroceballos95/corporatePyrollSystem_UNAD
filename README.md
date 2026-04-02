# Corporate Payroll System - UNAD 💼

## Descripción
Este proyecto es un Sistema de Nómina Empresarial desarrollado en Python. Fue construido como parte de la **Fase 3 del curso de Programación (213023)** de la Universidad Nacional Abierta y a Distancia (UNAD). 

El objetivo principal de este software es aplicar los pilares de la Programación Orientada a Objetos (POO), separando la lógica matemática de la interfaz visual mediante una arquitectura modular.

## Características Técnicas Aplicadas ⚙️
Para cumplir rigurosamente con los requerimientos técnicos de la guía de actividades y la rúbrica de evaluación, este proyecto implementa:
- **Herencia Múltiple y Simple:** A través de las clases base `Employee` y `Bonifiable`.
- **Polimorfismo y Sobreescritura:** El método `calculate_salary()` se adapta dinámicamente dependiendo de si la clase hija instanciada es `FullTimeEmployee`, `HourlyEmployee` o `CommissionedEmployee`.
- **Interfaz Gráfica (GUI):** Construida con la biblioteca estándar `tkinter`, diseñada íntegramente en idioma inglés y adaptada para su correcta ejecución en cualquier sistema operativo.

## Arquitectura del Proyecto 📂
El código está modularizado para aplicar buenas prácticas de ingeniería de software:
- `models.py`: Contiene exclusivamente el "cerebro" (Modelos y lógica POO).
- `gui.py`: Contiene la "vista" (Ventanas, botones y campos de entrada en Tkinter).
- `main.py`: Es el punto de entrada o "director de orquesta" de la aplicación.

## Autor 👨‍💻
**Jhon Alejandro Ceballos Tobón**
Grupo: 213023_109

## Cómo ejecutar la aplicación ▶️

Este proyecto utiliza únicamente librerías estándar de Python (`tkinter`), por lo que **no requiere** la instalación de dependencias externas mediante `pip`.

### Para usuarios de Windows:
1. Asegúrate de tener Python instalado en tu sistema (verificando que la opción *tcl/tk and IDLE* fue seleccionada durante la instalación, lo cual es por defecto).
2. Abre la consola de comandos (CMD o PowerShell) en la carpeta del proyecto.
3. Ejecuta el siguiente comando:
   ```cmd
   python main.py