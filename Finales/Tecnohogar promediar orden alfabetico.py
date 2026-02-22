""" Lucía Fernández ha tomado recientemente el liderazgo de la firma familiar TecnoHogar Sur S.R.L., la cual ha operado
durante años con procedimientos manuales. Con el objetivo de optimizar la gestión interna, Lucía ha decidido implementar 
un sistema informatizado requisitos del programa:
# Ingreso y almacenamiento de datos en vectores: Nombre del modelo del producto (en formato textual). Precio unitario (debe ser mayor a cero).
# Validaciones especiales:
    . Si el nombre del modelo se ingresa en minúsculas, debe convertirse automaticamente a mayusculas.
    . Si no se ingresan datos, el programa debe emitir un mensaje de aviso.
# Condición de corte: La carga de productos se interrumpe al ingresar "FIN" como nombre del modelo.
# Procesamiento y visualización:
    A) Mostrar todos los productos y sus precios en formato de tabla, utilizando una función.
    B) Identificar y mostrar el nombre del producto con el precio más bajo.
    C) Calcular el precio promedio de todos los productos.
    D) Eliminar los productos cuyo precio supere el promedio, junto con sus respectivos valores.
    E) Insertar el modelo "PRUEBA" con un precio de 999 inmediatamente después de cada precio impar.
    F) Ordenar los productos alfabéticamente por nombre, asegurando que los precios acompanen el orden.
# Importante:
    . Cada vez que se modifiquen los vectores, se debe mostrar el resultado actualizado con la función creada para mostrar."""

# DEFINICIONES DE FUNCIONES
def validar_nombre():
    nombre_prod = input("\nIngrese el nombre (FIN para terminar): ").upper()
    while nombre_prod == "":
        nombre_prod = input("Error - Ingrese el nombre (FIN para terminar):").upper()
    return nombre_prod


def validar_precio():
    precio_prod = int(input("Ingrese el valor del producto: "))
    while precio_prod <= 0:
        precio_prod = int(input("Error - Ingrese el valor del producto: "))
    return precio_prod


def cargar_datos(vec_nombres, vec_precios):
    nombre = validar_nombre()
    while nombre != 'FIN':
        precio = validar_precio()
        vec_nombres.append(nombre)
        vec_precios.append(precio)
        nombre = validar_nombre()# acordarse de volver a leer la variable que maneja el ciclo
    print("\nLa carga de datos ha sido finalizada...")
        

def mostrar_datos(vec_nombres, vec_precios):
    titulo1 = "Producto"
    titulo2 = "Precio"
    print(f"{titulo1:<15}{titulo2:>10}")
    print("-----------------------------------------")
    for i in range(len(vec_nombres)):
        print(f"{vec_nombres[i]:<15}{vec_precios[i]:>10}")
    print("-----------------------------------------\n")


def buscar_minimo(vec):
    pos = 0
    for i in range(1, len(vec)): #Empieza en 1 para no compararse consigo mismo.
        if vec[pos] > vec[i]:
            pos = i
    return pos


def promediar(vec):
    acum = 0
    cont = 0
    for i in range(len(vec)):
        acum += vec[i]
        cont += 1
    if cont >0:
        promedio_prec = acum / cont
    return promedio_prec


def eliminar_datos(vec, vec1):
    promedio = promediar(vec1)
    i = 0
    while i < len(vec1):
        if promedio < vec1[i]:
            vec.pop(i)
            vec1.pop(i)
        else:
            i += 1


def insertar(vec, vec1):
    i = 0
    while i < len(vec):
        if vec1[i] % 2 != 0:
            vec.insert(i + 1, "PRUEBA")
            vec1.insert(i + 1, 999)
            i += 2
        else:
            i += 1


def ordenar(vec, vec1):
    for i in range(len(vec) - 1):
        for j in range(i + 1, len(vec)):
            if vec[i] > vec[j]:
                intercambiar(vec, i, j)
                intercambiar(vec1, i, j)


def intercambiar(arreglo, i, j):
    aux = arreglo[i]
    arreglo[i] = arreglo[j]
    arreglo[j] = aux
    
    
# PROGRAMA PPAL
nombres = []
precios = []
print("-----------------------------------------")
cargar_datos(nombres,precios)
print("\n-----------------------------------------")

if len(nombres) == 0:
    print("No se registraron datos!")
    print("-----------------------------------------\n")
else:
    print("\nA) Mostrar todos los productos.\n")
    mostrar_datos(nombres,precios)
    
    print("B) Producto con el precio más bajo.")
    pos_minimo = buscar_minimo(precios)
    print(f"\nEl producto más barato es: {nombres[pos_minimo]} con ${precios[pos_minimo]}")
    print("-----------------------------------------\n")
    
    print("C) Calcular el promedio de los productos.")
    if len(precios) >0:
        print(f"\nEl promedio es de ${promediar(precios):.2f}")
    else:
        print("No hay datos para calcular.")
    print("-----------------------------------------\n")
    print("D) Eliminar los superiores al promedio.")
    eliminar_datos(nombres,precios)
    print("\n\tDespues de la eliminacion\n")
    mostrar_datos(nombres,precios)
    
    print("E) Insertar después de cada impar:")
    print("Modelo:'PRUEBA' y Precio: 999.\n")
    insertar(nombres,precios)
    mostrar_datos(nombres,precios)
    
    print("F) Ordenar los productos alfabéticamente.")
    ordenar(nombres,precios)
    print("Despues de ordenar por nombre:\n")
    mostrar_datos(nombres,precios)
    
    print("Fin del programa...\n")