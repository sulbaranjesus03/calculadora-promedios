# 📊 Calculadora de Promedios

Una sencilla y amigable calculadora de promedios diseñada en Python que permite a los usuarios ingresar sus notas, calcular el promedio final y navegar por una interfaz de texto clara y animada.

---

## 🚀 Características

- Menú interactivo con opciones de navegación
- Animación de carga personalizada en consola
- Entrada de notas con validación de errores
- Cálculo automático del promedio
- Visualización de instrucciones de uso
- Limpieza automática de la consola según el sistema operativo
- Lectura de archivo de descripción del creador (`About.txt`)

---

## 💻 Requisitos

- Python 3.7 o superior
- Consola compatible (Windows/Linux/macOS)
- Archivo opcional `About.txt` para la sección “Acerca del creador”

---

## 📦 Instalación

```bash
# Clona el repositorio
git clone https://github.com/sulbaranjesus03/calculadora-promedios.git

# Accede a la carpeta del proyecto
cd calculadora-promedios

# Ejecuta el script
python app.py

```               
---

## 🧠 Estructura del código

- main(): Bucle principal del programa

- menu(): Menú de navegación

- startCalculator(): Lógica para ingresar notas y calcular el promedio

- loadingBar(): Animación de barra de carga

- showInstructions(): Muestra las instrucciones de uso

- openAbout(): Muestra contenido del archivo About.txt

- cleanConsole(): Limpia la consola según el sistema operativo

- waitForUser(): Pausa la ejecución para continuar

- executeOption(): Controlador de opciones del menú

---

## 💡 Ideas futuras

- Exportar resultados a un archivo resultados.txt

- Versión con interfaz gráfica (GUI)

- Soporte para varios usuarios o sesiones 

---

## 📝Titulos de las revisiones

- feat: para nuevas funciones

- fix: para correcciones de errores

- docs: para cambios en documentación

- style: para ajustes de estilo (sin afectar el código)

- refactor: para mejoras en el código sin cambiar funcionalidad

- test: para agregar o modificar pruebas

- chore: para tareas generales de mantenimiento 