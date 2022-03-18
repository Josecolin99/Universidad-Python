# Tupla mantienen el orden, pero ya no se puede modificar
frutas = ("Naranja", "Platano", "Guayaba")
print(frutas)
# largo de la tupla
print(len(frutas))
# accediendo a un elemento
print(frutas[0])
# navegacion inversa
print(frutas[-1])
# rango
# print(frutas[0:2]) #excluyendo el indice 2
frutaLista = list(frutas)
frutaLista[1] = "Platanito"
frutas = tuple(frutaLista)
print(frutas)
# iterar una tupla
for fruta in frutas:
    print(fruta, end=" ")
# no podemos agregar ni eliminar elementos de una tupla

# Pero si eliminar la tupla
del frutas
print(frutas)