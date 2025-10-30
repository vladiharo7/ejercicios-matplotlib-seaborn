import matplotlib.pyplot as plt
import numpy as np

# Crear un generador de números aleatorios con una semilla específica
rng = np.random.default_rng(seed=42)

# Generación de datos aleatorios
x = rng.random(100)
y = rng.random(100)
colors = rng.random(100)
sizes = 1000 * rng.random(100)

# Creación del gráfico de dispersión
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='viridis')
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.title('Gráfico de dispersión multivariante')
plt.colorbar()  # Agrega una barra de color para interpretar los valores
plt.show()




import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Crear un generador de números aleatorios con una semilla específica
rng = np.random.default_rng(seed=42)

# Creación de un DataFrame de ejemplo
data = pd.DataFrame({
    'Variable A': rng.random(100),
    'Variable B': rng.random(100),
    'Variable C': rng.random(100),
    'Variable D': rng.random(100)
})

# Creación del pairplot
sns.pairplot(data)
plt.show()



# Añadir una variable categórica
data['Categoría'] = rng.choice(['Grupo 1', 'Grupo 2'], size=100)

# Creación del pairplot con hue
sns.pairplot(data, hue='Categoría')
plt.show()





import matplotlib.pyplot as plt
import numpy as np

# Crear un generador de números aleatorios con una semilla específica
rng = np.random.default_rng(seed=42)

# Generación de datos aleatorios para el ejemplo
x = rng.random(150)
y = rng.random(150)
colors = rng.random(150)
sizes = 500 * rng.random(150)

# Creación del gráfico de dispersión
plt.figure(figsize=(10, 6))
scatter = plt.scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap='plasma', edgecolors='w', linewidth=0.5)
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfico de dispersión con colores y tamaños')
plt.colorbar(scatter, label='Escala de colores')
plt.show()




import matplotlib.pyplot as plt
import numpy as np

# Crear un generador de números aleatorios con una semilla específica
rng = np.random.default_rng(seed=42)

# Generación de datos aleatorios y cálculo de la matriz de correlación
data = rng.random((10, 12))
correlation_matrix = np.corrcoef(data, rowvar=False)

# Creación del heatmap
plt.figure(figsize=(8, 6))
heatmap = plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='nearest')
plt.colorbar(heatmap, label='Coeficiente de correlación')
plt.title('Diagrama de calor de la matriz de correlación')
plt.xlabel('Variables')
plt.ylabel('Variables')
plt.xticks(ticks=np.arange(12), labels=[f'Var{i+1}' for i in range(12)], rotation=45)
plt.yticks(ticks=np.arange(12), labels=[f'Var{i+1}' for i in range(12)])
plt.show()







import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Crear un generador de números aleatorios con una semilla específica
rng = np.random.default_rng(seed=42)

# Generación de datos aleatorios para el ejemplo
x = rng.random(100)
y = rng.random(100)
z = rng.random(100)
colors = rng.random(100)
sizes = 100 * rng.random(100)

# Creación de la figura y el gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Gráfico de dispersión en 3D
scatter = ax.scatter(x, y, z, c=colors, s=sizes, cmap='viridis', alpha=0.6)
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')
plt.title('Gráfico de dispersión en 3D')
plt.colorbar(scatter, label='Escala de colores')
plt.show()








# Generación de una cuadrícula de puntos
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

# Creación de la figura y gráfico de superficie
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Gráfico de superficie
surface = ax.plot_surface(x, y, z, cmap='coolwarm', edgecolor='none')
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')
plt.title('Gráfico de superficie 3D')
plt.colorbar(surface, label='Valor de Z')
plt.show()
