import matplotlib.pyplot as plt
import subprocess

notas = [1, 4, 7, 9, 10]

plt.plot(notas)
plt.savefig("notas_obtenidas.png", dpi=300)

#xdg-open <filename>
