import seaborn as sns
print(sns.__version__)

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Crear un generador de números aleatorios con una semilla específica
rng = np.random.default_rng(seed=42)

# Generar datos sintéticos con el generador
x = rng.random(100)
y = rng.random(100)

# Crear un gráfico de dispersión con Seaborn
sns.scatterplot(x=x, y=y)

# Mostrar el gráfico
plt.show()



import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Crear un DataFrame de ejemplo
datos = pd.DataFrame({
    'edad': [23, 45, 12, 36, 22],
    'ingresos': [50000, 80000, 20000, 60000, 45000],
    'sexo': ['M', 'F', 'M', 'F', 'M']
})

# Crear un gráfico de barras con Seaborn
sns.barplot(data=datos, x='sexo', y='ingresos')

# Mostrar el gráfico
plt.show()





import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Crear un generador de números aleatorios con una semilla específica
rng = np.random.default_rng(seed=42)

# Suponiendo un DataFrame 'ventas' con una columna de fechas
ventas = pd.DataFrame({
    'fecha': pd.date_range(start='2023-01-01', periods=12, freq='ME'),
    'monto': rng.integers(1000, 5000, size=12)
})

# Convertir la columna 'fecha' en el índice del DataFrame
ventas.set_index('fecha', inplace=True)

# Crear un gráfico de línea con Seaborn
sns.lineplot(data=ventas, x=ventas.index, y='monto')

# Mostrar el gráfico
plt.show()


# Crear un gráfico de barras con agregación
sns.barplot(data=datos, x='sexo', y='ingresos', estimator=np.mean)

# Mostrar el gráfico
plt.show()


# Filtrar los datos para incluir solo individuos mayores de 30 años
datos_filtrados = datos[datos['edad'] > 30]

# Crear un gráfico de dispersión con los datos filtrados
sns.scatterplot(data=datos_filtrados, x='edad', y='ingresos')

# Mostrar el gráfico
plt.show()





import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el conjunto de datos 'tips'
datos = sns.load_dataset('tips')

# Mostrar las primeras filas del conjunto de datos
print(datos.head())


# Crear un diagrama de dispersión
sns.scatterplot(data=datos, x='total_bill', y='tip')

# Mostrar el gráfico
plt.show()


# Diagrama de dispersión diferenciando por género
sns.scatterplot(data=datos, x='total_bill', y='tip', hue='sex')

# Mostrar el gráfico
plt.show()



# Histograma y estimación de densidad para la variable 'total_bill'
sns.histplot(data=datos, x='total_bill', kde=True)

# Mostrar el gráfico
plt.show()



# Boxplot del total de la cuenta por día de la semana
sns.boxplot(data=datos, x='day', y='total_bill')

# Mostrar el gráfico
plt.show()


# Violinplot del total de la cuenta por tiempo de comida
sns.violinplot(data=datos, x='time', y='total_bill')

# Mostrar el gráfico
plt.show()




# Pairplot con diferenciación por género
sns.pairplot(data=datos, hue='sex')

# Mostrar el gráfico
plt.show()





# Establecer estilo y paleta
sns.set_style('whitegrid')
sns.set_palette('bright')

# Crear un gráfico con el nuevo estilo y paleta
sns.barplot(data=datos, x='day', y='total_bill', hue='sex')

# Mostrar el gráfico
plt.show()




# Crear un gráfico de línea del total de la cuenta
sns.lineplot(data=datos, x='size', y='total_bill', errorbar=None)

# Añadir título y etiquetas
plt.title('Total de la cuenta según el tamaño del grupo')
plt.xlabel('Tamaño del grupo')
plt.ylabel('Total de la cuenta ($)')

# Mostrar el gráfico
plt.show()

