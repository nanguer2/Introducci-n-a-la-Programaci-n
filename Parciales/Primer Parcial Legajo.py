# Autor: Nancy Guerrero
# Ejercicio: Primer Parcial
# Fecha: 13/10/2025
"""Se pide crear un código en Python para el siguiente problema, se ingresan los siguientes datos de los alumnos de un terciario:
Legajo, nombre y apellido, cantidad de materias cursadas, cantidad de materias aprobadas.
Validar los datos de entrada, el legajo, cantidad de materias cursadas y la cantidad de materias aprobadas.
La carga termina cuando en legajo se ingresa cero.
Se necesita calcular y mostrar:
a) el nombre y apellido del alumno con mayor cantidad de materias aprobadas.
b) El porcentaje por alumno de materias desaprobadas.
c) El porcentaje de materias aprobadas de todos los alumnos ingresados.
d) La cantidad de alumnos que aprobaron todas las materias que cursaron.
e) El legajo del alumno cuya cantidad de materias cursadas sea la minima."""
materias_cursadas = 0
materias_aprobadas = 0
contador_todas_aprobadas = 0
contador_alumnos = 0
total_cursadas = 0
total_aprobadas = 0
legajo_min_materias = 0
nombre_max_aprobadas = ""

legajo = int(input("Ingrese el numero de legajo (0 para salir):\t"))
while legajo != 0:
    while legajo < 0:
        legajo = int(input("Error. Ingrese el numero de legajo (0 para salir):\t"))
    
    nombre_apellido = input("Ingrese el nombre del alumno:\t").upper()
    while nombre_apellido == " ":
        nombre_apellido = input("Error. Ingrese el nombre del alumno:\t").upper()

    materias_cursadas = int(input("Ingrese la cantidad de materias cursadas:\t"))  
    while materias_cursadas <= 0:   
        materias_cursadas = int(input("Error. Ingrese la cantidad de materias cursadas:\t"))   

    materias_aprobadas = int(input("Ingrese la cantidad de materias aprobadas:\t"))  
    while materias_aprobadas < 0:   
        materias_aprobadas = int(input("Error. Ingrese la cantidad de materias aprobadas:\t"))

    if contador_alumnos == 0:
        max_aprobadas = materias_aprobadas
        min_materias = materias_cursadas
        legajo_min_materias = legajo
        nombre_max_aprobadas = nombre_apellido
    
    if materias_aprobadas > max_aprobadas:
        max_aprobadas = materias_aprobadas
        nombre_max_aprobadas = nombre_apellido

    if materias_cursadas < min_materias:
        min_materias = materias_cursadas
        legajo_min_materias = legajo
    
    # Contar alumnos que aprobaron todas las materias
    if materias_aprobadas == materias_cursadas:
        contador_todas_aprobadas += 1
    
    # Mostrar porcentaje de materias desaprobadas por alumno
    if materias_cursadas > 0 and total_cursadas > 0: 
        desaprobadas = materias_cursadas - materias_aprobadas
        porcentaje_desaprobadas = (desaprobadas / materias_cursadas) * 100
        print(f"Porcentaje de materias desaprobadas de {nombre_apellido}: {porcentaje_desaprobadas: .2f}%")
    
    # Acumular totales para calculos finales
    total_cursadas += materias_cursadas
    total_aprobadas += materias_aprobadas
    contador_alumnos += 1
    legajo = int(input("\nIngrese el numero de legajo (0 para salir):\t"))    

print("\nFinalizo el programa...\n")   
if total_cursadas > 0:
    porcentaje_aprobadas_total = (total_aprobadas / total_cursadas) * 100
    
    print("---------Resultados------------\n")   # Mostrar resultados finales
    print("Alumno con mayor cantidad de materias aprobadas: ", nombre_max_aprobadas)
    print(f"Porcentaje de materias aprobadas de todos los alumnos: {porcentaje_aprobadas_total: .2f}%")
    if contador_todas_aprobadas > 0:
        print("Cantidad de alumnos que aprobaron todas las materias: ", contador_todas_aprobadas)
    else:
        print("No hubo alumnos que aprobaran todas las materias.")    
    print("Legajo del alumno con menor cantidad de materias cursadas: ", legajo_min_materias)
else:
    print("No se ingresaron alumnos.")