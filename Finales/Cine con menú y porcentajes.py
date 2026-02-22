"""Se quiere realizar un control de ventas de entradas para el cine. Hay 3 tipos de entradas y precios a la venta: 2D: ARS 2000   3D: ARS 2700   4D: ARS 3500
El sistema debe ofrecer un menú con las siguientes opciones:
1)  Cargar entradas
2)  Mostrar mayor venta
3)  Calcular ganancias
4)  Calcular porcentaje
5)  Salir
Se deberá guardar la información en 2 listas paralelas: una para el tipo de entrada y otra para la cantidad vendida. La carga se detiene al ingresar la palabra "FIN" en el tipo de entrada. Se deberá validar que la cantidad a ingresar no sea negativa. Además se requiere crear funciones que realicen las siguientes operaciones:
a) Calcular que tipo de entrada fue la más vendida.
b) Buscar y calcular la ganancia total de ventas de un tipo de entrada pasada por parámetro.
c) Buscar y calcular el porcentaje de entradas vendidas de un tipo de entrada pasada por parámetro. Todas las funciones deben retornar el resultado obtenido y ser usado/mostrado en la secuencia de ejecución."""

# --- FUNCIONES ---

def mostrar_menu():
    print("\n--- SISTEMA DE VENTAS CINE ---\n")
    
    print("1) Cargar entradas")
    print("2) Mostrar tipo de entrada más vendida")   
    print("3) Calcular ganancia por tipo")
    print("4) Calcular porcentaje por tipo")
    print("5) Salir")
    
    op = int(input("\nSeleccione una opción (1-5): "))
    while op < 1 or op > 5:
        op = int(input("Error - Seleccione una opción (1-5): "))
    return op


def ingresar_tipo(): 
    tipo_entrada = input("Ingrese tipo de entrada (2D, 3D, 4D o FIN): ").upper()   
    while tipo_entrada != "FIN" and tipo_entrada != "2D" and tipo_entrada != "3D" and tipo_entrada != "4D":
        tipo_entrada = input("Error - Ingrese tipo entrada de entrada (2D, 3D, 4D o FIN): ").upper()  
    return tipo_entrada


def ingresar_cantidad(tipo):            
    cantidad_entrada = int(input(f"Cantidad de entradas {tipo}: "))
    while cantidad_entrada < 0:
        cantidad_entrada = int(input("Error: La cantidad no puede ser negativa: "))
    return cantidad_entrada


def cargar_entradas(arr_tipos, arr_cantidades):
    tipo = ingresar_tipo()
    while tipo == "2D" or tipo == "3D" or tipo == "4D":
        cantidad = ingresar_cantidad(tipo)
        arr_tipos.append(tipo)
        arr_cantidades.append(cantidad)
        tipo = ingresar_tipo()   
    print("\nCarga de datos finalizada...")        

# A) Calcular que tipo de entrada fue la más vendida.
def calcular_mayor_venta (arr_cantidades):      
    pos_mayor = 0
    i = 0
    for i in range (len(arr_cantidades)):
        if arr_cantidades[i] > arr_cantidades[pos_mayor]:
            arr_cantidades[pos_mayor] = arr_cantidades[i]
            pos_mayor = i
    return pos_mayor    

# A) Calcular que tipo de entrada fue la más vendida (Acumulado por tipo).
def calcular_tipo_mas_vendido(arr_tipos, arr_cantidades):
    t_2d = 0; t_3d = 0; t_4d = 0
    i = 0
    while i < len(arr_tipos):
        if arr_tipos[i] == "2D": t_2d += arr_cantidades[i]
        elif arr_tipos[i] == "3D": t_3d += arr_cantidades[i]
        elif arr_tipos[i] == "4D": t_4d += arr_cantidades[i]
        i += 1
    
    # Comparamos totales acumulados
    if t_2d >= t_3d and t_2d >= t_4d:
        return "2D", t_2d
    elif t_3d >= t_2d and t_3d >= t_4d:
        return "3D", t_3d
    else:
        return "4D", t_4d
             
# Calcula el total general. 
def total_entradas(arr): 
    acum = 0
    i = 0
    while i < len(arr):
        acum = acum + arr[i]
        i += + 1
    return acum

# Retorna el precio según el tipo de entrada.   
def obtener_precio(tipo_entrada): 
    if tipo_entrada == "2D":
        precio = 2000
    elif tipo_entrada == "3D":
        precio = 2700
    elif tipo_entrada == "4D":
        precio = 3500
    return precio

  
# B) Buscar y calcular la ganancia total de ventas de un tipo de entrada.
def calcular_ganancia_tipo(arr_tipo, arr_cant, tipo_buscado):
    ganancia_total = 0
    precio = obtener_precio(tipo_buscado)
    
    if precio > 0:           
        i = 0
        while i < len(arr_tipo):
            if arr_tipo[i] == tipo_buscado:
                ganancia_total = ganancia_total + (arr_cant[i] * precio)
            i += 1
    return ganancia_total

#C) Buscar y calcular el porcentaje por tipo de entrada.
def calcular_porcentaje_tipo(arr_tipos, arr_cantidades, tipo_buscado):      
    total_tipo = 0
    total_general = total_entradas(arr_cantidades)
    i = 0
    
    while i < len(arr_tipos):
        if arr_tipos[i] == tipo_buscado:
            total_tipo += arr_cantidades[i]
        i += 1    
        
    if total_general > 0 and tipo_buscado != "FIN":
        porcentaje = (total_tipo / total_general) * 100
    return porcentaje

def mostrar_tabla(arr_tipos, arr_cantidades):
    titulo = "Tipo"
    titulo1= "Cantidad"
                   
    print(f"\n\t{titulo:<20}{titulo1}")
    print("---------------------------------------")
    for i in range(len(arr_tipos)):
        print(f"\t{arr_tipos[i]:<20}{arr_cantidades[i]}")
    print("---------------------------------------")
       
# --- PROGRAMA PRINCIPAL ---
tipos = []
cantidades = []

opcion = mostrar_menu()
while opcion != 5:
    
    if opcion == 1:
        print("\n1) Cargar entradas:\n")
        cargar_entradas(tipos,cantidades)
        if len(tipos) > 0:
            mostrar_tabla(tipos,cantidades)   
        else:
            print("No hay datos cargados.")
    elif opcion == 2:
        print("\n2) Mostrar tipo de entrada más vendida:\n")
        valor_max = calcular_mayor_venta(cantidades)
        print(f"\n**EL tipo de entrada mas vendida es: {tipos[valor_max]}, con un total de {cantidades[valor_max]}.**")
        nom_tipo, total_v = calcular_tipo_mas_vendido(tipos, cantidades)
        print(f"\n**El tipo más vendido es: {nom_tipo}, con un total de {total_v} entradas.**")
    elif opcion == 3:
        print("\n3) Calcular ganancia por tipo:\n")
        if len(tipos) > 0:
            tipo = input("Ingrese el tipo (2D/3D/4D) para calcular su ganancia: ").upper()
            ganancia = calcular_ganancia_tipo(tipos,cantidades,tipo)
            print(f"\n**La ganancia total para {tipo} es: ARS {ganancia}.**")
        else:
            print("No hay datos cargados.")
    elif opcion == 4:
        print("\n4) Calcular porcentaje por tipo:\n")
        if len(tipos) > 0:
            tipo1 = input("Ingrese el tipo (2D/3D/4D) para calcular su porcentaje: ").upper()
            porc = calcular_porcentaje_tipo(tipos,cantidades,tipo1)
            print(f"\n**El tipo {tipo1} representa el {porc:.2f}% del total de entradas vendidas.**")
        else:
            print("No hay datos cargados.")

    opcion = mostrar_menu()
print("\nSaliendo del sistema... ¡Gracias!")
print("\nFin del programa.\n") 