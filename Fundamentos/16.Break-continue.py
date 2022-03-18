# Break
# Imprimir solo las letras a
for letra in "Holanda":
    if letra == "a":
        print(letra)
        break
else:
    print("Fin ciclo for")

print("Continua el programa")

# Continue
# Imprimir solo nuemros pares
for i in range(6):
    if i % 2 != 0:
        continue
        print(i)
    print(i)
