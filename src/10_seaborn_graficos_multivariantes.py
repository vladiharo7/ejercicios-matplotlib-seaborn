import seaborn as sns
import pandas as pd

# Cargar un conjunto de datos de ejemplo
datos = sns.load_dataset('penguins')

# Explorar los datos
print(datos.head())




import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el conjunto de datos
datos = sns.load_dataset('penguins')

# Crear el pairplot
sns.pairplot(datos, hue='species')
plt.show()






sns.pairplot(
    datos,
    hue='species',
    corner=True,
    diag_kind='kde'
)
plt.show()








variables_interes = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm']

sns.pairplot(
    datos,
    vars=variables_interes,
    hue='species',
    corner=True,
    diag_kind='kde'
)
plt.show()






sns.pairplot(
    datos,
    hue='species',
    palette='Dark2',
    markers=['o', 's', 'D'],
    plot_kws={'alpha': 0.7}
)
plt.show()







# Eliminar filas con valores nulos
datos = datos.dropna()

# Crear el pairplot con datos limpios
sns.pairplot(datos, hue='species')
plt.show()








import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el conjunto de datos
datos = sns.load_dataset('tips')

sns.scatterplot(data=datos, x='total_bill', y='tip')
plt.show()



sns.scatterplot(data=datos, x='total_bill', y='tip', hue='day')
plt.show()





sns.scatterplot(data=datos, x='total_bill', y='tip', size='size')
plt.show()








sns.scatterplot(data=datos, x='total_bill', y='tip', hue='day', size='size')
plt.show()






sns.scatterplot(data=datos, x='total_bill', y='tip', hue='day', size='size', alpha=0.7)
plt.show()






sns.scatterplot(
    data=datos,
    x='total_bill',
    y='tip',
    hue='day',
    size='size',
    palette='Set2',
    sizes=(20, 200),
    alpha=0.7
)
plt.show()








sns.scatterplot(
    data=datos,
    x='total_bill',
    y='tip',
    hue='day',
    size='smoker',
    sizes=(50, 150),
    alpha=0.7
)
plt.show()




sns.scatterplot(
    data=datos,
    x='total_bill',
    y='tip',
    hue='day',
    size='smoker',
    sizes=(50, 150),
    alpha=0.7,
    legend='full'
)
plt.legend(title='Detalles', loc='upper left')
plt.show()






sns.relplot(
    data=datos,
    x='total_bill',
    y='tip',
    hue='day',
    size='size',
    col='time',
    kind='scatter',
    alpha=0.7
)
plt.show()





import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el conjunto de datos
datos = sns.load_dataset('flights')

# Reestructurar los datos en una tabla pivot
tabla_pivot = datos.pivot(index='month', columns='year', values='passengers')


# Crear el diagrama de calor
sns.heatmap(tabla_pivot)
plt.show()






# Crear el diagrama de calor con personalización
sns.heatmap(
    tabla_pivot,
    cmap='YlGnBu',
    annot=True,
    fmt='d'
)
plt.show()






# Cargar el conjunto de datos
iris = sns.load_dataset('iris')

# Calcular la matriz de correlación
corr = iris.select_dtypes(include=['float64', 'int64']).corr()


# Crear el diagrama de calor de correlación
sns.heatmap(
    corr,
    annot=True,
    cmap='coolwarm'
)
plt.show()





# Crear el diagrama de calor personalizado
sns.heatmap(
    corr,
    annot=True,
    cmap='coolwarm',
    vmin=-1,
    vmax=1,
    xticklabels=iris.columns,
    yticklabels=iris.columns
)
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.show()




import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

datos = sns.load_dataset('flights')

tabla_pivot = datos.pivot(index='month', columns='year', values='passengers')

# Normalizar los datos de la tabla pivot
tabla_normalizada = tabla_pivot.apply(lambda x: (x - np.mean(x)) / np.std(x), axis=1)

# Crear el diagrama de calor de los datos normalizados
sns.heatmap(
    tabla_normalizada,
    cmap='RdBu_r',
    center=0
)
plt.show()







# Crear una máscara para los valores inferiores a 500
mascara = tabla_pivot < 500

# Crear el diagrama de calor con la máscara
sns.heatmap(
    tabla_pivot,
    cmap='YlGnBu',
    mask=mascara,
    annot=True,
    fmt='d'
)
plt.show()





import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el conjunto de datos
datos = sns.load_dataset('flights')






# Crear la tabla pivote
tabla_pivot = datos.pivot(index='month', columns='year', values='passengers')







# Generar el clustermap básico
sns.clustermap(tabla_pivot)
plt.show()





sns.clustermap(
    tabla_pivot,
    method='average',
    metric='correlation',
    cmap='YlGnBu'
)
plt.show()





# Estandarizar los datos por columnas
sns.clustermap(
    tabla_pivot,
    standard_scale=1,
    cmap='mako'
)
plt.show()






# Aplicar z-score por filas
sns.clustermap(
    tabla_pivot,
    z_score=0,
    cmap='vlag'
)
plt.show()





sns.clustermap(
    tabla_pivot,
    figsize=(12, 8),
    dendrogram_ratio=0.2,
    cbar_pos=(0.9, 0.7, 0.03, 0.2)
)
plt.show()




# Cargar el conjunto de datos
iris = sns.load_dataset('iris')

# Calcular la matriz de correlación
matriz_corr = iris.select_dtypes(include=['float64', 'int64']).corr()

# Generar el clustermap de correlación
sns.clustermap(
    matriz_corr,
    annot=True,
    cmap='coolwarm',
    center=0
)
plt.show()




sns.clustermap(
    tabla_pivot,
    cmap='rocket',
    vmin=100,
    vmax=700
)
plt.show()






import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Configurar el estilo de Seaborn
sns.set_theme(style='whitegrid')


# Cargar el conjunto de datos
iris = sns.load_dataset('iris')



# Crear la figura y el eje 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(projection='3d')

# Definir las variables para los ejes
x = iris['sepal_length']
y = iris['sepal_width']
z = iris['petal_length']

# Mapear las especies a colores
from matplotlib.colors import ListedColormap
import pandas as pd

# Convertir las especies a números
especies = pd.Categorical(iris['species']).codes

# Obtener una paleta de colores de Seaborn
paleta = sns.color_palette('bright', len(iris['species'].unique()))
colormap = ListedColormap(paleta)

# Graficar los datos
scatter = ax.scatter(x, y, z, c=especies, cmap=colormap)

# Añadir una leyenda
legend = ax.legend(*scatter.legend_elements(),
                   title='Especies',
                   loc='upper left',
                   bbox_to_anchor=(1, 0.5))

# Etiquetas de los ejes
ax.set_xlabel('Longitud del sépalo')
ax.set_ylabel('Ancho del sépalo')
ax.set_zlabel('Longitud del pétalo')

# Mostrar la gráfica con leyenda
ax.add_artist(legend)
plt.show()





import numpy as np

# Crear una cuadrícula de puntos
X = np.linspace(-5, 5, 100)
Y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Crear la figura y el eje 3D
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(projection='3d')

# Graficar la superficie
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

# Añadir una barra de color
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

# Etiquetas de los ejes
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')

# Título
ax.set_title('Superficie 3D de función matemática')

# Mostrar la gráfica
plt.show()
