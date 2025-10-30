import seaborn as sns

'''
Los temas disponibles en seaborn son:

darkgrid: fondo gris con cuadrículas.
whitegrid: fondo blanco con cuadrículas.
dark: fondo gris sin cuadrículas.
white: fondo blanco sin cuadrículas.
ticks: similar a 'white' pero con marcas de graduación en los ejes.
'''

sns.set_style("whitegrid")


sns.set_style("ticks")
sns.despine()


sns.set_context("talk")


datos = sns.load_dataset('iris')

import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style("whitegrid")
sns.set_context("notebook")

# Datos de ejemplo
x = [1, 2, 3, 4, 5]
y = [5, 7, 9, 6, 8]

# Crear gráfico
sns.lineplot(x=x, y=y)

# Mostrar gráfico
plt.title("Gráfico con estilo whitegrid")
plt.show()





import seaborn as sns

sns.set_palette("deep")

palette = sns.color_palette("bright")
sns.palplot(palette)



custom_palette = sns.color_palette(["#2ecc71", "#e74c3c", "#3498db"])
sns.set_palette(custom_palette)




# Paleta de tonos claros
light_palette = sns.light_palette("navy", as_cmap=True)

# Paleta de tonos oscuros
dark_palette = sns.dark_palette("purple", as_cmap=True)


sns.barplot(x="day", y="total_bill", data=datos, palette="pastel")




import matplotlib.pyplot as plt

sns.set_palette(plt.cm.viridis.colors)


sns.scatterplot(x="sepal_length", y="sepal_width", data=iris, hue="species", palette="Set1_r")


sns.set_palette("colorblind")




import seaborn as sns

sns.set_style("white", {"axes.grid": False, "axes.facecolor": "0.9"})


current_style = sns.axes_style()
print(current_style)



with sns.axes_style("darkgrid"):
    # Código para generar gráficos con el estilo "darkgrid"
    sns.lineplot(x=x_data, y=y_data)





sns.set_context("talk", rc={"lines.linewidth": 2.5})




import matplotlib.pyplot as plt

# Ajustar parámetros de matplotlib directamente
plt.rcParams["axes.labelsize"] = 14
plt.rcParams["axes.titlesize"] = 16

# O mediante seaborn
sns.set_style("ticks", {"xtick.direction": "in", "ytick.direction": "in"})




sns.set_theme(style="whitegrid", palette="pastel")




sns.set_style("darkgrid")
sns.set_context("notebook", rc={"axes.labelweight": "bold", "axes.labelsize": 12})

# Crear gráfico
sns.barplot(x="categoria", y="valor", data=datos)



sns.despine(left=True, bottom=True)




# Configuración general
sns.set_theme(style="ticks", palette="muted", context="paper")

# Gráfico 1
sns.lineplot(x="tiempo", y="variable1", data=datos1)

# Gráfico 2 con estilo personalizado
with sns.axes_style("whitegrid"):
    sns.barplot(x="categoría", y="variable2", data=datos2)
