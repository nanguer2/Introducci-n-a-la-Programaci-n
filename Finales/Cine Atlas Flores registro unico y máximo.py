"""El cine Atlas de Flores decide digitalizar el control de ventas de entradas para las películas infantiles que estarán en cartelera
durante las vacaciones de invierno. Para la venta de las entradas se pide al usuario que ingrese la siguiente información:
  Cantidad de entradas. (valor entero)
  Nombre de película. (cadena de caracteres)
a) Generar un arreglo con las peliculas guardando la cantidad de entradas vendidas en un arreglo paralelo.
b) La carga finaliza cuando en cantidad se ingresa un 0.
c) En una función calcular y retornar la pelicula que mas vendió.
d) PLUS: buscar si la pelicula ingresada ya existe en el arreglo, y si es así, acumular la cantidad de entradas para esa pelicula."""

#--- FUNCIONES ---
def cargar_datos(arre_pel, arre_cant):
    cantidad = int(input("\nIngrese la cantidad de entradas (0 para finalizar): "))
    while cantidad != 0:
        # Validación de cantidad: solo aceptamos positivos
        while cantidad < 0:
            print("Error - La cantidad no puede ser negativa.")
            cantidad = int(input("Ingrese la cantidad de entradas (0 para finalizar): "))
        
        # Si después de validar, la cantidad es 0, el while principal terminará
        if cantidad > 0:    
            pelicula = input("Ingrese el nombre de la pelicula: ").upper()
            while pelicula == "":
                pelicula = input("Error - Ingrese el nombre de la pelicula: ").upper()
            
            # Buscamos si ya existe
            posicion_encontrada = -1
            for i in range(len(arre_pel)):
                if arre_pel[i] == pelicula:
                    posicion_encontrada = i
            
            if posicion_encontrada >= 0:
                # Acumulamos
                arre_cant[posicion_encontrada] += cantidad
                print(f"Entradas acumuladas para: {pelicula}")
            else:
                # Agregamos nuevo
                arre_pel.append(pelicula)
                arre_cant.append(cantidad)
                print(f"Nueva película registrada: {pelicula}")

        # Pedir el siguiente dato
        cantidad = int(input("\nIngrese la cantidad de entradas (0 para finalizar): "))

def calcular_max(arre_cant):
    pos_max = 0
    for i in range(1, len(arre_cant)):
        # Solo comparamos, NO asignamos valores al arreglo
        if arre_cant[i] > arre_cant[pos_max]:
            pos_max = i
    return pos_max 

def mostrar_datos(arre_pel, arre_cant): 
    print(f"\n{'PELÍCULA':<20}{'CANTIDAD':<10}")
    print("-" * 25)
    for i in range(len(arre_pel)):
        print(f"{arre_pel[i]:<20}{arre_cant[i]:<10}")

#--- PROGRAMA PRINCIPAL ---

peliculas = []
cantidades = []

print("\nSISTEMA DE VENTAS - CINE ATLAS")
cargar_datos(peliculas, cantidades)

if len(peliculas) > 0:
    print("\n--- RESUMEN DE VENTAS ---")
    mostrar_datos(peliculas, cantidades)
    
    indice_max = calcular_max(cantidades) 
    print(f"\n--- Película más taquillera ---\n")
    print(f"{peliculas[indice_max]} con {cantidades[indice_max]} entradas.")
else:
    print("\nNo se registraron ventas.")

print("\nFin del programa.\n")