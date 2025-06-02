#Ejercicio sobre colecciones:
#Se pide crear un programa para almacenar pokemones.
#La información del pokemon debe ser número, nombre y altura.
#El programa debe mostrar las siguientes opciones:
#===MENU===
#1. Agregar pokemon
#2. Ver pokemones
#3. Eliminar pokemon
#4. Salir
#Importante:
#- Debe validar todos los valores que se ingresen por teclado, y volver a solicitarlo si existe algún error.
#- La información de los pokemones se debe almacenar en un formato de lista de diccionarios.


menu="""===MENU===
#1. Agregar pokemon
#2. Ver pokemones
#3. Eliminar pokemon
#4. Salir"""

import os, msvcrt, operator
os.system("cls")
pokedex = []

while True:
    os.system("cls")
    print(menu)
    opcion = input("Ingrese una opción: ")
    os.system("cls")


    if opcion == "1":
        # Agregar pokemon
        while True:
            try:
                numero = int(input("Ingrese el número del pokemon: "))
                if numero <=0:
                    print("El número del pokemon debe ser un entero positivo. Intente nuevamente.")
                    continue
                else:
                    break
            except:
                print("Entrada inválida. Por favor, ingrese un número entero positivo.")
                print("\n...presione una tecla para continuar...")
                msvcrt.getch()

        while True:
            try:
                nombre = input("Ingrese el nombre del pokemon: ").strip().title()
                if len(nombre)>=3 and nombre.isalpha():
                    break
                else:
                    print("Nombre muy corto para tu puchaball")
            except:
                print("El nombre del pokemon debe contener solo letras y tener al menos 3 caracteres.")
                print("\n...presione una tecla para continuar...")
                msvcrt.getch()

        while True:
            try:
                altura = float(input("Ingrese la altura del pokemon: "))
                if altura <= 0:
                    print("La altura debe ser un número positivo. Intente nuevamente.")
                else:
                    break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número válido para la altura.")
                print("\n...presione una tecla para continuar...")
                msvcrt.getch()
        
        pokedex.append({
            "numero": numero,
            "nombre": nombre,
            "altura": altura
        })
        print("Pokemon agregado exitosamente.")
    
    elif opcion == "2":
        # Ver pokemones
        if not pokedex:
            print("No hay pokemones registrados.")
        else:
            #Esta la aprendi de gugle
            pokedex.sort(key=operator.itemgetter("numero"))
            for p in pokedex:
                print(f"Numero: {p['numero']}, Nombre: {p['nombre']}, Altura: {p['altura']} m")
        print("\n...presione una tecla para continuar...")
        msvcrt.getch()
    
    elif opcion == "3":
        # Eliminar pokemon
            pass
    elif opcion == "4":
        # Salir
        print("Saliendo de la pokedex...")
        break
    
    else:
        print("Opción no válida. Intente nuevamente.")
        print("\n...presione una tecla para continuar...")
        msvcrt.getch()
