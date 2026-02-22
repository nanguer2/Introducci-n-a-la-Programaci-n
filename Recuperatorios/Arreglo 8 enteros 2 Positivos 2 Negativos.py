""" Pregunta 2 Ingresar números hasta cargar un arreglo con 8 números de la siguiente manera: 
dos números positivos y luego dos números negativos, en ese orden.
Por ejemplo: Se ingresan 1 2 3 4 5 6 -10 -20 4 5 6 -100 5 6 -8
El arreglo queda: 1 2 -10 -20 3 4 -100 -8 """

# --- FUNCIONES ---
def cargar_con_patron(espera, resultado):
    num = -1 

    # El bucle principal controla la carga TOTAL (hasta 8 elementos)
    while num != 0 and len(resultado) < 8:
        
        # --- SUB-BLOQUE: 2 POSITIVOS ---
        cant_bloque = 0
        while num != 0 and cant_bloque < 2 and len(resultado) < 8:
            # Revisar espera
            j = 0
            while j < len(espera) and cant_bloque < 2:
                if espera[j] > 0:
                    resultado.append(espera.pop(j))
                    cant_bloque += 1
                else:
                    j += 1
            
            # Pedir por teclado si falta completar el bloque de 2
            if num != 0 and cant_bloque < 2 and len(resultado) < 8:
                num = int(input(f"\n[{len(resultado)+1}/8] -> "))
                if num > 0:
                    resultado.append(num)
                    cant_bloque += 1
                elif num < 0:
                    espera.append(num)

        # --- SUB-BLOQUE: 2 NEGATIVOS ---
        cant_bloque = 0
        while num != 0 and cant_bloque < 2 and len(resultado) < 8:
            # Revisar espera
            j = 0
            while j < len(espera) and cant_bloque < 2:
                if espera[j] < 0:
                    resultado.append(espera.pop(j))
                    cant_bloque += 1
                else:
                    j += 1
            
            # Pedir por teclado si falta completar el bloque de 2
            if num != 0 and cant_bloque < 2 and len(resultado) < 8:
                num = int(input(f"[{len(resultado)+1}/8] -> "))
                if num < 0:
                    resultado.append(num)
                    cant_bloque += 1
                elif num > 0:
                    espera.append(num)             
    return resultado

# --- PROGRAMA PRINCIPAL ---
bolsa_espera = []
arreglo_final = []
print("\n--- Carga: 2 Positivos y 2 Negativos (0 para finalizar) ---")
print("\nIngrese un número entero...")
cargar_con_patron(bolsa_espera, arreglo_final)

if len(bolsa_espera) > 0:
    arreglo_final = cargar_con_patron(bolsa_espera, arreglo_final)
    print("\n" + "-"*35)
    print("Arreglo procesado (8 elementos):")
    print(arreglo_final)
    print("-"*35)
    if len(arreglo_final) < 8:
        print("Aviso: No hubo suficientes números para completar los 8 requeridos.")
else:
    print("\nNo se ingresaron datos.")

print("\n--- FIN DEL PROGRAMA ---\n") 