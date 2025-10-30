import seaborn as sns
import matplotlib.pyplot as plt

# Cargar conjunto de datos de ejemplo
data = sns.load_dataset('penguins')

# Crear un histograma de la variable 'flipper_length_mm'
sns.histplot(data=data, x='flipper_length_mm')

# Mostrar la gráfica
plt.show()



# Crear una figura y un eje
fig, ax = plt.subplots()

# Crear un histograma en el eje especificado
sns.histplot(data=data, x='flipper_length_mm', ax=ax)

# Personalizar el eje
ax.set_title('Distribución del largo de aletas')
ax.set_xlabel('Largo de aleta (mm)')
ax.set_ylabel('Frecuencia')

# Mostrar la gráfica
plt.show()




# Crear una figura con tres ejes en una fila
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Gráfica 1: Histograma del largo de aletas
sns.histplot(data=data, x='flipper_length_mm', ax=axes[0])
axes[0].set_title('Largo de aletas')

# Gráfica 2: Histograma del peso corporal
sns.histplot(data=data, x='body_mass_g', ax=axes[1], color='orange')
axes[1].set_title('Peso corporal')

# Gráfica 3: Gráfico de dispersión largo de aletas vs peso
sns.scatterplot(data=data, x='flipper_length_mm', y='body_mass_g', ax=axes[2], hue='species')
axes[2].set_title('Relación entre largo de aletas y peso')

# Ajustar el layout y mostrar la gráfica
plt.tight_layout()
plt.show()




# Crear una figura y un eje
fig, ax = plt.subplots()

# Gráfico de densidad con Seaborn
sns.kdeplot(data=data, x='flipper_length_mm', ax=ax, fill=True, alpha=0.5)

# Añadir una línea vertical con Matplotlib
ax.axvline(data['flipper_length_mm'].mean(), color='red', linestyle='--', label='Media')

# Personalizar el eje
ax.set_title('Distribución y media del largo de aletas')
ax.legend()

# Mostrar la gráfica
plt.show()





# Crear una figura y un eje
fig, ax = plt.subplots()

# Gráfico de caja y bigotes
sns.boxplot(data=data, x='species', y='body_mass_g', ax=ax)

# Rotar etiquetas del eje x (forma recomendada)
ax.tick_params(axis='x', rotation=45)

# Ajustar formato de los ticks del eje y
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

# Añadir título y etiquetas
ax.set_title('Peso corporal por especie')
ax.set_xlabel('Especie')
ax.set_ylabel('Peso corporal (g)')

# Mostrar la gráfica
plt.tight_layout()  # Ajustar diseño para evitar superposición
plt.show()




import seaborn as sns
import matplotlib.pyplot as plt

# Cargar conjunto de datos
data = sns.load_dataset('tips')

# Crear histograma
ax = sns.histplot(data=data, x='total_bill')

# Establecer límites del eje x
ax.set_xlim(0, 60)

# Mostrar gráfica
plt.show()





# Crear gráfico de dispersión
ax = sns.scatterplot(data=data, x='total_bill', y='tip')

# Establecer límites de los ejes
ax.set_xlim(10, 40)
ax.set_ylim(0, 10)

# Mostrar gráfica
plt.show()






# Crear subgráficas
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Primer gráfico
sns.scatterplot(data=data, x='total_bill', y='tip', ax=axes[0])
axes[0].set_title('Propinas vs Total de la cuenta')

# Segundo gráfico con una variable adicional
sns.scatterplot(data=data, x='total_bill', y='tip', hue='time', ax=axes[1])
axes[1].set_title('Propinas por momento del día')

# Unificar límites de los ejes
for ax in axes:
    ax.set_xlim(0, 60)
    ax.set_ylim(0, 12)

# Ajustar diseño y mostrar
plt.tight_layout()
plt.show()





# Obtener límites actuales
x_min, x_max = ax.get_xlim()
y_min, y_max = ax.get_ylim()

# Expandir límites en un 10%
ax.set_xlim(x_min * 0.9, x_max * 1.1)
ax.set_ylim(y_min * 0.9, y_max * 1.1)





# Restablecer límites automáticos
ax.relim()
ax.autoscale()







import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Crear un generador de números aleatorios con una semilla
rng = np.random.default_rng(seed=42)

# Generar datos con distribución exponencial
data = rng.exponential(scale=1.0, size=1000)

# Crear histograma
fig, ax = plt.subplots()
sns.histplot(data, ax=ax)

# Establecer escala logarítmica en el eje y
ax.set_yscale('log')

# Añadir etiquetas y título
ax.set_xlabel('Valor')
ax.set_ylabel('Frecuencia')
ax.set_title('Histograma con escala logarítmica en el eje y')

# Mostrar gráfica
plt.show()






# Generar datos
x = np.linspace(1, 1000, 100)
y = x ** 2

# Crear gráfico de dispersión
fig, ax = plt.subplots()
sns.scatterplot(x=x, y=y, ax=ax)

# Establecer escala logarítmica en ambos ejes
ax.set_xscale('log')
ax.set_yscale('log')

# Añadir etiquetas y título
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Gráfico de dispersión con escalas logarítmicas')

# Mostrar gráfica
plt.show()







# Crear un generador de números aleatorios con una semilla
rng = np.random.default_rng(seed=42)

# Datos con valores negativos y positivos
data = np.concatenate((rng.normal(-1000, 300, 1000), rng.normal(1000, 300, 1000)))

# Crear histograma
fig, ax = plt.subplots()
sns.histplot(data, bins=50, ax=ax)

# Establecer escala simbólica en el eje x
ax.set_xscale('symlog', linthresh=500)

# Añadir etiquetas y título
ax.set_xlabel('Valor')
ax.set_ylabel('Frecuencia')
ax.set_title('Histograma con escala simbólica en el eje x')

# Mostrar gráfica
plt.show()






# Crear un generador de números aleatorios con una semilla
rng = np.random.default_rng(seed=42)

# Datos de proporciones
data = rng.beta(a=0.5, b=0.5, size=1000)

# Crear histograma
fig, ax = plt.subplots()
sns.histplot(data, bins=50, ax=ax)

# Establecer escala logit en el eje x
ax.set_xscale('logit')

# Configurar límites y ticks
ax.set_xlim(0.001, 0.999)
ax.set_xticks([0.01, 0.1, 0.5, 0.9, 0.99])
ax.get_xaxis().set_major_formatter(plt.ScalarFormatter())

# Añadir etiquetas y título
ax.set_xlabel('Proporción')
ax.set_ylabel('Frecuencia')
ax.set_title('Histograma con escala logit en el eje x')

# Mostrar gráfica
plt.show()







# Ajustar ticks y etiquetas en escala logarítmica
ax.set_yscale('log')
ax.yaxis.set_major_locator(plt.LogLocator(base=10))
ax.yaxis.set_major_formatter(plt.FormatStrFormatter('%.0f'))







# Crear datos
x = np.linspace(0.1, 10, 100)
y1 = np.exp(x)
y2 = np.log(x)

# Crear subgráficas
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Gráfica 1 con escala logarítmica en el eje y
sns.lineplot(x=x, y=y1, ax=axes[0])
axes[0].set_yscale('log')
axes[0].set_title('Escala logarítmica en el eje y')
axes[0].set_xlabel('X')
axes[0].set_ylabel('Y1')

# Gráfica 2 con escala logarítmica en el eje x
sns.lineplot(x=x, y=y2, ax=axes[1])
axes[1].set_xscale('log')
axes[1].set_title('Escala logarítmica en el eje x')
axes[1].set_xlabel('X')
axes[1].set_ylabel('Y2')

# Ajustar diseño y mostrar
plt.tight_layout()
plt.show()








