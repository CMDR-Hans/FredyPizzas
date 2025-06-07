#Creamos una lista vacia para almacenar las pizzas
ListaPizzas=[]

# Importamos las librerias necesarias
import os,msvcrt,time

#tulpa de masas
tipoMasa=("delgada","tradicional","estilo chicago","intregral") #wacala integral
#menu
menu="""--- MENU DE PIZZAS ---
1. Registrar pizzas
2. Ver catalogo de pizzas
3. Realizar pedido
4. Ver pedidos realizados
5. Salir"""
#Ciclo para el menu
while True:
    os.system("cls")
    print(menu)

    opcion=input("Seleccione una opción (1-5): ")

    if opcion=="1":
        while True:
            try:
                # Pedimos el codigo de la pizza y validamos
                codigo=int(input("Ingrese el código de la pizza:"))
                if codigo>0:
                    if any(p["codigo"]==codigo for p in ListaPizzas):
                        print("El código ya existe. Ingrese un código diferente.")
                        print("Ingrese cualquier tecla...")
                        msvcrt.getch()
                    else:
                        break
                else:
                    print("El codigo debe ser superior a 0")
                    print("Ingrese cualquier tecla...")
                    msvcrt.getch()
            except:
                print("Ingrese un codigo númerico positivo")
                print("Ingrese cualquier tecla...")
                msvcrt.getch()
        # pedimos el nombre de la pizza y validamos
        while True:
                nombre=input("Ingrese el nombre de la pizza: ").strip()
                if len(nombre)>4:
                    if any(p["nombre"].lower() == nombre.lower() for p in ListaPizzas):
                        print("El nombre ya existe. Ingrese un nombre diferente.")
                        print("Ingrese cualquier tecla...")
                        msvcrt.getch()
                    else:
                        break
                else:
                    print("Nombre muy corto para tu pizza")
                    print("Ingrese cualquier tecla...")
                    msvcrt.getch()
        # Masa masa masa masa masa
        while True:
            #si esto funciona queda mamalon
            print("\nTipos de masa disponibles:")
            for i, masa in enumerate(tipoMasa, start=1):
                print(f"{i}. {masa}")
            try:
                masa=int(input("Seleccione el múmero del tipo de masa: "))
                if masa>0 or masa<5:
                    break
                else:
                    print("Numero no valido")
                    print("Ingrese cualquier tecla...")
                    msvcrt.getch()
            except:
                print("Ingrese un numero valido")
                print("Ingrese cualquier tecla...")
                msvcrt.getch()
        masaP=tipoMasa[masa - 1]
        
        # Precio de la pizza
        while True:
            try:
                precio=float(input("Ingrese el precio de la pizza: "))
                if precio>9999:
                    break
                else:
                    print("El precio debe ser superior a 9999.")
                    print("Ingrese cualquier tecla...")
                    msvcrt.getch()
            except ValueError:
                print("Error. Por favor, ingrese un número válido para el precio.")
                print("Ingrese cualquier tecla...")
                msvcrt.getch()
        #stock de las pizzas
        while True:
            try:
                stock=int(input("Ingrese el stock de la pizza: "))
                if stock>0:
                    break
                else:
                    print("Como que estas ingresando una pizza con stock cero? seras.")
                    print("Ingrese cualquier tecla...")
                    msvcrt.getch()
            except ValueError:
                print("Error. Por favor, ingrese un número válido para el stock.")
                print("Ingrese cualquier tecla...")
                msvcrt.getch()
        pizza={
            "codigo": codigo,
            "nombre": nombre,
            "masa": masaP,
            "precio": precio,
            "stock": stock 
        }

        ListaPizzas.append(pizza)

    elif opcion=="2":
        #validamos que haya pizzas registradas
        if len(ListaPizzas)==0:
            print("No hay pizzas registradas.")
            print("Ingrese cualquier tecla...")
            msvcrt.getch()
        else:
            #llegaron las pipsas
            print("\n--- LISTA DE PIZZAS ---")
            for p in ListaPizzas:
                print(f"codigo: {v["codigo"]}, Nombre: {v["nombre"]}, tipo de masa: {v["masa"]}, precio: {v["precio"]}, stock: {v["stock"]}")
            print("Ingrese cualquier tecla.")
            msvcrt.getch()
    elif opcion=="3":
        while True:
            try: 
                codigo=int(input("Ingrese el código del vieojuego a modificar: "))
                break
            except:
                print("Ingrese un número valido")
                print("Ingrese cualquier tecla...")
                msvcrt.getch()
        encontrado=False
        for v in videosjuegos:
            if v["codigo"]==codigo:
                v["nombre"]==input("Nuevo nombre: ").strip()
                v["genero"]==input("Nuevo género: ")

                print("\nPlataformas disponibles:")
                print("1. PC")
                print("2. PS5")
                print("3. Xbox Serie X")
                print("4. Nintengo switch")
                while True:
                    try:
                        plataforma_codigo=int(input("Seleccione el número de la nueva plataforma: "))
                        if plataforma_codigo>0 and plataforma_codigo<5:
                            break
                        else:
                            print("Numero no valido")
                            print("Ingrese cualquier tecla...")
                            msvcrt.getch()
                    except:
                        print("Ingrese un numero valido")
                        print("Ingrese cualquier tecla...")
                        msvcrt.getch()
                v["plataforma"]=plataformas[plataforma_codigo - 1]
                #Otra vez se hace esto 

                print("Videojuego modificado correctamente.")
                time.sleep(2)
                encontrado=True
                break
        if not encontrado:
            print("Videojuego no encontrado.")
            print("Ingrese cualquier tecla...")
            msvcrt.getch()

    elif opcion=="4":
        while True:
            try:
                codigo=int(input("Ingrese el código del viojuego a eliminar: "))
                break
            except:
                print("ingrese un codigo valido")
                print("Ingrese cualquier tecla...")
                msvcrt.getch()
        eliminado=False
        for v in videosjuegos:
            if v["codigo"]==codigo:
                videosjuegos.remove(v)
                print("Videojuego eliminado correctamente.")
                print("Ingrese cualquier tecla...")
                msvcrt.getch()
                eliminado=True
                break
        if not eliminado:
            print("Videojuego no encontrado.")
            print("Ingrese cualquier tecla...")
            msvcrt.getch()

    elif opcion=="5":
        print("Saliendo del programa.")
        break
    else:
        print("Opcion inválida.")
        print("Ingrese cualquier tecla...")
        msvcrt.getch()