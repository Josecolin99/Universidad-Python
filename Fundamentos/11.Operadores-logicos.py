#a = int(input("Proporciona un valor "))
a = 3
valorMinimo = 0
valorMaximo = 5
#Con and, ambas condiciones deben ser True
dentroRango = (a >= valorMinimo and a <= valorMaximo)
# print(dentroRango)
if(dentroRango):
    print("Dentro de rango")
else:
    print("Fuera de rango")
    
vacaciones = False
diaDescanso = False
#Con or, solo se necesita que una sea verdadero 
if(vacaciones or diaDescanso):
    print("Puedes ir al parque")
else:
    print("Tienes deberes que hacer")

#Not invierte el resultado bool

print(not(vacaciones))