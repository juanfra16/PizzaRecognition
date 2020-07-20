import sys
import numpy as np


assert "-n" in sys.argv
num = sys.argv.index("-n")
sys.argv.pop(num)
cantidad = int(sys.argv.pop(num))
entrada, salida = sys.argv[1:3]


with open(entrada) as file:
    datos = file.readlines()

assert len(datos) >= cantidad

filas = np.asarray(datos)
with open(salida, "w") as file:
    file.write("".join(filas[np.random.choice(np.arange(0, len(datos),1), cantidad, replace=False)]))


