"""Crear dos arreglos A y B(partidos /jugadores )
se cargan valores hasta que un jugador se ingrese FIN
-Mostrar el nombre el nombre del jugador que jugo mas partidos y la cantidad de partidos jugados 
-Insertar despues de cada cantidad de partidos impares un 999 e insertado en jugadores
-Eliminar jugadores con partidos multiplo de 7"""
# FUNCIONES
def cargar_jugadores(arr_jugadores, arr_partidos): #Carga los nombres de los jugadores y la cantidad de partidos jugados.
    nombre = input("Ingrese el jugador (FIN para terminar): ").upper()
    while nombre != "FIN":
        while nombre == "":
            nombre = input("Error - Ingrese el jugador (FIN para terminar): ")
        partidos = int(input("Cantidad de partidos jugados: "))
        while partidos < 0:
            partidos = int(input("Error - Cantidad de partidos jugados: "))
                
        arr_jugadores.append(nombre)
        arr_partidos.append(partidos)
        nombre = input("Ingrese el jugador (FIN para terminar): ").upper()

def mostrar_tabla(arr_jugadores, arr_partidos):
    #Muestra los datos de los arreglos en formato de tabla.
    titulo = "Jugador"
    titulo1= "Partidos Jugados"
    print(f"\n{titulo:<10}{titulo1:>12}")
    print("--------------------------")
    for i in range(len(arr_jugadores)):
        print(f"{arr_jugadores[i]:<10}{arr_partidos[i]:>12}")

# 1. Mostrar el nombre del jugador que jugó más partidos y la cantidad de partidos jugados
def buscar_maximo(arr_partidos):
    pos_max = 0
    for i in range(1, len(arr_partidos)):
        if arr_partidos[i] > arr_partidos[pos_max]:
            pos_max = i
    return pos_max

# 2. Insertar desp de cada cant de partidos impares un 999 e insertado en jugadores
def insertar_despues_impar(arr_jugadores, arr_partidos):
    #Inserta el valor 999 en ambos arreglos después de cada cantidad impar de partidos."""
    i = 0
    while i < len(arr_partidos):
        # NOTA: arr_partidos[i] != 999 para evitar insertar infinitamente después de un 999 recién insertado
        if arr_partidos[i] % 2 != 0 and arr_partidos[i] != 999: 
            # Insertar en ambos arreglos en la posición i + 1
            arr_partidos.insert(i + 1, 999)
            arr_jugadores.insert(i + 1, "INSERCION")
            i += 2  # Salta la cantidad impar y el 999 que acabamos de insertar
        else:
            i += 1

# 3. Eliminar jugadores con partidos multiplo de 7
def eliminar_multiplo_7(arr_jugadores, arr_partidos):
    #Elimina elementos de ambos arreglos donde la cantidad de partidos es múltiplo de 7 (excepto el 0)."""
    i = 0
    while i < len(arr_partidos):
        # Excluímos el 0 ya que 0 % 7 es 0 (múltiplo), pero generalmente no se quiere eliminar un 0.
        if arr_partidos[i] != 0 and arr_partidos[i] % 7 == 0: 
            arr_jugadores.pop(i)
            arr_partidos.pop(i)
        else:
            i += 1

# ---------- PROGRAMA PRINCIPAL ----------
print("\n---------------------------------------\n") 
jugadores = []
partidos = []

# Carga de datos
cargar_jugadores(jugadores, partidos)

print("\n---------------------------------------") 
if len(partidos) > 0:
    # Mostrar tabla inicial
    print("\nDatos iniciales ingresados:")
    mostrar_tabla(jugadores, partidos)
    # 1. Jugador con más partidos
    index_max = buscar_maximo(partidos)
    if index_max != -1:
        print(f"\nJugador con más partidos: {jugadores[index_max]} ({partidos[index_max]}).")
    # 2. Inserción de 999 después de impares
    insertar_despues_impar(jugadores, partidos)
    print("\nInsertar '999' y 'INSERCION' (impares):")
    mostrar_tabla(jugadores, partidos)
    # 3. Eliminación de múltiplos de 7
    eliminar_multiplo_7(jugadores, partidos)
    print("\nEliminar partidos múltiplos de 7:")
    if len(partidos) > 0:
        mostrar_tabla(jugadores, partidos)
    else:
        print("\nLa lista quedó vacía tras las eliminaciones.")
else:
    print("No se ingresaron datos de jugadores.\n")
     
print("\nFin del programa.\n")