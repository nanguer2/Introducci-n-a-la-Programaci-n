""" Una empresa de logística necesita un sistema para gestionar el pesaje de sus productos antes de ser despachados. 
Para ello, se solicita desarrollar un programa en Python que utilice vectores paralelos para almacenar el Nombre del Producto y su Peso (en kg).

Tareas a realizar:
a) Carga de Datos: Implementar una función que permita cargar los productos. La carga finaliza cuando el usuario ingresa "FIN".
En el nombre del producto. Se debe validar que el peso sea un valor positivo.
b) Peso Promedio: Crear una función que calcule y retorne el peso promedio de todos los productos ingresados. 
Mostrar el resultado por pantalla.
c) Producto más Liviano: Desarrollar una función que busque el peso mínimo de forma programática (sin ordenar).
Mostrar el peso como el nombre del producto asociado.
d) Limpieza por Promedio: Diseñar una función que elimine de ambos arreglos todos aquellos productos cuyo peso sea estrictamente mayor al 
promedio calculado en el punto 2. Al finalizar, mostrar la tabla actualizada.
e) Reemplazo Crítico: Implementar una función que busque productos con un peso superior a 15 kg. En esos casos, se debe reemplazar el nombre del
producto por la cadena "REEMPLAZADO" y su peso por el valor 999.
f) Ordenamiento Logístico: Crear una función que ordene ambos vectores de manera ascendente (de menor a mayor) basándose en el peso, 
utilizando el método de intercambio (Burbuja). Mostrar la tabla final resultante. """

#--- FUNCIONES ---
def cargar_productos(arr_nombres, arr_pesos):
    print("\n--- CARGA DE PRODUCTOS (Logística) ---")
    nombre = input("\nProducto (o 'FIN' para terminar): ").upper()
    
    while nombre != "FIN":
        while nombre == "":
            nombre = input("Error - Producto (o 'FIN' para terminar): ").upper()
        if nombre != "FIN":    
            peso = float(input(f"Ingrese el peso de '{nombre}' (kg): "))
            while peso <= 0:
                peso = float(input(f"Error (debe ser > 0) - Peso de '{nombre}': "))
                
        arr_nombres.append(nombre)
        arr_pesos.append(peso)
        
        nombre = input("\nProducto (o 'FIN' para terminar): ").upper()
            
        
def mostrar_datos(arr_nombres, arr_pesos):
    print(f"{'PRODUCTO':<20}{'PESO (kg)':<10}")
    print("-" * 32)
    for i in range(len(arr_nombres)):
        print(f"{arr_nombres[i]:<20}{arr_pesos[i]:<10.2f}")

# 1. Calcular promedio:
def calcular_promedio(arr_pesos):
    acum = 0
    cant = 0
    i = 0
    while i < len(arr_pesos):
        acum += arr_pesos[i]
        cant += 1
        i += 1
    if cant >0:
        prom =  acum/cant
    return prom

# 2. Buscar mínimo:
def buscar_minimo(arr_pesos):
    pos_min = 0
    for i in range(1, len(arr_pesos)):
        if arr_pesos[i] < arr_pesos[pos_min]:
            pos_min = i
    return pos_min

# 3. Eliminar productos con peso mayor al promedio:
def eliminar_mayor_promedio(arr_nombres, arr_pesos):
    prom = calcular_promedio(arr_pesos)
    print(f"Eliminando > {prom:.2f} kg...\n")
    
    i = 0
    while i < len(arr_pesos):
        if arr_pesos[i] > prom:
            arr_nombres.pop(i)
            arr_pesos.pop(i)
            # Al eliminar, no incrementamos i porque el siguiente cae en esta posición
        else:
            i += 1

# 4. Reemplazar valores > 15
def reemplazar_valores(arr_nombres, arr_pesos):
    for i in range(len(arr_pesos)):
        if arr_pesos[i] > 15:
            arr_nombres[i] = "REEMPLAZADO"
            arr_pesos[i] = 999
            

def intercambiar(arr_mod, i, j):
    # Intercambia dos elementos en un arreglo (para ordenamiento).
    aux = arr_mod[i]
    arr_mod[i] = arr_mod[j]
    arr_mod[j] = aux

# 5. Ordenar de menor a mayor (Burbuja)
def ordenar_menor_mayor(arr_nombres, arr_pesos):
    for i in range(len(arr_pesos)- 1):
        for j in range(i + 1, len(arr_pesos)):
            if arr_pesos[i] > arr_pesos[j]:
                # Intercambiamos ambos vectores para mantener el paralelismo
                intercambiar(arr_pesos, i, j)
                intercambiar(arr_nombres, i, j)

# --- PROGRAMA PRINCIPAL ---

nombres = []
pesos = []

cargar_productos(nombres, pesos)

if len(pesos) > 0:
    # 1. Peso promedio.
    print("\n1. Peso promedio:")
    promedio_gral = calcular_promedio(pesos)
    print(f"\nEl promedio de los pesos es: {promedio_gral:.2f} kg")

    # 2. Buscar mínimo.
    print("\n2. Buscar mínimo:")
    idx_min = buscar_minimo(pesos)
    print(f"\nEl menor peso es {pesos[idx_min]:.2f} kg del producto {nombres[idx_min]}")

    # 3. Eliminar mayores al promedio.
    print("\n3. Eliminar mayores al promedio:")
    if len(pesos) > promedio_gral:
        eliminar_mayor_promedio(nombres, pesos)
        mostrar_datos(nombres, pesos)
    else:
        print("\nNo hay mayores al promedio.")
    # 4. Reemplazar valores > 15
    print("\n4. Reemplazar valores > 15:\n")
    reemplazar_valores(nombres, pesos)
    mostrar_datos(nombres, pesos)

    # 5. Ordenar de menor a mayor
    print("\n5. Ordenar pesos (Ascendente):\n")
    ordenar_menor_mayor(nombres, pesos)
    mostrar_datos(nombres, pesos)

else:
    print("\nNo se cargaron productos.")

print("\nFin del programa.\n")