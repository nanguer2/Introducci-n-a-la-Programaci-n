"""2. Ingresar valores numéricos enteros hasta cargar un arreglo con:
los 8 primerosnumeros pares multiplos de 3. 
A. Mostrarlo.
B. Mostrar los 2 valores más pequeños multiplos de 6. Si no los hubiese mostrar una leyenda.
C. Eliminar del arreglo aquellos valores menores a su promedio.
D. Insertar en dicho arreglo despues de cada número su doble"""

# FUNCIONES
def leer_entero():
    # Solo validamos la condición del ejercicio (ser par y múltiplo de 3).
    valor = int(input("Ingrese un valor numérico entero: "))
    while valor < 0:
        valor = int(input("Error - Ingrese un valor numérico entero: "))
    return valor


def cargar_numeros_multiplos_6(arreglo, cantidad):
    # Ingresa valores hasta cargar el arreglo con el límite (8) de números pares múltiplos de 3. 
    while len(arreglo) < cantidad:
        numero = leer_entero()
        # Validación: es par y múltiplo de 3 (múltiplo de 6)
        if numero % 6 == 0:
            arreglo.append(numero)
            print(f"Número {numero} agregado. Faltan {cantidad - len(arreglo)}.\n")
        else:
            print(f"El número {numero} no es par y múltiplo de 3. Ingrese otro.\n")


def mostrar_arreglo(numero):
    print("---------------------------------------")
    print(numero)
    print("---------------------------------------\n")


def obtener_dos_minimos_multiplos_6(arr):
   
    if len(arr) < 2:
        print("\nNo hay suficientes datos.")

    else:    # 1. Hallar la posición del primer mínimo
        pos_min1 = 0
        for i in range(len(arr)):
            if arr[i] < arr[pos_min1]:
                pos_min1 = i
        
        # 2. Hallar la posición del segundo mínimo (VALOR DISTINTO)
        # Buscamos la primera posición que tenga un valor diferente al min1 para inicializar
        pos_min2 = -1 
        for i in range(len(arr)):
            if arr[i] > arr[pos_min1]:
                if pos_min2 == -1 or arr[i] < arr[pos_min2]:
                    pos_min2 = i

    # 3. Mostrar resultados con validación
    valor1 = arr[pos_min1]
    
    if pos_min2 == -1:
        print(f"\nTodos los valores son iguales a {valor1}")
        print("No hay un segundo mínimo distinto.")
    else:
        valor2 = arr[pos_min2]
        print(f"\nArreglo analizado: {arr}")
        print(f"1er Mínimo es: {valor1}")
        print(f"2do Mínimo (distinto) es: {valor2}")
       
# Calcula el promedio del arreglo.
def calcular_promedio(arr):
    cont = 0
    acumulador = 0
    i = 0
    while i < len(arr):
        acumulador += arr[i]
        cont += 1
        i += 1
    
    promedio = acumulador / cont
    return promedio


def eliminar_menores_al_promedio(arr):
    #C. Eliminar del arreglo aquellos valores menores a su promedio.
    promedio = calcular_promedio(arr)
    print(f"\nPromedio actual: {promedio:.2f}")
    
    i = 0
    while i < len(arr):
        if arr[i] < promedio:
            arr.pop(i)
            # No incrementamos 'i' porque el siguiente elemento ahora está en la posición actual
        else:
            i += 1


def insertar_doble(arr):
    #D. Insertar en dicho arreglo después de cada número, su doble."""
    # Recorremos el arreglo y duplicamos los elementos, insertando el doble
    i = 0
    while i < len(arr):
        valor_original = arr[i]
        valor_doble = valor_original * 2
        # Insertamos el doble en la posición siguiente (i+1)
        arr.insert(i + 1, valor_doble)
        # Avanzamos 'i' dos posiciones para saltar el elemento original y su doble
        i += 2

# ---------- PROGRAMA PRINCIPAL ----------
print("\n---------------------------------------")
print("    EJERCICIO DE ARREGLOS NUMÉRICOS")
print("---------------------------------------\n")

numeros = []
rango = 8

# Carga inicial (Ingresar hasta obtener 8 pares múltiplos de 3)
cargar_numeros_multiplos_6(numeros, rango)

# A) Mostrar el arreglo cargado
print("\nA. Mostrar el arreglo cargado:")
print("\n        8 Pares multiplos de 3            ")
mostrar_arreglo(numeros)


# B) Mostrar los 2 valores más pequeños múltiplos de 6.
print("B. Mostrar los 2 valores más pequeños:")
obtener_dos_minimos_multiplos_6(numeros)
print("---------------------------------------\n")

# C) Eliminar menores al promedio.
print("C. Eliminar menores al promedio:")
eliminar_menores_al_promedio(numeros)
print("\n            Pares restantes            ")
mostrar_arreglo(numeros)

#D. Insertar en dicho arreglo despues de cada número su doble.
print("D. Insertar el doble desués de cada uno:\n")
insertar_doble(numeros)
mostrar_arreglo(numeros)

print("Fin del programa.\n")