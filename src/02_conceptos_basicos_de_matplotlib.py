import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8, 6), dpi=100)

ax = fig.add_subplot(111)

ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')

ax.set_title('Título de la gráfica')

ax.plot([1, 2, 3], label='Serie 1')
ax.legend()

plt.show()


categorias = ['A', 'B', 'C']
valores = [4, 7, 1]
plt.bar(categorias, valores)
plt.xlabel('Categoría')
plt.ylabel('Valor')
plt.title('Gráfico de barras')
plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Crear un generador de números aleatorios con una semilla específica
rng = np.random.default_rng(seed=42)

# Generar los datos aleatorios utilizando el generador
datos = rng.standard_normal(1000)

# Crear el histograma
plt.hist(datos, bins=30)
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.title('Histograma')

# Mostrar el gráfico
plt.show()


import matplotlib.pyplot as plt

x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 5, 6, 7]
y = [7, 4, 3, 8, 3, 2, 4, 9, 6, 1, 8, 7, 1, 2, 6]
plt.scatter(x, y)
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.title('Diagrama de dispersión')
plt.show()



import matplotlib.pyplot as plt

labels = 'A', 'B', 'C', 'D'
sizes = [15, 30, 45, 10]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Gráfico de sectores')
plt.show()








import matplotlib.pyplot as plt
import numpy as np

# Crear un generador de números aleatorios con una semilla específica
rng = np.random.default_rng(seed=42)

# Generar datos aleatorios utilizando el generador
data = rng.random((10, 10))

# Crear el mapa de calor
plt.imshow(data, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title('Mapa de calor')

# Mostrar el gráfico
plt.show()



