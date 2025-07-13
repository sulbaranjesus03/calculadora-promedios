import os 
import platform
import time
import sys

def banner():
    print('''
    ╔══════════════════════════════════════════════╗
    ║         📊 CALCULADORA DE PROMEDIOS          ║
    ║           Creada por: Jesus Sulbaran         ║
    ╚══════════════════════════════════════════════╝
            ¡Bienvenido! Empecemos a calcular.
    ''')  

def menu():
    print("=" * 50)
    print("1. Iniciar calculadora")
    print("2. Ver instrucciones")
    print("3. Acerca del creador")
    print("4. Salir")
    print("=" * 50)

def startCalculator():
    notas = []
    while True:
        nota = input("\n 📥 Ingresa una nota (o escribe 'fin' para terminar): ")
        if nota.lower() == 'fin':
            break
        try:
            valor = float(nota)
            notas.append(valor)
        except ValueError:
            print("⚠️ Solo se permiten números o 'fin'.")
    
    if notas:
        promedio = sum(notas) / len(notas)

        print(f"\n✅ Promedio calculado: {round(promedio, 2)}")
        print(f'📊 Total de notas: {len(notas)}')
        print(f"📈 Nota maxima: {max(notas)}")
        print(f"📉 Nota minima: {min(notas)}")
    else:
        print("⚠️ No se ingresaron notas.")    

def showInstructions():
    print('''
    📘 INSTRUCCIONES:
    1. Selecciona la opción "Iniciar calculadora".
    2. Ingresa tus notas una por una.
    3. Escribe "fin" para terminar el ingreso.
    4. El programa mostrará tu promedio final.
    ''')

def showErrorBanner():
    print('''
     _________________________
    |                         |
    |   ⚠️   ERROR FATAL ⚠️     |
    |_________________________|
    |                         |
    |  La opción ingresada no |
    |  es válida. Por favor,  |
    |  elige entre 1 y 4.     |
    |_________________________|
            (\__/) 
            (•ㅅ•) 
    ''')    

def openAbout():
    try:
        with open("About.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            print("\n" + contenido)
    except FileNotFoundError:
        print("❌ No se encontro el archivo 'About.txt'.")

def waitForUser():
    input('🔄 Presione enter para continuar...')     

def cleanConsole():
    sistema = platform.system()

    if sistema == "Windows":
        os.system('cls')
    else:
        os.system('clear') 

def loadingBar(mensaje="🔄 Cargando", total=20, delay=0.05):
    print(mensaje)
    for i in range(total + 1):
        bar = "[" + "#" * i + "-" * (total - i) + "]"
        sys.stdout.write("\r" + bar)
        sys.stdout.flush()
        time.sleep(delay)
    # Imprime el mensaje final junto a la barra en la misma linea
    finalBar = "[" + "#" * total + "] ✅ Carga completa!"
    sys.stdout.write("\r" + finalBar + "\n")
    sys.stdout.flush()            

def executeOption(option):
    cleanConsole()    
    if option == '1':
        loadingBar("🔢 Iniciando la calculadora...")
        # print("🔢 Iniciando la calculadora...")
        startCalculator()
    elif option == '2':
        showInstructions()
    elif option == '3':
        openAbout()
    elif option == '4':
        print("👋 Gracias por usar la calculadora. ¡Hasta pronto!")
        exit()            
    else:
        # print("⚠️ Opcion invalida. BY : JD")
        showErrorBanner()
        time.sleep(1.5)

    print('=' * 50)
    waitForUser()

def main():
    while True:
        cleanConsole()
        banner()
        menu()
        option = input('Selecciona una opcion (1-4): ')
        executeOption(option)

main()            