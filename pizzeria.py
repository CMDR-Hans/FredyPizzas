#Creamos una lista vacia para almacenar las pizzas
ListaPizzas=[]
Lista_pedidos=[]
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
                nombre=input("Ingrese el nombre de la pizza: ").strip().lower()
                if len(nombre)>4:
                    if any(p["nombre"]==nombre.lower() for p in ListaPizzas):
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
                precio=int(input("Ingrese el precio de la pizza: "))
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
                print(f"codigo: {p["codigo"]}, Nombre: {p["nombre"]}, tipo de masa: {p["masa"]}, precio: {p["precio"]}, stock: {p["stock"]}")
            print("Ingrese cualquier tecla.")
            msvcrt.getch()
    elif opcion=="3":
        #realizar pedido
        if len(ListaPizzas)==0:
            print("No hay pizzas registradas para realizar un pedido.")
            print("Ingrese cualquier tecla...")
            msvcrt.getch()
        else:
            #pedimo el nombre del cliente
            while True:
                nombre_cliente=input("Ingrese el nombre del cliente: ").strip().lower()
                #validamos que el nombre no este vacio
                if len(nombre_cliente)>=3 and nombre_cliente.isalpha():
                    break
                else:
                    print("Nombre muy corto o inválido para el cliente.")
                    print("Ingrese cualquier tecla...")
                    msvcrt.getch()
            
            #pedimos el codigo de la pizza    
            while True:
                try:
                    codigopedido=int(input("Ingrese el código de la pizza que desea pedir: "))
                    if codigopedido>0:
                        break
                    else:
                        print("El código debe ser un número positivo.")
                        print("Ingrese cualquier tecla...")
                        msvcrt.getch()
                except ValueError:
                    print("Error. Por favor, ingrese un número válido para el código.")
                    print("Ingrese cualquier tecla...")
                    msvcrt.getch()
            #cantidad de pizzas a pedir
            while True:
                try:
                    cantidad_Pizzas=int(input("Ingrese la cantidad de pizzas a pedir: "))
                    if cantidad_Pizzas>0:
                        break
                    else:
                        print("La cantidad debe ser un número positivo.")
                        print("Ingrese cualquier tecla...")
                        msvcrt.getch()
                except ValueError:
                    print("Error. Por favor, ingrese un número válido para la cantidad.")
                    print("Ingrese cualquier tecla...")
                    msvcrt.getch()
            encontrado=False
            for p in ListaPizzas:
                if p["codigo"]==codigo:
                    if p["stock"]>=cantidad_Pizzas:
                        p["stock"]-=cantidad_Pizzas
                        print(f"Pedido realizado exitosamente para {nombre_cliente}.")
                        print(f"Cantidad de pizzas: {cantidad_Pizzas}, Total a pagar: {p['precio'] * cantidad_Pizzas}")
                        print("Ingrese cualquier tecla...")
                        msvcrt.getch()
                        encontrado=True
                        compra_Pizza={
                            "cliente": nombre_cliente,
                            "codigo_pizza": p["codigo"],
                            "nombre_pizza": p["nombre"],
                            "cantidad": cantidad_Pizzas,
                            "total": p["precio"] * cantidad_Pizzas
                        }
                        Lista_pedidos.append(compra_Pizza)
                        break
                    else:
                        print(f"No hay suficiente stock de la pizza {p['nombre']}. Stock disponible: {p['stock']}")
                        print("Ingrese cualquier tecla...")
                        msvcrt.getch()
                        encontrado=True
                        break
            if not encontrado:
                print("Pizza no encontrada.")
                print("Ingrese cualquier tecla...")
                msvcrt.getch()

    elif opcion=="4":
        #ver pedidos realizados
        if len(ListaPizzas)==0:
            print("No hay pedidos realizados.")
            print("Ingrese cualquier tecla...")
            msvcrt.getch()
        else:
            print("\n--- PEDIDOS REALIZADOS ---")
            for p in Lista_pedidos:
                print(f"Cliente: {p['cliente']}, Código de pizza: {p['codigo_pizza']}, Nombre de pizza: {p['nombre_pizza']}, Cantidad: {p['cantidad']}, Total: {p['total']}")
            print("Ingrese cualquier tecla...")
            msvcrt.getch()

    elif opcion=="5":
        print("arrivederci.")
        break
    else:
        print("Opcion inválida.")
        print("Ingrese cualquier tecla...")
        msvcrt.getch()