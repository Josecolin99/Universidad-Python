# Un diccionario está compuesto de llave,valor(key,value)
diccionario = {
    "IDE": "Integrated Development Evironment",
    "OOP": "Object Oriented Programming",
    "DBMS": "Database Managment System"
}
print(diccionario)

# Largo de un diccionario
print(len(diccionario))

# Accediando a un elemento
print(diccionario["IDE"])

# Otra forma con el mismo resultado
print(diccionario.get("IDE"))

# Modificando valores
diccionario["IDE"] = "Integrated development evironment"
print(diccionario)

# Iterar
for termino in diccionario:
    print(termino)
for termino in diccionario:
    print(termino, ":", diccionario[termino])
for valor in diccionario.values():
    print(valor)

# Comprobando existencia de un elemento
print("IDE" in diccionario)

# Agregar nuevo elemento
diccionario["PK"] = "Primary Key"
print(diccionario)

# Remover elementos
diccionario.pop("DBMS")
print(diccionario)

# Limpiar
diccionario.clear()
print(diccionario)

# Eliminar por completo
del diccionario
# print(diccionario)
