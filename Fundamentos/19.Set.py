# Set es una colección din orden y sin indices, no permite elementos repetidos
# y los elementos no se pueden modificarl, pero si se agregar nuevos o eliminar
planetas = {"Marte", "Jupiter", "Venus"}
print(planetas)
# Revisar el largo
print(len(planetas))
# Revisar si un elemrto esta presente
print("Tierra" in planetas)
# agreagar elementos
planetas.add("Tierra")
print(planetas)
planetas.add("Tierra")  # no se pueden agregar elementos duplicados
print(planetas)
# eliminar con remove posiblemente arroja exepcion si no se encuentra el
# elemento a eliminar
planetas.remove("Tierra")
print(planetas)
#Eliminar con discard no arroja una exepción si no encuentra el elemento
planetas.discard("Jupiters")
print(planetas)
#Limpiar el set
planetas.clear()
print(planetas)
#elimianr set
del planetas
#print(planetas)