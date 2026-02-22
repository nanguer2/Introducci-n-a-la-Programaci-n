"""Pregunta 1 55 puntos
Alimentos para mascotas y le solicitan un programa informatico para registro de ventas. Este registro se realiza al finalizar el día.
1- Se cargan facturas HASTA QUE el número de factura sea 0. (EL NUMERO DE FACTURA NO PUEDE SER NEGATIVO). 
Y una vez cargado el número de la factura se carga el importe. (Dos arreglos)
2- Se muestran los numeros de facturas con sus importes
3- Se calcula el importe máximo facturado y a que factura pertenece. (Resolver con una función).
4- Calcular el promedio de los importes (Con una función), a partir del resultado obtenido reemplazar los numeros de facturas y 
los importes por el valor 9999 para todos aquellos que sean inferiores al promedio.
5- A partir del promedio de los importes, insertar después de cada valor superior al promedio, un -2 en ambos vectores
6- Se eliminan los numeros de facturas impares y los valores asociados a ellas
NOTA: SE DEBE MOSTRAR EL RESULTADO DE LO SOLICITADO"""

# 1. Se cargan facturas HASTA QUE el número de factura sea 0.
def validar_factura():
    factura_ing = int(input("Ingrese el número de factura (0 para terminar): "))
    while factura_ing < 0:
        factura_ing = int(input("Error - Ingrese un número de factura positivo (o 0 para terminar): "))
    return factura_ing    


def validar_importe():
    importe_ing = float(input("Ingrese el importe de la factura: ")) 
    while importe_ing <= 0: 
        importe_ing = float(input("Error - Ingrese el importe de la factura (debe ser positivo): "))
    return importe_ing
        
        
def cargar_datos(arr_facturas, arr_importes):
    factura = validar_factura()
    while factura != 0:
        importe = validar_importe()   
            
        arr_facturas.append(factura)
        arr_importes.append(importe)
        
        print(f">> Factura {factura} cargada con éxito.\n")
        factura = validar_factura()
    print("\nLa carga se ha finalizado.")
    
# 2. Se muestran los numeros de facturas con sus importes
def mostrar_facturas(arr_facturas, arr_importes):
    titulo = "FACTURAS"
    print(f"\n           {titulo}           ")
    print(f"{'Factura Nº':<15}{'Importe':>15}")
    print("------------------------------")
    for i in range(len(arr_facturas)):
        print(f"{arr_facturas[i]:<15}{arr_importes[i]:>15.2f}")
    print("------------------------------")

# 3. Se calcula el importe máximo facturado y a que factura pertenece.
def calcular_maximo(arr_importes):
    pos_max = 0
    for i in range(len(arr_importes)):
        if arr_importes[i] > arr_importes[pos_max]:
            pos_max = i
    return  pos_max

# 4. Calcular el promedio e, a partir de este, reemplazar valores inferiores por 9999
def calcular_promedio(arr_importes):
    acum = 0
    cont = 0
    for i in range(len(arr_importes)):
        acum += arr_importes[i]
        cont += 1
    if cont > 0:
        promedio = acum / cont
    return promedio

def reemplazar_inferiores(arr_facturas, arr_importes, promedio):
    print(f"\nReemplazo (Importes < {promedio:.2f} por 9999)")
    for i in range(len(arr_importes)):
        if arr_importes[i] < promedio:
            arr_facturas[i] = 9999  # Reemplazar
            arr_importes[i] = 9999  # Reemplazar

# 5. Insertar -2 después de cada valor superior al promedio
def insertar_superior(arr_facturas, arr_importes, promedio):
    print(f"\nInserción (-2 después de importes > {promedio:.2f})")
    i = 0
    while i < len(arr_importes):
        if arr_importes[i] > promedio:
            arr_facturas.insert(i + 1, -2)
            arr_importes.insert(i + 1, -2)
            i += 2  
        else:
            i += 1  
            
# 6. Eliminar los números de facturas impares y los valores asociados
def eliminar_impares(arr_facturas, arr_importes):
    i = 0
    while i < len(arr_facturas):
        # Verifica si el número de factura es impar
        if arr_facturas[i] % 2 != 0:
            print(f"\nEliminando factura Nº {arr_facturas[i]} con importe {arr_importes[i]:.2f}")
            arr_facturas.pop(i)
            arr_importes.pop(i)
            # NO se incrementa 'i' porque el siguiente elemento se mueve a la posición 'i'
        else:
            i += 1  # Solo avanza si el elemento no fue eliminado

# --- PROGRAMA PRINCIPAL---
facturas = []
importes = []
print("\n---------------------------------------\n")
# 1. Se cargan facturas HASTA QUE el número de factura sea 0.
print("1. Cargar facturas:\n")
cargar_datos(facturas, importes)
print("\n---------------------------------------")

if len(facturas) >0:
    # 2. Mostrar los numeros de facturas con sus importes.
    print("\n2. Mostrar datos:")
    mostrar_facturas(facturas, importes)
    
    # 3. Se calcula el importe máximo facturado y a que factura pertenece.
    print("\n3. Calcular el máximo:")
    max_importe= calcular_maximo(importes)
    print(f"\nEl importe máximo facturado es: {importes[max_importe]:.2f}")
    print(f"pertenece a la factura Nº: {facturas[max_importe]}")
    print("\n---------------------------------------\n")
    
    # 4.Calcular el promedio y reemplazar por el valor 9999 para todos aquellos que sean inferiores al promedio.
    print("4. Reemplazar por 9999 valores inferiores al promedio:")
    if len(facturas)>0:
        promedio_val = calcular_promedio(importes)
        print(f"\nPromedio: {promedio_val:.2f}")
        reemplazar_inferiores(facturas, importes, promedio_val)
        mostrar_facturas(facturas, importes)
    else:
        ("No se puede calcular el promedio.")
    
    # 5. Insertar después de cada valor superior al promedio, un -2 en ambos vectores.
    print("\n5. Insertar después de cada valor superior al promedio:")
    insertar_superior(facturas, importes, promedio_val)
    mostrar_facturas(facturas, importes)
    
    # 6. Eliminar los numeros de facturas impares y los valores asociados a ellas.
    print("\n6. Eliminar los numeros de facturas impares:")
    eliminar_impares(facturas, importes)
    if len(facturas) == 0:
        print("\n*No hay facturas parar mostrar*")
    else:
        mostrar_facturas(facturas, importes)
    
else:
    print("\nNo se ingresaron datos.")
print("\nFin del programa.")
print("\n---------------------------------------\n")
    