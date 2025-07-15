
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}




def stock_marca():
        while True:
                
            marca = input("Ingrese la marca del computador: ").upper()
            if len(marca.strip()) <= 0:
                  print("No se puede dejar este espacio vacio, tampoco solo agregar espacios!!!!\n")
                  continue
            numeroSerie = []
            contadorMarca = 0
            for i in productos:
                  if marca == productos[i][0].upper():
                        contadorMarca += 1
                        numero = productos[i]
                        numeroSerie.append(numero)
                        

            if contadorMarca != 0:
                print(f"Se encontraron {contadorMarca} cantidad de productos de esa marca")
            else:      
                print("No se a encontrador el producto, intentelo nuevamente")
                continue

             
            for i in range(len(stock)):
                for j in stock:
                    if numeroSerie[i] == stock[i][0]:
                        print(f"STOCK - {stock[i][1]}")                

                    

def busqueda_precio(p_min,p_max):
    while True:
        modelo = input("Ingrese el modelo del ordenador:").upper()
        if len(modelo.strip()) <= 0:
            print("Debe ingresar texto , no se valido solo espacio\n")
            continue
        



#def actualizar_precio(modelo,p):
        
                  












while True:
    print("*** MENU PRINCIPAL ***")
    print("1 - Stock marca.")        
    print("2 - Busqueda por precio.")        
    print("3 - Actualizar precio.")
    print("4 - Salir")   
      

    try:
        opc = int(input("Ingrese la opcion deseada: "))
        if opc <= 0:
             print("Ingrese un numero mayor a 0!!!\n")
             continue
    except ValueError:
        print("Error: Ingrese la opcion deseada en un formato numerico valido!!!\n")
        continue



    if opc == 1:
        print(stock_marca)

    elif opc == 2:
        busqueda_precio(p_min,p_max)

    elif opc == 3:
        modelo = input("Ingrese el modelo del ordenador: ").upper()
        precio = int(input("Ingrese el precio del ordenador"))
        busqueda_precio(modelo,precio)

    elif opc == 4:
        print("Saliendo del menu!!")
        break         
