import seaborn as sns
import matplotlib.pyplot as plt

# Cargar un conjunto de datos de ejemplo
diamonds = sns.load_dataset("diamonds")

# Crear una cuadrícula de plots segmentada por corte y color de diamante
g = sns.FacetGrid(diamonds, col="cut", row="color", margin_titles=True)
g.map(sns.histplot, "price")
plt.show()



# Cargar datos sobre ejercicios físicos
exercise = sns.load_dataset("exercise")

# Crear una cuadrícula de plots para visualizar la relación entre pulso y tiempo, segmentada por tipo de ejercicio
g = sns.FacetGrid(exercise, col="kind")
g.map(sns.scatterplot, "time", "pulse")
plt.show()




import seaborn as sns
import matplotlib.pyplot as plt

# Cargar un conjunto de datos de ejemplo
tips = sns.load_dataset("tips")


# Crear una cuadrícula de facetas segmentada por día y momento
g = sns.FacetGrid(tips, col="day", row="time")




# Mapear un histograma de la columna 'tip' en la cuadrícula
g.map(sns.histplot, "tip")
plt.show()



# Utilizar map_dataframe para añadir más argumentos
g.map_dataframe(sns.scatterplot, x="total_bill", y="tip")
plt.show()



# Añadir una variable 'sex' como hue
g = sns.FacetGrid(tips, col="day", row="time", hue="sex")
g.map(sns.scatterplot, "total_bill", "tip")
g.add_legend()
plt.show()





# Ajustar el tamaño y el espacio entre las facetas
g = sns.FacetGrid(tips, col="day", row="time", height=3, aspect=1)
g.map(sns.histplot, "tip")
plt.subplots_adjust(hspace=0.4, wspace=0.4)
plt.show()




# Añadir títulos y ajustar escalas
g = sns.FacetGrid(tips, col="day", row="time", margin_titles=True)
g.map(sns.histplot, "tip")
g.set_axis_labels("Propina", "Frecuencia")
g.set_titles(col_template="{col_name}", row_template="{row_name}")
plt.show()






import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el conjunto de datos 'iris'
iris = sns.load_dataset("iris")



# Crear una instancia de PairGrid
g = sns.PairGrid(iris)


# Mapear histogramas en la diagonal
g.map_diag(sns.histplot, color="skyblue")

# Mapear scatterplots en posiciones fuera de la diagonal
g.map_offdiag(sns.scatterplot, color="darkblue")
plt.show()



# Crear PairGrid diferenciando por especie
g = sns.PairGrid(iris, hue="species")

# Mapear funciones de visualización
g.map_diag(sns.kdeplot)
g.map_offdiag(sns.scatterplot)

# Añadir leyenda
g.add_legend()
plt.show()





# Usar violinplot en la diagonal
g = sns.PairGrid(iris, hue="species")
g.map_diag(sns.violinplot)

# Mantener scatterplots fuera de la diagonal
g.map_offdiag(sns.scatterplot)

# Añadir leyenda
g.add_legend()
plt.show()





# Mapear regplot fuera de la diagonal con ajustes personalizados
g = sns.PairGrid(iris, hue="species")
g.map_diag(sns.histplot)
g.map_offdiag(sns.regplot, scatter_kws={"s": 20}, line_kws={"color": "red"})
g.add_legend()
plt.show()




# Crear PairGrid mostrando sólo la esquina inferior
g = sns.PairGrid(iris, hue="species", corner=True)
g.map_lower(sns.scatterplot)
g.map_diag(sns.histplot)
g.add_legend()
plt.show()





# Definir función personalizada para mostrar correlación
def corrfunc(x, y, **kws):
    coef = x.corr(y)
    ax = plt.gca()
    ax.annotate(f"r = {coef:.2f}", xy=(0.1, 0.9), xycoords=ax.transAxes)

# Aplicar función personalizada fuera de la diagonal
g = sns.PairGrid(iris)
g.map_offdiag(corrfunc)
g.map_diag(sns.histplot)
plt.show()



# Personalizar gráficos con títulos y ajustes de espacio
g = sns.PairGrid(iris, hue="species")
g.map_diag(sns.histplot)
g.map_offdiag(sns.scatterplot)
g.add_legend(title="Especie")
g.figure.subplots_adjust(top=0.95)
g.figure.suptitle('Relaciones entre variables en el conjunto de datos Iris', fontsize=16)
plt.show()
