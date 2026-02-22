"""Desarrollar un programa donde se ingresa el nombre y apellido, el saldo de la caja de ahorro
y el saldo de la caja de cuenta corriente de los clientes de un banco,
hasta que el nombre y apellido sea FIN. Calcular y mostrar:
a) Nombre y apellido del cliente que tiene el mayor saldo en la caja de ahorro
b) Cantidad de clientes cuyo saldo en caja de ahorro o en cuenta corriente sea negativo.
c) Total de dinero depositado en ambas cajas.
d) Mostrar el nombre y apellido de aquellos clientes que no tienen dinero en ambas cuentas."""

# --- FUNCIONES ---

def cargar_clientes(arr_nombres, arr_ahorro, arr_corriente):
    
    print("--- SISTEMA DE GESTIÓN BANCARIA ---")
    nom = input("Nombre y Apellido (o 'FIN' para terminar): ").upper()
    
    while nom != "FIN":
        while nom == "":
            nom = input("Error - Ingrese un nombre válido: ").upper()
            
        s_ahorro = float(input(f"Saldo Caja de Ahorro de {nom}: $"))
        s_corriente = float(input(f"Saldo Cuenta Corriente de {nom}: $"))
        
        arr_nombres.append(nom)
        arr_ahorro.append(s_ahorro)
        arr_corriente.append(s_corriente)
        
        nom = input("\nNombre y Apellido (o 'FIN' para terminar): ").upper()
        
    return nombres, ahorro, corriente

# a) Nombre del cliente con mayor saldo en caja de ahorro
def buscar_maximo_ahorro(arr_nombres, arr_ahorro):
    pos_max = 0
    for i in range(1, len(arr_ahorro)):
        if arr_ahorro[i] > arr_ahorro[pos_max]:
            pos_max = i
    return pos_max

# b) Clientes con saldo negativo en alguna cuenta
def contar_negativos(arr_ahorro, arr_corriente):
    contador = 0
    for i in range(len(arr_ahorro)):
        if arr_ahorro[i] < 0 or arr_corriente[i] < 0:
            contador += 1
    return contador

# c) Total de dinero en ambas cajas
def calcular_total_general(arr_ahorro, arr_corriente):
    total = 0
    for i in range(len(ahorro)):
        total += arr_ahorro[i] + arr_corriente[i]
    return total

# d) Clientes sin dinero en AMBAS cuentas (Saldo 0 y Saldo 0)
def mostrar_sin_dinero(nombres, ahorro, corriente):
    print("\nClientes con saldo $0 en ambas cuentas:")
    encontrado = False
    for i in range(len(nombres)):
        if ahorro[i] == 0 and corriente[i] == 0:
            print(f"- {nombres[i]}")
            encontrado = True
    if not encontrado:
        print("No hay clientes en esta situación.")

# --- PROGRAMA PRINCIPAL ---
nombres = []
ahorro = []
corriente = []
    
cargar_clientes(nombres, ahorro, corriente)

if len(nombres) > 0:
    # Punto A
    cliente_max, monto_max = buscar_maximo_ahorro(nombres, ahorro)
    print(f"\na) Mayor saldo en Ahorro: {cliente_max} (${monto_max:.2f})")

    # Punto B
    cant_negativos = contar_negativos(ahorro, corriente)
    print(f"b) Clientes con algún saldo negativo: {cant_negativos}")

    # Punto C
    total_banco = calcular_total_general(ahorro, corriente)
    print(f"c) Total depositado en el banco: ${total_banco:.2f}")

    # Punto D
    print("d) Clientes sin dinero")
    mostrar_sin_dinero(nombres, ahorro, corriente)

else:
    print("\nNo se ingresaron datos de clientes.")

print("\n--- Fin del programa ---")