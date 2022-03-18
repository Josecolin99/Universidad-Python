condicion = False
#modo ternario (Solo valido en operaciones simples)
print("Condicion verdadera") if condicion else print("Condicion falsa")
#modo normal
if condicion == True:
    print("La condicion es verdadera")
elif condicion == False:
    print("La condicion es falsa")
else:
    print("Condicion no reconocida")
    
numero = int(input("Proporcione un numero entre 1 y 3: "))
if numero == 1:
    numero_texto = "numero 1"
elif numero == 2:
    numero_texto = "numero 2"
elif numero == 3:
    numero_texto = "numero 3"
else:
    numero_texto = "Valor fuera de rango"

print("numero proporcionado: ", numero_texto)