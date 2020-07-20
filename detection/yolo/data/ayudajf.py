import sys

archivo1, nuevo = sys.argv[1:3]

with open(archivo1) as file:
    datos = file.read().replace("../","")

with open(nuevo, "w") as file:
    file.write(datos)


