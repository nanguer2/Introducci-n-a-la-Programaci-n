"""Actividad Ejercicios de integracion de Python. Nancy Guerrero.
Este programa procesa los datos de 23 pacientes atendidos por un dentista en un día.
Se registran nombre, número de socio, horario y tratamiento realizado.
Se calcula el promedio de pacientes con ortodoncia, cantidad atendidos antes de las 16 hs,
porcentaje de pacientes por tipo de tratamiento,
y se identifica el socio con número más alto y el que se atiende más temprano."""

# Inicialización de contadores y variables para acumular datos y resultados
contador_ortodoncia = 0       # Contador específico para ortodoncia
contador_antes_16hs = 0       # Contador de pacientes atendidos antes de las 16 hs
contador_control = 0          # Contador de pacientes con tratamiento control
contador_caries = 0           # Contador de pacientes con arreglo de caries
contador_extraccion = 0       # Contador de pacientes con extracción
nombre_mayor_socio = ""       # Nombre del paciente con mayor número de socio
tratamiento_mayor_socio = ""  # Tratamiento del paciente con mayor número de socio
socio_mas_temprano = ""       # Nombre del paciente que se atiende más temprano
total_pacientes = 0           # Contador total de pacientes procesados

# Ciclo para ingresar datos de 23 pacientes.
for i in range(23):
    # Solicitar y convertir a mayúsculas el nombre del paciente.
    nombre = input(" \nIngrese el nombre del paciente: \t").upper()
    
    # Solicitar número de socio y validar que sea positivo
    numero_socio = int(input("Ingrese el número de socio del paciente: \t"))
    while numero_socio <= 0:
        numero_socio = int(input("Error. Ingrese el numero de socio (números mayores de cero): \t"))
    
    # Solicitar horario y validar que esté en rango 8 a 20
    horario = int(input("Ingrese el horario en un rango de 8 a 20hs: \t"))
    while horario <= 7 or horario >= 21:
        horario = int(input("Error. Ingrese el horario en un rango de 8 a 20hs: \t"))
    
    # Solicitar tipo de tratamiento y convertir a mayúsculas
    tratamiento = input("Ingrese el tipo de tratamiento: CONTROL (C), ARREGLO DE CARIES (A), ORTODONCIA (O), EXTRACCION (E): \t").upper()
    # Validar tratamiento
    while tratamiento != "C" and tratamiento != "A" and tratamiento != "O" and tratamiento != "E":
        print("Error. Tratamiento inválido. Debe ser C, A, O o E.")
        tratamiento = input("Ingrese el tipo de tratamiento válido: \t").upper()
    
    # Para el primer paciente (i==0), inicializar las variables de mayor socio y más temprano con sus valores
    if i == 0:
        mayor_numero_socio = numero_socio
        nombre_mayor_socio = nombre
        tratamiento_mayor_socio = tratamiento
        hora_mas_temprano = horario
        socio_mas_temprano = nombre
        numero_temprano = numero_socio
    
    # Actualizar el total de pacientes procesados (i empieza en 0, por eso se suma 1)
    total_pacientes = i + 1   
             
    # Contabilizar según el tipo de tratamiento ingresado
    if tratamiento == "O":
        contador_ortodoncia += 1
    
    elif tratamiento == "C":
        contador_control += 1
    
    elif tratamiento == "A":
        contador_caries += 1
    
    elif tratamiento == "E":
        contador_extraccion += 1     
    
    # Actualizar datos del paciente con mayor número de socio si corresponde
    if numero_socio > mayor_numero_socio:
        mayor_numero_socio = numero_socio
        nombre_mayor_socio = nombre
        tratamiento_mayor_socio = tratamiento        
    
    # Actualizar datos del paciente que se atiende más temprano si corresponde
    if horario < hora_mas_temprano:
        hora_mas_temprano = horario
        socio_mas_temprano = nombre
        numero_temprano = numero_socio
       
    # Contar pacientes atendidos antes de las 16 hs
    if horario < 16:
        contador_antes_16hs += 1
       
# Calcular porcentaje de pacientes por cada tipo de tratamiento, evitando división por cero
if total_pacientes > 0:
    porcentaje_control = (contador_control / total_pacientes) * 100
    porcentaje_caries = (contador_caries / total_pacientes) * 100
    porcentaje_ortodoncia = (contador_ortodoncia / total_pacientes) * 100
    porcentaje_extraccion = (contador_extraccion / total_pacientes) * 100
else:
    print("Error. División por cero.")
       
# Calcular promedio de ortodoncia solo si hay pacientes con ortodoncia
if contador_ortodoncia > 0:
    promedio_ortodoncia = contador_ortodoncia / total_pacientes
else:
    promedio_ortodoncia = 0 
        
# Mostrar resultados finales al usuario
print(" \nPromedio de pacientes que se realizan ortodoncia: \t", promedio_ortodoncia)
print("Cantidad de pacientes atendidos antes de las 16hs: \t", contador_antes_16hs)
print(" \nPorcentaje de pacientes por tratamiento: \n")
print("Control: \t", porcentaje_control, "%")
print("Arreglo de caries: \t", porcentaje_caries, "%")
print("Ortodoncia: \t", porcentaje_ortodoncia, "%")
print("Extracción: \t", porcentaje_extraccion, "%")
print(" \nPaciente con mayor número de socio: \t", nombre_mayor_socio, "Tratamiento:", tratamiento_mayor_socio)

print("Socio que se atiende más temprano: \t", socio_mas_temprano, "Número de socio: ", numero_temprano)
