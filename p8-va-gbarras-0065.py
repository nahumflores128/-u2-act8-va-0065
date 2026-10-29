import matplotlib.pyplot as plt
import numpy as np

diasX = ["Lun", "Mar", "Mie", "Jue", "Vie"]
califa_va_y = [5, 6, 3, 8, 10]

plt.bar(diasX, califa_va_y)
plt.title("Califas en VA de Nahum flores NC 0065")
plt.xlabel("dias de la seamana habil")
plt.ylabel("Calificaciones en VA")
plt.grid()
plt.show()