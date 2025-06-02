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
        for p in pokedex:
            if p["numero"]==numero or p["nombre"]==nombre:
                print("Ya existe un pokemon con ese número o ese nombre. Intente nuevamente.")
                print("\n...presione una tecla para continuar...")
                msvcrt.getch()
                break
            else:
                pokedex.append({
                "numero": numero,
                "nombre": nombre,
                "altura": altura
                })
                print("Pokemon agregado exitosamente.")
                print("\n...presione una tecla para continuar...")
                msvcrt.getch()
    
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
        if not pokedex:
            print("No hay pokemones registrados para eliminar.")
        else:
            while True:
                try:
                    numero = int(input("Ingrese el número del pokemon a eliminar: "))
                    if numero <= 0:
                        print("El número del pokemon debe ser un entero positivo. Intente nuevamente.")
                        continue
                    break
                except :
                    print("Entrada inválida. Por favor, ingrese un número entero positivo.")
                    print("\n...presione una tecla para continuar...")
                    msvcrt.getch()

            verificador = False
            for p in pokedex:
                if p["numero"] == numero:
                    pokedex.remove(p)
                    verificador= True
                    print(f"Pokemon {p['nombre']} eliminado exitosamente.")
                    break
            
            if verificador == False:
                print("Pokemon no encontrado.")
    elif opcion == "4":
        # Salir
        print("Saliendo de la pokedex...")
        break
    
    else:
        print("Opción no válida. Intente nuevamente.")
        print("\n...presione una tecla para continuar...")
        msvcrt.getch()
