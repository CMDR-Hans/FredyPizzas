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

import os, msvcrt
os.system("cls")
pokedex = []

while True:
    print(menu)
    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
        # Agregar pokemon
        numero = input("Ingrese el número del pokemon: ")
        nombre = input("Ingrese el nombre del pokemon: ")
        altura = input("Ingrese la altura del pokemon: ")
        
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
            for p in pokedex:
                print(f"Numero: {p['numero']}, Nombre: {p['nombre']}, Altura: {p['altura']} m")
    
    elif opcion == "3":
        # Eliminar pokemon
        pass
    
    elif opcion == "4":
        # Salir
        print("Saliendo de la pokedex...")
        break
    
    else:
        print("Opción no válida. Intente nuevamente.")
