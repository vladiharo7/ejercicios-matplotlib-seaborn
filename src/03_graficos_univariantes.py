import matplotlib.pyplot as plt
import numpy as np

# Crear un generador de números aleatorios con una semilla específica
rng = np.random.default_rng(seed=42)

# Generar datos aleatorios utilizando el generador
data = rng.standard_normal(1000)

# Crear el histograma
plt.hist(data, bins=30, edgecolor='black')

# Añadir título y etiquetas
plt.title('Histograma de datos univariantes')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')

# Mostrar la gráfica
plt.show()



import matplotlib.pyplot as plt
import numpy as np

# Crear un generador de números aleatorios con una semilla específica
rng = np.random.default_rng(seed=42)

# Generar datos aleatorios utilizando el generador (distribución normal)
data = rng.normal(0, 1, 1000)

# Crear el histograma
plt.hist(data, bins=30, color='blue', alpha=0.7, edgecolor='black')

# Configurar título y etiquetas
plt.title('Distribución de Datos')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')

# Mostrar gráfico
plt.show()



plt.hist(data, bins=30, cumulative=True, color='green', edgecolor='black')
plt.title('Histograma Acumulativo')
plt.xlabel('Valores')
plt.ylabel('Frecuencia Acumulada')
plt.show()




plt.hist(data, bins=30, density=True, color='purple', alpha=0.6, edgecolor='black')
plt.title('Densidad de Probabilidad')
plt.xlabel('Valores')
plt.ylabel('Densidad')
plt.show()



import matplotlib.pyplot as plt
import numpy as np

# Crear un generador de números aleatorios con una semilla específica
rng = np.random.default_rng(seed=42)

# Generar datos de ejemplo con diferentes desviaciones estándar
data = [rng.normal(0, std, 100) for std in range(1, 4)]

# Crear el boxplot
plt.boxplot(data, vert=True, patch_artist=True, showmeans=True)

# Configurar título y etiquetas
plt.title('Diagrama de Caja y Bigotes')
plt.xlabel('Grupos')
plt.ylabel('Valores')

# Mostrar gráfico
plt.show()



plt.boxplot(data, patch_artist=True,
            boxprops=dict(facecolor='lightblue', color='blue'),
            whiskerprops=dict(color='blue'),
            capprops=dict(color='blue'),
            flierprops=dict(marker='o', color='red', alpha=0.5),
            medianprops=dict(color='red'))
plt.title('Diagrama de Caja y Bigotes Personalizado')
plt.xlabel('Grupos')
plt.ylabel('Valores')
plt.show()



import matplotlib.pyplot as plt
import numpy as np

# Crear un generador de números aleatorios con una semilla específica
rng = np.random.default_rng(seed=42)

# Generar datos de ejemplo con diferentes desviaciones estándar
data = [rng.normal(0, std, 100) for std in range(1, 4)]

# Crear el gráfico de violín
plt.violinplot(data, showmeans=True, showmedians=True)

# Configurar título y etiquetas
plt.title('Gráfico de Violín')
plt.xlabel('Grupos')
plt.ylabel('Valores')

# Mostrar gráfico
plt.show()





parts = plt.violinplot(data, showmeans=False, showmedians=True)

# Personalizar la apariencia
for pc in parts['bodies']:
    pc.set_facecolor('lightblue')
    pc.set_edgecolor('black')
    pc.set_alpha(0.7)
parts['cmedians'].set_edgecolor('red')

plt.title('Gráfico de Violín Personalizado')
plt.xlabel('Grupos')
plt.ylabel('Valores')
plt.show()






import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Crear la gráfica de línea
plt.plot(x, y, label='Seno', color='blue', linewidth=2)

# Añadir título y etiquetas
plt.title('Gráfica de Línea de una Función Seno')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Añadir leyenda
plt.legend()

# Mostrar la gráfica
plt.show()





y2 = np.cos(x)
plt.plot(x, y, label='Seno', color='blue', linestyle='-', marker='o')
plt.plot(x, y2, label='Coseno', color='red', linestyle='--', marker='x')

# Configurar título y etiquetas
plt.title('Gráfica de Línea de Seno y Coseno')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Añadir leyenda
plt.legend()

# Mostrar gráfico
plt.show()

