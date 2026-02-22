"""Pregunta 2 45 puntos
Ingresar 6 números enteros y cargar un arreglo con un número positivo y otro negativo en ese orden.
Si no hubiese números negativos o positivos , poner ceros en esas posiciones.
Ejemplo: Se ingresan 1 -3 2 3 -4 10
El arreglo queda 1 -3 2 -4 3 0"""

#FUNCIONES
def ingresar_numeros(arre_num):
    i = 0
    while i < 6:
        num = int(input(f"Ingrese el número {i + 1}/6: "))
        i += 1
        arre_num.append(num)
    return arre_num


def construir_arreglo(arre_num):
    # 1. Almacenar POSICIONES de positivos y negativos en el arreglo de entrada
    # ESTAS LISTAS SON LOCALES y contienen ÍNDICES, no los valores completos
    indices_pos = [] # Cambio sugerido: Arreglo LOCAL de índices positivos
    indices_neg = [] # Cambio sugerido: Arreglo LOCAL de índices negativos
    
    for i in range(len(arre_num)):
        if arre_num[i] > 0:
            indices_pos.append(i)
        elif arre_num[i] < 0:
            indices_neg.append(i)
            
    # 2. Construir el arreglo final (tamaño 6)
    arreglo_final = [] 
    
    # Contadores para saber qué índice tomar de las listas de POSICIONES
    cp = 0 # Contador para índices positivos
    cn = 0 # Contador para índices negativos
    
    i = 0
    while i < 6:
        # Posiciones pares (0, 2, 4) -> Necesitan un Positivo
        if i % 2 == 0:
            if cp < len(indices_pos):
                # Tomar el VALOR del arreglo original (arre_num) usando el índice disponible
                valor = arre_num[indices_pos[cp]]
                arreglo_final.append(valor)
                cp += 1
            else:
                # Si no hay positivos disponibles, poner cero
                arreglo_final.append(0)
        
        # Posiciones impares (1, 3, 5) -> Necesitan un Negativo
        else: # i % 2 != 0
            if cn < len(indices_neg):
                # Tomar el VALOR del arreglo original (arre_num) usando el índice disponible
                valor = arre_num[indices_neg[cn]]
                arreglo_final.append(valor)
                cn += 1
            else:
                # Si no hay negativos disponibles, poner cero
                arreglo_final.append(0)
        i += 1 
    return arreglo_final


# PROGRAMA PRINCIPAL
arreglo_entrada = [] # Usado para ingresar los 6 números
arreglo_final = []
print("\n--- Carga Alternada (P, N, P, N, P, N) ---\n")
print("A continuación, ingrese 6 números enteros...\n")

# 1. Ingresar los 6 números. La función modifica arreglo_entrada.
ingresar_numeros(arreglo_entrada)

arreglo_resultante = construir_arreglo(arreglo_entrada)

print("\n---------------- RESULTADO ----------------\n")
print("Números ingresados:\n")
print(arreglo_entrada)

if len(arreglo_resultante) > 0:
    print("\nEl Arreglo Final (P, N, P, N, P, N) es:\n")
    print(arreglo_resultante)
else:
    print("No se ingresaron valores")
    
print("\n--------------------------------------------")
print("\nFin del programa...")
print("\n--------------------------------------------\n")