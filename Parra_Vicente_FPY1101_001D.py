productos= {
'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}

stock = {
'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0], 
}

def stock_marca(marca):
    total = 0
    for modelo, datos in productos.items():
        if datos[0].lower() == marca.lower():
            total += stock.get(modelo, [0, 0])[1]
    print(f"El stock es: {total}")

def buscar_por_precio(p_min, p_max):
    try:
        p_min = int(p_min)
        p_max = int(p_max)
    except ValueError:
        print("Debe ingresar valores enteros!!")
        return
    disponibles = []
    for modelo, (precio, cantidad) in stock.items():
        if p_min <= precio <= p_max and cantidad > 0:
            marca = productos[modelo][0]
            disponibles.append(f"{marca}--{modelo}")
            if disponibles:
                print("productos disponibles:", sorted(disponibles))
            else:
                print("No hay teléfonos en ese rango de precios.")

def actualizar_precio(modelo, nuevo_precio):
    if modelo in stock:
        stock[modelo][0] = nuevo_precio
        return True
    else:
        return False
def menu():
    while True:
        print("\n*** MENÚ PRINCIPAL ***")
        print("1. Stock por marca")
        print("2. Buscar por rango de precios")
        print("3. Actualizar precio de modelo")
        print("4. Salir")
        opcion = input("Ingrese opción: ")
        if opcion == '1':
            marca = input("Ingrese marca a consultar: ")
            stock_marca(marca)

        elif opcion == '2':
            p_min = input("Ingrese precio mínimo: ")
            p_max = input("Ingrese precio máximo: ")
            buscar_por_precio(p_min, p_max)

        elif opcion == '3':
            while True:
                modelo = input("Ingrese modelo a actualizar: ")
                try:
                    nuevo_precio = int(input("Ingrese precio nuevo: "))
                    if actualizar_precio(modelo, nuevo_precio):
                        print("Precio actualizado!!")
                    else:
                        print("El modelo no existe!!")
                except ValueError:
                    print("Debe ingresar un precio válido (entero)!!")

                seguir = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower()
                if seguir != 's':
                    break

        elif opcion == '4':
            print("Programa finalizado.")
            break

        else:
            print("Debe seleccionar una opción válida!!")


menu()
