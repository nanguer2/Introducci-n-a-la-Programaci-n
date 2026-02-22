"""En base a los conceptos vistos en el módulo, debés realizar el siguiente ejercicio: 
Ingresar números enteros hasta que sea dicho número cero y cargar un arreglo con aquellos números múltiplos de 5. 
Mostrar el arreglo y calcular:
a. Los 3 primeros números más grandes.
b. Generar otro arreglo con los números múltiplos de 10. Si no los hubiera mostrar una leyenda.
c. Eliminar del arreglo original el valor mínimo. Si los hubiera repetido, eliminar todas las apariciones del elemento mínimo
"""

# --- FUNCIONES ---
def cargar_datos(arr_multi5):
    print("\n--- Entrada de Datos ---\n")
    num = int(input("Ingrese un número entero (0 para terminar): "))
    while num != 0:
        if num % 5 == 0:
                arr_multi5.append(num)
        num = int(input("Ingrese un número entero (0 para terminar): "))

def mostrar_arreglo(arr,):
    #Muestra el contenido de un arreglo.
    if len(arr) == 0:
        print("\nEl arreglo está vacío.")
    else:
        print(f"\nArreglo: {arr}")

# a. Los 3 primeros números más grandes.
def mostrar_3_mayores(arreglo):
    copia = []
    for i in arreglo:
        copia.append(i)
    
    copia.sort()
    copia.reverse()
    
    # Determinamos cuántos mostrar (mínimo entre 3 y el largo del arreglo)
    limite = 3
    if len(copia) < 3:
        limite = len(copia)
        
    for i in range(limite):
        print(f"{i+1}° puesto: {copia[i]}")
        
# b. Generar otro arreglo con los números múltiplos de 10.
def generar_multiplos_10(arr_mult_5, arr_mult_10):
    for i in arr_mult_5:
        if i % 10 == 0:
            arr_mult_10.append(i)
    return arr_mult_10

# calcular el minimo.
def calcular_minimo(arre):
    pos_min = 0
    for i in range (1, len(arre)):
        if arre[i]  < arre[pos_min]:
            pos_min = i
    return pos_min

def eliminar_minimo_repetido(arr):
    if len(arr) == 0:
        print("\nEl arreglo está vacío, no se puede eliminar el mínimo.")
    else:
        # 1. Obtenemos el ÍNDICE del mínimo
        posicion_minimo = calcular_minimo(arr)
        # 2. Guardamos el VALOR real que hay en esa posición
        valor_a_borrar = arr[posicion_minimo]
        i = 0
        while i < len(arr):
            if arr[i] == valor_a_borrar: # Comparamos contra el valor real
                arr.pop(i)
                # Al usar pop, los elementos de la derecha se desplazan a la izquierda
            else:
                i += 1   
        
        print(f"\nValor mínimo a eliminar: {valor_a_borrar}.")
        print("Se eliminaron todas sus apariciones.")
              
# --- PROGRAMA PRINCIPAL ---

multiplos5 = []
multiplos10 = []

# 1. Cargar y filtrar (Orden correcto)
cargar_datos(multiplos5)

# 2. Verificar si hay múltiplos de 5 para trabajar
if len(multiplos5) > 0:
    print("\n--- Procesando Múltiplos de 5 ---")
    mostrar_arreglo(multiplos5)
    
    # a. Los 3 más grandes
    print("\n--- 3 primeros números grandes ---\n")
    mostrar_3_mayores(multiplos5)
    
    # b. Generar y mostrar múltiplos de 10
    generar_multiplos_10(multiplos5, multiplos10)
    if len(multiplos10) > 0:
        print("\n--- Múltiplos de 10 encontrados ---")
        mostrar_arreglo(multiplos10)
    else:
        print("\nLeyenda: No existen múltiplos de 10.")
        
    # c. Eliminar mínimo y mostrar resultado final
    print("\n--- Eliminar mínimo ---")
    eliminar_minimo_repetido(multiplos5)
    print("\nArreglo final (Múltiplos de 5 sin el mínimo):")
    mostrar_arreglo(multiplos5)
    
else:
    print("\nNo se ingresaron datos.")

print("\n--- Fin del programa ---\n")
