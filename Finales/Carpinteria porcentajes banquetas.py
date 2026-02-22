"""La carpintería "La banqueta loca" quiere llevar el registro de los pedidos del mes, para ello se ingresan:
día entre 1 y 31 cantidad no negativa
código cliente entre 10 y 15
modelo Redondo, alta, baja (guardar en mayusculas)
la carga finaliza con dia 0 Se pide:
A) la cantidad de ventas realizadas (len(dias))
B) la cantidad de banquetas encargadas (sumar_cantidades)
C) el promedio de ventas (promediar)
D) la cantidad de banquetas pedidas x cliente (sumar_x_cliente_2)
E) porcentajes de banquetas de cada cliente sobre el total
F) porcentaje de cada modelo"""

# FUNCIONES

def cargar_pedidos(arr_dia,arr_cant,arr_cliente,arr_mod):
    dia = int(input("Ingrese Día (1-31) (0 finaliza): "))    
    while dia != 0:
        while dia < 1 or dia > 31:
            dia = int(input("Error - Ingrese Día (1-31) (0 finaliza): "))
        cantidad = int(input("Ingrese Cantidad: ")) 
        while cantidad < 0:
            cantidad = int(input("Error - Ingrese Cantidad: ")) 
        cliente = int(input("Ingrese Código Cliente (10-15): "))
        while cliente < 10 or cliente > 15:
            cliente = int(input("Error - Ingrese Código Cliente (10-15): "))
        modelo = input("Ingrese el modelo (Redonda(R), Alta(A) o Baja(B)): ").upper()
        while modelo != "R" and modelo != "A" and modelo != "B" or modelo == "":
            modelo = input("Error - Ingrese el modelo (Redonda(R), Alta(A) o Baja(B)): ").upper()
        arr_dia.append(dia)
        arr_cant.append(cantidad)
        arr_cliente.append(cliente)
        arr_mod.append(modelo)  
        dia = int(input("Ingrese Día (1-31) (0 finaliza): "))


def sumar_cantidades(arr_cant):
    total_general = 0
    i = 0
    while i < len(arr_cant):
        total_general += arr_cant[i]
        i += 1
    return total_general

def mostrar_datos(arr_dia,arr_cant,arr_cliente,arr_mod):
    titulo = "Dia"
    titulo1 = "Cantidad"
    titulo2 = "Cliente"
    titulo3 = "Modelo"
    print("---------------------------------------")
    print(f"{titulo:<5}{titulo1:>10}{titulo2:>13}{titulo3:>11}")
    print("---------------------------------------")
    for i in range(len(arr_dia)):
        print(f"{arr_dia[i]:<5}{arr_cant[i]:>10}{arr_cliente[i]:>13}{arr_mod[i]:>11}")

# Cantidad de banquetas pedidas por cliente
def pedidos_cliente(arr_cliente, arr_cantidades):
    totales_cliente = [0] * 6   # 1. Creamos el arreglo para acumular (clientes 10 al 15)
    i = 0
    while i < len(arr_cliente):  # 2. Recorremos los arreglos de entrada
        codigo = arr_cliente[i]
        cantidad = arr_cantidades[i]
        indice = codigo - 10      # 3. Calculamos el índice correspondiente (10->0, 11->1, ..., 15->5)
        if 0 <= indice < 6:       # 4. Validamos que el código esté entre 10 y 15 para no romper el programa
            totales_cliente[indice] += cantidad  # 5. Acumulamos la cantidad en el índice correspondiente
        i += 1                     # 6. Incrementamos el índice del bucle
    
    titulo = "Cliente" 
    titulo1 = "Banquetas"
    print(f"\n{titulo:<14}{titulo1:>14}")
    print("------------------------------")
    j = 0
    while j < 6: 
        cliente_id = j + 10
        print(f"{cliente_id:<14}{totales_cliente[j]:>14}")
        j += 1
                    
# Porcentajes de banquetas de cada cliente sobre el total
def calcular_porc_cliente(arr_cliente, arr_cantidades):
    total_general = sumar_cantidades(arr_cantidades)
    
    i = 0
    while i < len(arr_cliente):
        cliente = i + 10
        cantidad = arr_cantidades[i]
        
        if cantidad > 0:
            porcentaje = (cantidad / total_general) * 100
            print(f"Cliente {cliente}: {porcentaje:.2f}%")
        else:
            print("\nNo hay banquetas para calcular porcentajes.")
        i += 1

# Porcentaje de cada modelo
def calcular_porc_modelo(arr_modelos, arr_cantidades):
    #Calcula y muestra el porcentaje de banquetas de cada modelo.
    total_general = sumar_cantidades(arr_cantidades)
    cant_redondo = 0 # Inicializar contadores
    cant_alta = 0
    cant_baja = 0
    i = 0
    while i < len(arr_modelos):
        modelo = arr_modelos[i]
        cantidad = arr_cantidades[i]
        
        if modelo == "R":
            cant_redondo += cantidad
        elif modelo == "A":
            cant_alta += cantidad
        elif modelo == "B":
            cant_baja += cantidad
        i += 1
    porc_redondo = (cant_redondo / total_general) * 100
    print(f"Mod. Redonda: {porc_redondo:.2f}%")
    porc_alta = (cant_alta / total_general) * 100
    print(f"Modelo Alta: {porc_alta:.2f}%")
    porc_baja = (cant_baja / total_general) * 100
    print(f"Modelo Baja: {porc_baja:.2f}%")

# ---------- PROGRAMA PRINCIPAL ----------

print("\nRegistro de pedidos - Banqueta LOCA")
print("---------------------------------------\n")

dias = []
cantidades = []
clientes = []
modelos = []

cargar_pedidos(dias, cantidades, clientes, modelos)

print("\n---------------------------------------")

if len(cantidades) > 0:
    total_ventas = len(cantidades)
    print(f"\nA. Cantidad de ventas realizadas: {total_ventas}\n")
    total_banquetas = sumar_cantidades(cantidades)
    print(f"B. Total de banquetas encargadas: {total_banquetas}\n")
    mostrar_datos(dias, cantidades, clientes, modelos)
    if total_ventas > 0:
        promedio_banquetas = total_banquetas / total_ventas
        print(f"\nC. Promedio de banquetas por venta: {promedio_banquetas:.2f}\n")
    else:
        print("\nC. No se registraron ventas (no hay promedio).")
    print("\nD. Banquetas pedidas por cliente:\n") 
    pedidos_cliente(clientes, cantidades)
    print("\nE. Porcentajes por cada cliente:\n") 
    calcular_porc_cliente(clientes, cantidades)
    print("\nF. Porcentaje de cada modelo:\n")
    calcular_porc_modelo(modelos, cantidades)
else:
    print("No se ingresaron pedidos.\n")
print("\nFin del programa.\n")