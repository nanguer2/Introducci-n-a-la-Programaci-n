"""
Se quiere generar un sistema de software que permita registrar las capacidades de supervivencia para un reality show en la selva amazónica. 
Para lo cual, a partir del uso de un menú, se podrán realizar las siguientes acciones del sistema:
1) Opción 1: Carga de datos. Se registra la siguiente información (utilizando arreglos paralelos):
- Nombre del competidor
- Edad
- Días de supervivencia
Consideraciones:
- El nombre de competidor debe ser único. En caso de que un nombre ya esté registrado previamente, se deberá mostrar un mensaje de error al momento de la carga y no procesar el resto
de la información.
- No se debe poder registrar a menores de edad (edad menor a 18). En caso de que algún competidor sea menor, no deberá registrarse, mostrar un mensaje y no procesar el resto de la
Información asociada.
- Se deben validar los datos de entrada con criterio lógico.
- Al momento del registro de un competidor. Se considera que, si supera los 45 días de supervivencia, su categoría será EXTREMA, en caso contrario, SOBREVIVIENTE. Este dato debe ser registrado en un arreglo.
2) Opción 2: Mostrar la información cargada.
3) Opción 3: Record. Calcular el máximo de días de supervivencia entre todos los competidores.
4) Opción 4: Modificar record. Crear una función que, a partir del máximo calculado previamente, identifique si el competidor supera los 40 días de supervivencia y su edad es mayor a 50; modificar
su categoría por "EXTREMO SR."
5) Opción 5: Promedio. Determinar el promedio de edad de todos los competidores.
6) Opción 6: Eliminar. Eliminar aquellos competidores cuyos días de supervivencia sean menores a la mitad del máximo calculado.
CONSIDERACIONES ADICIONALES:
- Todos los puntos requeridos, salvo el primero, deben ser realizados con los arreglos cargados.
- Cada punto debe ser resuelto al menos con una función.
"""

# --- FUNCIONES
def seleccionar_opcion():
    print("\n--- MENÚ DE OPCIONES ---\n")
    print("1. Cargar competidor")
    print("2. Mostrar información")
    print("3. Ver Record (Máximo)")
    print("4. Modificar Categoría (Extremo SR.)")
    print("5. Promedio de Edad")
    print("6. Eliminar competidores débiles")
    print("7. Salir")
    
    op = int(input("\nSeleccione una opción: "))
    while op < 1 or op > 7:
        op = int(input("Error. Seleccione entre 1 y 7: "))
    return op


def buscar_nombre(arr_nombre, nombre_buscado):
    for i in range(len(arr_nombre)):
        if arr_nombre[i] == nombre_buscado:
            return i # Retorna la posición si lo encuentra
    return -1 # Retorna -1 si no existe


def validar_nombre():
    var_nombre = input("\nIngrese el nombre: ")
    while var_nombre == "":
        var_nombre = input("Error - Ingrese el nombre: ")
    return var_nombre


def validar_edad():
    var_edad = int(input("\nIngrese la edad: "))
    while var_edad < 18:
        var_edad = int(input("Error - Ingrese la edad (Mayores a 18): "))
    return var_edad


def validar_dias():
    var_dias = int(input("\nIngrese Nro. de días de supervivencia: "))
    while var_dias <= 0:
        var_dias = int(input("Error - Nro. de días de supervivencia: "))
    return var_dias

# Cargar los datos.
def cargar_datos(arr_edad, arr_nombre, arr_dias, arr_categoria):
    categoria = ""
    edad = validar_edad()
    nombre = validar_nombre()
    if buscar_nombre(arr_nombre, nombre) != -1:
        print("ERROR: El nombre ya está registrado. Carga cancelada.")
        nombre = validar_nombre()
    dia = validar_dias()
    # 4. Determinar Categoría    
      
    if dia > 45:
        categoria = "EXTREMA"
    else:
        categoria = "SOBREVIVIENTE"

    arr_edad.append(edad)
    arr_nombre.append(nombre)
    arr_dias.append(dia)
    arr_categoria.append(categoria)
    
# Mostrar los datos.
def mostrar_datos(arr_edad, arr_nombre, arr_dias, arr_categoria):
    titulo1 = "Nombre"
    titulo2 = "Edad"
    titulo3 = "Días"
    titulo4 = "Categoria"
    print(f"{titulo1:<10}{titulo2:<7}{titulo3:<10}{titulo4:<15}")
    print("-"*40)
    for i in range (len(arr_edad)):
        print(f"{arr_nombre[i]:<10}{arr_edad[i]:<7}{arr_dias[i]:<10}{arr_categoria[i]:<15}")
    print("-"*40)

#3: Record. Calcular el maxino de dias de supervivencia entre todos los competidores.
def maximo_supervivencia(arr_dias):
    pos_max = 0
    for i in range (1, len(arr_dias)):
        if arr_dias[i] > arr_dias[pos_max]:
            pos_max = i
    return pos_max

#4: Modificar record, supera los 40 dias de supervivencia y su edad es mayor a se, modificar su categoria por "EXTREMO SR."
def modificar_categoria(arr_edad, arr_categoria, arr_dias):
    cont = 0
    for i in range (len(arr_categoria)):
        if arr_edad[i] > 50 and arr_dias[i] > 40:
            arr_categoria[i] = "EXTREMO SR."
            cont += 1
    print(f"Se modificaron {cont} competidores.\n")
    
#5: Promedio de edad de todos los competidores.
def calcular_promedio(arr_edad):
    total_edades = 0
    cont = 0
    for i in range (len(arr_edad)):
        total_edades += arr_edad[i]
        cont += 1
    promedio = total_edades/cont
    return promedio

#6: Eliminar menores a la mitad del máximo calculado.
def eliminar_debiles(arr_edad, arr_nombre, arr_dia, arr_categoria):
    max = maximo_supervivencia(arr_dia)
    umbral = arr_dia[max]/2
    cont = 0
    i = 0
    while i < len(arr_dia):
        if arr_dia[i] < umbral:
            arr_edad.pop(i)
            arr_nombre.pop(i)
            arr_dia.pop(i)
            arr_categoria.pop(i)
        else:
            i += 1
        cont += 1    
    print(f"Se eliminaron {cont} competidores débiles.\n")        
        
# --- PROGRAMA PRINCIPAL ---
edades = []
nombres = []
supervivencia = []
categorias = []

seleccion = seleccionar_opcion()
while seleccion != 7: #(es == 7 salir)
    if seleccion == 1:
        print("\n1. Cargar datos:")
        cargar_datos(edades, nombres, supervivencia, categorias)
        print("\nRegistro exitoso.")
    if seleccion == 2:
        print("\n2. Mostrar datos:\n")
        mostrar_datos(edades, nombres, supervivencia, categorias)
    if seleccion == 3:
        print("\n3. Record de supervivencia:\n")
        if len(supervivencia) >0:
            index = maximo_supervivencia(supervivencia)
            print(f"El mayor superviviente es {nombres[index]} con {supervivencia[index]} dias.")
        else: 
            print("No hay suficientes datos.")
    if seleccion == 4:
        print("\n4. Mayor a 40 EXTREMO SR:\n")
        modificar_categoria(edades, categorias, supervivencia)
        mostrar_datos(edades, nombres, supervivencia, categorias)
    if seleccion == 5:
        print("\n5. Promedio de competidores:\n")
        if len(edades) >0:
            prom = calcular_promedio(edades)
            print(f"El promedio es: {prom:.2f} años.")      
        else: 
            print("No hay suficientes datos.")
    if seleccion == 6:
        print("\n6. Eliminar débiles:\n")
        eliminar_debiles(edades, nombres, supervivencia, categorias)
        mostrar_datos(edades, nombres, supervivencia, categorias)
    seleccion = seleccionar_opcion()
print("\nSaliendo del progrma... ")
print("Fin del progrma.\n")           