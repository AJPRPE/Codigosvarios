import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Datos de entrenamiento: tamaño en pies cuadrados de las casas
tamanio_casas = np.array([1400, 1600, 1700, 1875, 1100, 1550, 2350, 2450, 1425, 1700])

# Precios correspondientes de las casas
precios_casas = np.array([245000, 312000, 279000, 308000, 199000, 219000, 405000, 324000, 319000, 255000])

# Crear un modelo de regresión lineal
modelo = LinearRegression()

# Entrenar el modelo con los datos
modelo.fit(tamanio_casas.reshape(-1, 1), precios_casas)

# Hacer una predicción para una casa de 2000 pies cuadrados
tamanio_casa_nueva = np.array([2000])
precio_predicho = modelo.predict(tamanio_casa_nueva.reshape(-1, 1))

print(f"El precio predicho para una casa de 2000 pies cuadrados es: ${precio_predicho[0]:,.2f}")

# Visualizar los datos y la línea de regresión
plt.scatter(tamanio_casas, precios_casas, color='blue')
plt.plot(tamanio_casas, modelo.predict(tamanio_casas.reshape(-1, 1)), color='red', linewidth=2)
plt.title("Regresión Lineal Simple")
plt.xlabel("Tamaño de la casa (pies cuadrados)")
plt.ylabel("Precio de la casa ($)")
plt.show()
