salas_comp = 0
total_butacas = 0
total_vendidas = 0
sala_menor = 0

# Procesamos las 15 salas en un solo bucle
for i in range(15):
  num_sala = int(input("Ingrese el numero de sala: \t"))
  while num_sala < 0:
    num_sala = int(input("Error. Ingrese el numero de sala: \t"))
    
  cant_butacas = int(input("Ingrese la cantidad total de butacas: \t"))
  while cant_butacas < 1:
    cant_butacas = int(input("Error. Ingrese la cantidad total de butacas: \t"))
    
  cant_vendidas = int(input("Ingrese la cantidad de butacas vendidas: \t"))
  while cant_vendidas < 0:
    cant_vendidas = int(input("Error. Ingrese la cantidad de butacas vendidas: \t"))
    
    # Acumuladores
  total_butacas += cant_butacas
  total_vendidas += cant_vendidas
    
  if i == 0:
    mayorcant_vendidas = cant_vendidas
    sala_mayor = num_sala
    menorcant_vendidas = cant_vendidas
    sala_menor = num_sala  # Agregar inicialización
    
    # Buscar mínimo
  if cant_vendidas < menorcant_vendidas:
    menorcant_vendidas = cant_vendidas
    sala_menor = num_sala
   
    # Buscar máximo
  if cant_vendidas > mayorcant_vendidas:
    mayorcant_vendidas = cant_vendidas
    sala_mayor = num_sala
    
    # Calcular porcentaje de la sala
  porce_vendidas = (cant_vendidas * 100) / cant_butacas
  print(f"El porcentaje de butacas vendidas de la sala es: {porce_vendidas:.1f}%\n")
    
    # Verificar si la sala está completa
  if cant_butacas == cant_vendidas:
    salas_comp += 1

print("Finalizo el ingreso de datos\n")        
print("--------------Resultados finales--------------------------\n")
print(f"El numero de sala con menor cantidad de butacas vendidas es: {sala_menor}\n")

if salas_comp == 0:
    print("En ninguna sala se vendio el total de butacas.\n")
else:
    print(f"En {salas_comp} sala(s) se vendieron el total de butacas.\n")

promedio_vendidas = (total_vendidas * 100) / total_butacas
print(f"El promedio de butacas vendidas de todo el cine es: {promedio_vendidas:.1f}%\n")

print(f"El numero de sala con mayor capacidad de butacas vendidas es: {sala_mayor}\n")
