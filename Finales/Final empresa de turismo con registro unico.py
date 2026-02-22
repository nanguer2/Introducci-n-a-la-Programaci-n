"""Se quiere generar un programa para llevar estadisticas de reservas de viajes, de una empresa de turismo para la próxima temporada de verano, 
Para ello se debe poder trabajar las siguientes acciones a partir de un memú de opciones. El sistema debe cargar:
registrar ventas: Nro. de reserva, Tipo (Estadia, Viaje, Paquete), Precio Total, Adicionales (Texto libre, en caso que el comprador no quiera adicionales, se debe registra Sin Adicionales)
1)El número de reserva debe estar entre 1 y 1000 y debe ser único. No se debe repetir el codigo de reserva.
2)Validar los datos de entrada con criterio lógico.
3)Mostrar los datos de todas las reservas cargadas,
4)Promedio: Calcular el promedio (Precio) de las reservas cargadas que no contengan adicionales
5)Porcentaje: Calcular el porcentaje de cada tipo de reserva realizada.
6)Agregar al texto en Adicionales "VIP" , en las reservas que incluyan paquetes con un precio mayor a $1.500.000 (Ejemplo, si dice en el adicional "Habitacion para fumadores" queda "VIP - Habitación para fumadores".
7)Máximo: Calcular la mayor reserva y mostrar sus datos.
8)Elimimar todos los registros que sean Viaje y mostrar los arreglos resultantes.

CONSIDERACDONES ADICIONALES!
Salvo el monto facturado, todo los demas cálculos deben ser sobre los arreglos cargados.
No calcular minimo o maximo ordenando los arreglos.
Las funciones de calcular y buscar deben retornar los valores. Puede desarrollar funciones que muestren información, pero estas deberan recibir los datos a mostrar por parametro o llamando a otras funciones."""

#FUNCIONES
def seleccionar_opcion():
    print("\nMenu de opciones:\n")
    print("1. Registrar nueva reserva")
    print("2. Mostrar")
    print("3. Estadisticas")
    print("4. Salir")
    opcion = int(input("\nIngrese una opcion (1-4): "))
    while opcion < 1 or opcion > 4:
        opcion = int(input("Error - Ingrese una opcion (1-4): "))
    return opcion
    
def ingresar_nroreserva():    
    nroreserva = int(input("Ingrese el número de reserva: "))             
    while (nroreserva < 1 or nroreserva > 1000):
        nroreserva = int(input("Error - Ingrese el numero de reserva: "))
    return nroreserva

def ingresar_tipo():    
    tipo = input("Ingrese el tipo (Estadia (E), Viaje (V) o Paquete(P)): ").upper()
    while tipo != "E" and tipo != "V" and tipo != "P":
        tipo = input("Error - Ingrese el tipo (Estadia (E), Viaje (V) o Paquete(P)): ").upper()
    return tipo
    
def ingresar_precio():    
    precio = int(input("Ingrese el precio del viaje: "))
    while precio <= 0:
        precio = int(input("Error - Ingrese el precio del viaje: "))
    return precio

def ingresar_adicional():    
    adicional = input("Ingrese si tiene adicional: ").upper()        
    while adicional == "":
        adicional = "Sin Adicionales"
    return adicional   

def buscar_nroreserva(arr_nroreserva, nroreserva):
    i = 0 # Retorna la posición si lo encuentra, o el largo del arreglo si no existe
    while i < len(arr_nroreserva) and nroreserva != arr_nroreserva[i]:
        i += 1
    return i

def registrar_reservas(arr_nroreserva,arr_tipo,arr_precio,arr_adicional): # No se debe repetir el codigo de reserva.
    nroreserva = ingresar_nroreserva()
    while buscar_nroreserva(arr_nroreserva, nroreserva) < len(arr_nroreserva):
        print("Error - El número de reserva ya existe.")
        nroreserva = ingresar_nroreserva()
    tipo = ingresar_tipo()
    precio = ingresar_precio()
    adicional = ingresar_adicional()
    
    arr_nroreserva.append(nroreserva)
    arr_tipo.append(tipo)
    arr_precio.append(precio)
    arr_adicional.append(adicional)
    
def agregar_vip(arr_precio,arr_adicional):
    #6.- Agregar al texto en Adicionales "VIP" , en las reservas que incluyan paquetes con un precio mayor a $1.500.000
    # (Ejemplo, si dice en el adicional "Habitacion para fumadores" queda "VIP - Habitación para fumadores".
    for i in range(len(arr_precio)):
        if arr_precio[i] > 1500000 and "VIP" not in arr_adicional[i]:
            arr_adicional[i] = "VIP - " + arr_adicional[i]
            
def mostrar_reservas(arr_nroreserva,arr_tipo,arr_precio,arr_adicional):
    titulo = "Nro."
    titulo2 = "Tipo"
    titulo3 = "Precio"
    titulo4 = "Adicionales"
    print(f"{titulo:<10}{titulo2:<10}{titulo3:<15}{titulo4:<20}")
    print("-----------------------------------------------")
    for i in range(len(arr_nroreserva)):
        print(f"{arr_nroreserva[i]:<10}{arr_tipo[i]:<10}{arr_precio[i]:<15}{arr_adicional[i]:<20}")
    print("-----------------------------------------------\n")    

def calcular_promedio_sin_adicionales(arr_precio,arr_adicional):
    cont_precios = 0
    acum_precios = 0
    prom = -1 # Valor por defecto en caso de no haber reservas sin adicionales
    for i in range(len(arr_precio)):
        if arr_adicional[i] == "Sin Adicionales":
            acum_precios += arr_precio[i]
            cont_precios += 1
    if cont_precios != 0:
        prom = acum_precios / cont_precios  
    return prom        

def calcular_porcentaje_tipo(arr_tipo):
    contador_estadia = 0
    contador_viaje = 0
    contador_paquete = 0
    contador_total = 0

    for i in range(len(arr_tipo)):
        if arr_tipo[i] == "E":
            contador_estadia += 1
        if arr_tipo[i] == "V":
            contador_viaje += 1
        if arr_tipo[i] == "P":
            contador_paquete += 1
        contador_total += 1

    if contador_total != 0:
        porc_estadia = (contador_estadia / contador_total) * 100 
        porc_viaje = (contador_viaje / contador_total) * 100
        porc_paquete = (contador_paquete / contador_total) * 100

    else:
        print("No hay reservas para calcular porcentajes.")
        
    print(f"Estadia: {porc_estadia:.2f}%")
    print(f"Viaje: {porc_viaje:.2f}%")
    print(f"Paquete: {porc_paquete:.2f}%")    
                    
def maximo_reserva(arr_precio):
    max_precio = arr_precio[0]
    pos_max = 0
    for i in range(1, len(arr_precio)):
        if arr_precio[i] > max_precio:
            max_precio = arr_precio[i]
            pos_max = i
    return pos_max

def eliminar_viajes(arr_nroreserva,arr_tipo,arr_precio,arr_adicional):
    i = 0
    while i < len(arr_tipo):
        if arr_tipo[i] == "V":
            arr_nroreserva.pop(i)
            arr_tipo.pop(i)
            arr_precio.pop(i)
            arr_adicional.pop(i)
        else:
            i += 1

def ver_estadisticas(arr_nroreserva,arr_tipo,arr_precio,arr_adicional):

    if len(arr_nroreserva) > 0:
    #1)Promedio: Calcular el promedio (Precio) de las reservas cargadas que no contengan adicionales
        print("1. Promedio sin adicionales:\n")
        promedio = calcular_promedio_sin_adicionales(arr_precio,arr_adicional)
        if promedio != -1:
            print(f"Promedio de reservas: $ {promedio:.2f}\n")
        else:
            print("No hay reservas sin adicionales para calcular el promedio.\n")
    #2)Porcentaje: Calcular el porcentaje de cada tipo de reserva realizada.
        print("2. Porcentaje por tipo:\n")
        calcular_porcentaje_tipo(arr_tipo)
    #3)Agregar al texto en Adicionales "VIP" , en las reservas que incluyan paquetes con un precio mayor a $1.500.000
        print("\n3. Agregar VIP en adicionales:")
        agregar_vip(arr_precio,arr_adicional)
        print("\nActualización VIP realizada (si corresponde).\n")
        mostrar_reservas(arr_nroreserva,arr_tipo,arr_precio,arr_adicional)
    #4)Máximo: Calcular la mayor reserva y mostrar sus datos.
        print("4. Mayor reserva:")
        index_max = maximo_reserva(arr_precio)
        print(f"\nLa mayor reserva es: {arr_nroreserva[index_max]}, Tipo: {arr_tipo[index_max]}, Precio: ${arr_precio[index_max]}\n")
    #5)Elimimar todos los registros que sean Viaje y mostrar los arreglos resultantes."""
        print("5. Eliminar reservas de tipo Viaje:\n")
        eliminar_viajes(arr_nroreserva,arr_tipo,arr_precio,arr_adicional)
        print("Lista de reservas después de eliminar.\n")
        mostrar_reservas(arr_nroreserva,arr_tipo,arr_precio,arr_adicional)
    else:
        print("No hay reservas registradas.\n")
           
#PROGRAMA PPAL
nroreservas = []
tipos = []
precios = []
adicionales = []

seleccion = seleccionar_opcion()
while seleccion != 4: # Salir es == 4
    
    if seleccion == 1:
        print("\n--- Registrar reserva ---\n")
        registrar_reservas(nroreservas,tipos,precios,adicionales)
        print("\nReserva registrada con éxito.")
    if seleccion == 2:
        print("\n--- Mostrar reservas ---\n")
        mostrar_reservas(nroreservas,tipos,precios,adicionales)
        print("Fin lista de reservas registradas.")
    if seleccion == 3:
        print("\n--- Ver estadisticas ---\n")
        ver_estadisticas(nroreservas,tipos,precios,adicionales)
        print("Fin de las estadísticas.")
    seleccion = seleccionar_opcion()
print("\nSaliendo del programa...")
print("\nFin del programa.\n")