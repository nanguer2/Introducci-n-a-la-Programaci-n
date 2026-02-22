"""La cantina Al paso vende comidas rápidas y requiere un sistema para registrar las operaciones del día. El menú que ofrece es:
Tortilla de papas ($2500), Guiso de lentejas ($3750), Hamburguesa ($5600), Agua ($1200) y Gaseosa ($1500).
A. Mostrar Facturas, B. Factura con el máximo en ventas, C. Promedio de comidas, D. Porcentajes de bebidas.
- El sistema debe registrar el número de factura, el monto total por la comida y el monto total por las bebidas. (usando arreglos paralelos)
- Cargar los datos de las facturas hasta que esta sea 0. El numero de la factura es entero y no puede ser negativo.
- Se le debe solicitar al usuario el plato y la cantidad. Validar la comida. (T para tortilla, G para guiso, H para hamburguesa)
- Se le debe solicitar al usuario si quiere bebida."""
   
# --- FUNCIONES ---
def calcular_monto_comida():
    print("\nMenú: [T]ortilla ($2500), [G]uiso ($3750), [H]amburguesa ($5600)")
    plato = input("Seleccione el plato (T, G, H): ").upper()
    while plato != 'T' and plato != 'G' and plato != 'H':
        plato = input("Error - Ingrese T, G o H: ").upper()
    cantidad = int(input(f"¿Cuántas unidades de '{plato}' desea?: "))
    if plato == 'T':
        return cantidad * 2500
    elif plato == 'G':
        return cantidad * 3750
    else: # Es H
        return cantidad * 5600


def calcular_monto_bebida():
    monto = 0
    quiere_bebida = input("\n¿Quiere bebida? (S/N): ").upper()
    if quiere_bebida == 'S':
        print("Bebidas: [A]gua ($1200), [G]aseosa ($1500)")
        tipo = input("Seleccione bebida (A/G): ").upper()
        while tipo !='A' and tipo != 'G':
            tipo = input("Error - Ingrese A o G: ").upper()
        cant = int(input("¿Cantidad de bebidas?: "))
        if tipo == 'A':
            monto = cant * 1200
        else:
            monto = cant * 1500    
    return monto


def registrar_operaciones(arr_facturas, montos_comida, montos_bebida):
    print("\n--- Sistema de Ventas: Cantina Al Paso ---")
    # Pedimos la primera factura
    num_factura = int(input("\nIngrese número de factura (0 para finalizar): "))
    # El bucle principal solo se detiene con el 0
    while num_factura != 0:
        # Validación: Si es negativa, avisamos y pedimos de nuevo
        if num_factura < 0:
            print("Error: El número de factura no puede ser negativo.")
        else:
            # Si es válida y no es cero, procedemos a la carga
            total_c = calcular_monto_comida()
            total_b = calcular_monto_bebida()
            # Guardamos en los arreglos paralelos
            arr_facturas.append(num_factura)
            montos_comida.append(total_c)
            montos_bebida.append(total_b)
            print(f"\nFactura #{num_factura} registrada con éxito.")
        # Volvemos a pedir factura para la siguiente vuelta o para salir
        num_factura = int(input("\nIngrese número de factura (0 para finalizar): "))


def factura_mayor_venta(arr_facturas, montos_comida, montos_bebida):
    pos_mayor = 0
    mayor_monto = 0
    for i in range(len(arr_facturas)):
        total_factura = montos_comida[i] + montos_bebida[i]
        if total_factura > mayor_monto:
            mayor_monto = total_factura
            pos_mayor = i   
    print(f"La factura con más ventas fue: {facturas[pos_mayor]} con un total de {mayor_monto}")


def analizar_promedio_comidas(arr_facturas, montos_comida):
    suma_comidas = 0
    # 1. Usamos len() para saber cuántos hay, o un contador que sume
    cantidad_facturas = len(montos_comida)
    # Sumamos los montos reales de comida
    for i in range(len(montos_comida)):
        suma_comidas += montos_comida[i] # Sumamos el valor del arreglo
    # 2. Verificamos que haya facturas para no dividir por cero
    if cantidad_facturas > 0:
        promedio = suma_comidas / cantidad_facturas
        print(f"\nEl promedio de ventas en comida es: ${promedio:.2f}")
        print("\nFacturas con ventas de comida menores al promedio:")
        # 3. Buscamos las facturas menores al promedio
        for i in range(len(montos_comida)):
            if montos_comida[i] < promedio:
                print(f"- Factura #{arr_facturas[i]} (Monto: ${montos_comida[i]})")
    else:
        print("\nNo hay ventas registradas para calcular el promedio.")

            
def porcentaje_sin_bebidas(montos_bebida):
    cont_sin_bebida = 0
    if len(montos_bebida) >0:   
        for i in range (len(montos_bebida)):
            if montos_bebida[i] == 0:
                cont_sin_bebida += 1           
    porcentaje = (cont_sin_bebida / (len(montos_bebida))) * 100
    return porcentaje

# --- PPAL ---
# Arreglos paralelos para el registro
facturas = []
comidas = []
bebidas = []

registrar_operaciones(facturas, comidas, bebidas)

if len(facturas) > 0:
    print("\nA. Mostrar Facturas:")
    print("\n" + "="*40)
    print(f"{'Factura':<10} | {'Comida':<12} | {'Bebida':<12}")
    print("-" * 40)
    for i in range(len(facturas)):
        print(f"{facturas[i]:<10} | ${comidas[i]:<11} | ${bebidas[i]:<11}")
    print("="*40)
    print("\nB. Factura con el máximo en ventas:")
    factura_mayor_venta(facturas, comidas, bebidas)
    print("\nC. Promedio de comidas:")
    analizar_promedio_comidas(facturas, comidas)
    print("\nD. Porcentajes de bebidas:")
    porc = porcentaje_sin_bebidas(bebidas)
    print(f"Porcentaje de facturas que NO incluyeron bebidas: {porc:.2f}%")
else:
    print("\nNo se ingresaron datos...")    
print("\nFin del programa.\n")