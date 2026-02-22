"""Se quiere llevar el control de preguntas para un nuevo juego. Para lo que se debe generar un sistema que cumpla con las 
siguientes características.
Cargar preguntas y sus puntajes (se deben usar arreglos paralelos)
La carga Finaliza cuando en pregunta se ingresa "FIN" o que la suma de los puntajes ingresados haya llegado a 150.
El puntaje que corresponde a cada pregunta debe ser mayor 0 y menor o igual a 25.
Se pide crear funciones que:
a) Determinar el mínimo puntaje ingresado y mostrar la pregunta a la que corresponde.
b) Calcular el puntaje promedio de las preguntas y genere y retorne un nuevo arreglo con las preguntas cuyo puntaje superen ese promedio.
c) Crear una función que muestre las preguntas y su puntaje"""

# FUNCIONES
def ingresar_pregunta():
    pregunta = input("\nIngrese la pregunta: ").upper()
    while pregunta == "":
        pregunta = input("Error - Ingrese la pregunta: ").upper()
    return pregunta


def ingresar_puntaje(arre_puntaje): # float o int es indistinto en este ejercicio
    puntaje = int(input("Ingrese el puntaje (0 < entero <= 25): "))
    while puntaje <= 0 or puntaje > 25 or chequear_resto(puntaje, arre_puntaje)==-1:
        puntaje = int(input("Ingrese el puntaje (0 < entero <= 25): "))
    return puntaje


def cargar_datos(arr_preguntas, arr_puntajes):
    pregunta = ingresar_pregunta()
    # Mientras no sea FIN y la suma sea menor a 150
    while pregunta != "FIN" and sumar_puntaje(arr_puntajes) < 150:
        puntaje = ingresar_puntaje(arr_puntajes)
        
        arr_preguntas.append(pregunta)
        arr_puntajes.append(puntaje)
        
        # Verificamos si aún podemos seguir cargando
        if sumar_puntaje(arr_puntajes) < 150:
            pregunta = ingresar_pregunta()
        else:
            print("--- Se ha alcanzado el límite de 150 puntos ---")
    
    
def chequear_resto(puntaje, arre_puntaje):
    resto = 150 - sumar_puntaje(arre_puntaje)
    if puntaje > resto:
        print(f"La suma de puntajes se pasa de 150. Disponible {resto} puntos.")
        return -1
    return 0


def sumar_puntaje(arre_puntaje):
    acumulador = 0
    if len(arre_puntaje) > 0:
        for i in range (len(arre_puntaje)):
            acumulador += arre_puntaje[i]
    return acumulador


def minimo_puntaje(arre_puntaje):
    indice_del_minimo = 0
    for i in range(1, len(arre_puntaje)):
        if arre_puntaje[i] < arre_puntaje[indice_del_minimo]:
            indice_del_minimo = i
    return indice_del_minimo


def mayor_promedio(arre_puntaje):
    arre_nuevo = []
    promedio = sumar_puntaje(arre_puntaje) / len(arre_puntaje)
    for i in range(len(arre_puntaje)):
        if arre_puntaje[i] > promedio:
            arre_nuevo.append(i)
    return arre_nuevo


def mostrar_arreglo(arre_pregunta, arre_puntaje):
    print("Mostrando todas las preguntas:\n")
    for i in range(len(arre_pregunta)):
        print(f"Pregunta {i+1}: {arre_pregunta[i]} ({arre_puntaje[i]} puntos)")


def mostrar_mayor_promedio(arre_pregunta, arre_puntaje, arre_promedio):
    print("Preguntas cuyos puntajes superan el promedio:\n")
    for i in range(len(arre_promedio)):
        print(f"Pregunta {arre_promedio[i]+1}: {arre_pregunta[arre_promedio[i]]} ({arre_puntaje[arre_promedio[i]]} puntos)")

# PROGRAMA PRINCIPAL
preguntas = []
puntajes = []

print("\n--- SISTEMA DE CONTROL DE PREGUNTAS ---")
# 1. Llamamos a la función de carga pasándole nuestras listas
cargar_datos(preguntas, puntajes)

# 2. Verificamos si se cargó algo
if len(preguntas) > 0:
    # a) Mínimo puntaje
    indice_minimo = minimo_puntaje(puntajes)
    
    # b) Preguntas que superan el promedio
    preguntas_superan_promedio = mayor_promedio(puntajes)
    
    # c) Mostrar resultados
    print("\n" + "="*45)
    mostrar_arreglo(preguntas, puntajes)
    
    print("\n" + "="*45)
    print(f"\nPregunta con el puntaje mínimo: {preguntas[indice_minimo]} ({puntajes[indice_minimo]} puntos)")
    
    print("\n" + "="*45)
    print("Preguntas que superan el promedio:")
    for p in preguntas_superan_promedio:
        print(f"-> {p}")
else:
    print("\nNo se ingresaron datos.")
print("" + "="*45)
print("\nFin del programa...")
print("" + "="*45)