# Arreglo con 10 números 5 positivos y 5.
""" Cargar y mostrar un arreglo con los primeros 5 úmeros positivos y los últimos 5 negativos. Calcular y mostrar:
a) El promedio de los números negativos.
b) Ordenar el arreglo de menor a mayor.
c) Mostrar cuantos pares y multiplos de 3 hay en este arreglo.
d) Otro arreglo con los números con los multiplos de 4. Si no hubiese, mostrar el cartel aclaratorio.
"""

#FUNCIONES
def cargar_datos(arr_pos, arr_neg):
    print("\n--- Registro de 5 Positivos y 5 Negativos ---") 
    # Primera lectura (Lectura anticipada)
    num_ent = int(input(f"\nIngrese un número (0 para finalizar): "))
    
    # El ciclo sigue mientras el número no sea 0 Y nos falte completar alguna lista
    while num_ent != 0 and (len(arr_pos) < 5 or len(arr_neg) < 5):
        if num_ent > 0 and len(arr_pos) < 5:
            arr_pos.append(num_ent)
            print(f"Cargado positivo ({len(arr_pos)}/5)")
        elif num_ent < 0 and len(arr_neg) < 5:
            arr_neg.append(num_ent)
            print(f"Cargado negativo ({len(arr_neg)}/5)")
        else:
            print("(!) Aviso: Ese cupo ya está lleno o el número no es válido.")

        # Verificamos si aún necesitamos pedir más números
        if len(arr_pos) < 5 or len(arr_neg) < 5:
            num_ent = int(input(f"\nSiguiente número (0 para finalizar): "))
        else:
            print("\n¡Ambos cupos completados!")

    print("\nCarga finalizada...") 
    return arr_pos + arr_neg 

def mostrar(arr):
    print(arr)


def promedio(arr):
    acum=0
    for i in range(len(arr)):
        acum += arr[i]
    prom=acum/5
    print(f"\na) El promedio de los números negativos es:\n\nPromedio: {prom:.2f}")
    return


def generar_multiplos_4(arr):
    mult4 = [] # 1. Creamos la lista vacía donde guardaremos los resultados
    
    for i in range(len(arr)):
        # 2. Verificamos si el número en la posición i es múltiplo de 4
        if arr[i] % 4 == 0:
            mult4.append(arr[i]) # 3. Agregamos el número, NO la lista
            
    return mult4 # 4. Devolvemos la lista llena


def cantidad(arr):
    pares=0
    mult3=0
    for i in range(len(arr)):
        if arr[i]%2 == 0:
            pares += 1
        if arr[i]%3 == 0:
            mult3 += 1
    print(f"La cantidad de números pares es: {pares}")
    print(f"La cantidad de multiplos de 3 es: {mult3}")
    return

#PPAL
print("\nCargar primero con los positivos y luego los negativos...\n")
pos = []
neg = []

arreglo = cargar_datos(pos,neg)
if len(arreglo) == 0:
    print("\nNo se ingresaron datos.")  
else:
    if len(pos) < 5 or len(neg) < 5:
        print("***No se completaron los 5 positivos y 5 negativos.")      
    print(f"\nArreglo inicial (5 pos y 5 neg):\n \n{arreglo}\n")
    print("\nFin de la carga de datos.\n")
    print("El arreglo cargado es:\n")
    mostrar(arreglo)
    # a) El promedio de los números negativos.
    promedio(neg)
    # b) Ordenar el arreglo de menor a mayor.
    print("\nb) Ordenar el arreglo de menor a mayor:\n")
    arreglo.sort()
    mostrar(arreglo)
    # c) Mostrar cuantos pares y multiplos de 3 hay en este arreglo.
    print("\nc) Mostrar cuantos pares y multiplos de 3 hay en el arreglo.\n")
    cantidad(arreglo)
    print("\nd) Otro arreglo con los números multiplos de 4.\n") 
    m=generar_multiplos_4(arreglo)
    if m == 0:
        print("No hay multiplos de 4")
    else:
        print(f"Los multiplos encontrados son: {m}")
print("\nFin del programa.\n")