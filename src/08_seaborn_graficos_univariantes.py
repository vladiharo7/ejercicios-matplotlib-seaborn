import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el conjunto de datos
df = sns.load_dataset('tips')

# Crear un histograma de la variable 'total_bill'
sns.histplot(data=df, x='total_bill')

# Especificar el número de bins
sns.histplot(data=df, x='total_bill', bins=20)

# Mostrar la densidad en el eje y
sns.histplot(data=df, x='total_bill', stat='density')

# Añadir una curva KDE al histograma
sns.histplot(data=df, x='total_bill', kde=True)

# Histograma con diferenciación por sexo
sns.histplot(data=df, x='total_bill', hue='sex', multiple='stack')

# Colocar las barras de categorías lado a lado
sns.histplot(data=df, x='total_bill', hue='sex', multiple='dodge')

# Personalizar color y transparencia
sns.histplot(data=df, x='total_bill', color='teal', alpha=0.6)

# Histograma bidimensional entre 'total_bill' y 'tip'
sns.histplot(data=df, x='total_bill', y='tip')



plt.xlabel('Total de la factura')
plt.ylabel('Frecuencia')
plt.title('Distribución del total de las facturas')
plt.show()


# Configurar el estilo del gráfico
sns.set_style('whitegrid')

sns.histplot(data=df, x='total_bill', kde=True, color='purple')
plt.xlabel('Total de la factura')
plt.ylabel('Frecuencia')
plt.title('Histograma del total de las facturas con KDE')
plt.show()

# Añadir un rug plot al histograma
sns.histplot(data=df, x='total_bill', kde=True, color='coral')
sns.rugplot(data=df, x='total_bill', color='black')






import seaborn as sns
import matplotlib.pyplot as plt

# Cargar un conjunto de datos de ejemplo
df = sns.load_dataset('tips')

# Crear un diagrama de caja y bigotes de la variable 'total_bill'
sns.boxplot(data=df, x='total_bill')

plt.xlabel('Total de la factura')
plt.title('Diagrama de caja y bigotes del total de las facturas')
plt.show()




# Diagrama de caja y bigotes del total de facturas por día
sns.boxplot(data=df, x='day', y='total_bill')

plt.xlabel('Día de la semana')
plt.ylabel('Total de la factura')
plt.title('Total de las facturas por día de la semana')
plt.show()



# Diagrama de caja y bigotes con diferenciación por tiempo de comida
sns.boxplot(data=df, x='day', y='total_bill', hue='time')

plt.xlabel('Día de la semana')
plt.ylabel('Total de la factura')
plt.title('Total de las facturas por día y tiempo de comida')
plt.legend(title='Tiempo de comida')
plt.show()

# Boxplot horizontal de la variable 'tip'
sns.boxplot(data=df, x='tip')

plt.xlabel('Propina')
plt.title('Diagrama de caja y bigotes de las propinas')
plt.show()


# Personalizar colores con una paleta
sns.boxplot(data=df, x='day', y='total_bill', palette='Set2', hue='day', dodge=False)
plt.legend([],[], frameon=False) 

plt.xlabel('Día de la semana')
plt.ylabel('Total de la factura')
plt.title('Total de las facturas por día con colores personalizados')
plt.show()



# Ajustar el ancho de las cajas y tamaño de los valores atípicos
sns.boxplot(data=df, x='day', y='total_bill', width=0.5, fliersize=4)

plt.xlabel('Día de la semana')
plt.ylabel('Total de la factura')
plt.title('Boxplot ajustado del total de las facturas')
plt.show()


# Combinar boxplot con swarmplot
sns.boxplot(data=df, x='day', y='total_bill', color='lightgray')
sns.swarmplot(data=df, x='day', y='total_bill', color='steelblue', size=3)

plt.xlabel('Día de la semana')
plt.ylabel('Total de la factura')
plt.title('Boxplot y swarmplot combinados del total de las facturas')
plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

# Cargar un conjunto de datos de ejemplo
df = sns.load_dataset('tips')

# Crear un gráfico de violín de la variable 'total_bill'
sns.violinplot(data=df, x='total_bill')

plt.xlabel('Total de la factura')
plt.title('Gráfico de violín del total de las facturas')
plt.show()




# Gráfico de violín del total de facturas por día
sns.violinplot(data=df, x='day', y='total_bill')

plt.xlabel('Día de la semana')
plt.ylabel('Total de la factura')
plt.title('Total de las facturas por día de la semana')
plt.show()




# Gráfico de violín con diferenciación por sexo
sns.violinplot(data=df, x='day', y='total_bill', hue='sex', split=True)

plt.xlabel('Día de la semana')
plt.ylabel('Total de la factura')
plt.title('Total de las facturas por día y sexo')
plt.legend(title='Sexo')
plt.show()




# Personalizar el interior del gráfico de violín
sns.violinplot(data=df, x='day', y='total_bill', inner='quartile')

plt.xlabel('Día de la semana')
plt.ylabel('Total de la factura')
plt.title('Gráfico de violín con cuartiles del total de las facturas')
plt.show()




# Ajustar la escala de los violines
sns.violinplot(data=df, x='day', y='total_bill', density_norm='count')

plt.xlabel('Día de la semana')
plt.ylabel('Total de la factura')
plt.title('Gráfico de violín escalado por recuento')
plt.show()





# Combinar gráfico de violín con stripplot
sns.violinplot(data=df, x='day', y='total_bill', color='lightgray')
sns.stripplot(data=df, x='day', y='total_bill', color='black', size=3)

plt.xlabel('Día de la semana')
plt.ylabel('Total de la factura')
plt.title('Gráfico de violín con observaciones individuales')
plt.show()






# Gráfico de violín con orientación horizontal
sns.violinplot(data=df, x='total_bill', y='day')

plt.xlabel('Total de la factura')
plt.ylabel('Día de la semana')
plt.title('Gráfico de violín horizontal del total de las facturas')
plt.show()





import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el conjunto de datos 'fmri'
df = sns.load_dataset('fmri')

# Crear una gráfica de línea básica
sns.lineplot(data=df, x='timepoint', y='signal')

plt.xlabel('Punto en el tiempo')
plt.ylabel('Señal')
plt.title('Evolución de la señal cerebral a lo largo del tiempo')
plt.show()





# Gráfica de línea diferenciada por región
sns.lineplot(data=df, x='timepoint', y='signal', hue='region')

plt.xlabel('Punto en el tiempo')
plt.ylabel('Señal')
plt.title('Señal cerebral por región a lo largo del tiempo')
plt.legend(title='Región')
plt.show()





# Gráfica de línea con diferenciación adicional por evento
sns.lineplot(data=df, x='timepoint', y='signal', hue='region', style='event', markers=True)

plt.xlabel('Punto en el tiempo')
plt.ylabel('Señal')
plt.title('Señal cerebral por región y evento')
plt.legend(title='Región - Evento')
plt.show()







# Gráfica de línea con intervalos de confianza
sns.lineplot(data=df, x='timepoint', y='signal', hue='region', errorbar='sd')

plt.xlabel('Punto en el tiempo')
plt.ylabel('Señal')
plt.title('Señal cerebral con desviación estándar por región')
plt.legend(title='Región')
plt.show()








# Mostrar todas las observaciones individuales
sns.lineplot(data=df, x='timepoint', y='signal', hue='region', estimator=None, units='subject', lw=1)

plt.xlabel('Punto en el tiempo')
plt.ylabel('Señal')
plt.title('Trayectorias individuales de la señal cerebral por región')
plt.legend(title='Región')
plt.show()









# Personalizar la paleta de colores y estilos de línea
sns.lineplot(data=df, x='timepoint', y='signal', hue='region', style='event', palette='tab10', dashes=False)

plt.xlabel('Punto en el tiempo')
plt.ylabel('Señal')
plt.title('Señal cerebral con estilos personalizados')
plt.legend(title='Región - Evento')
plt.show()








# Ajustar el estilo general de la gráfica
sns.set(style='whitegrid')

sns.lineplot(data=df, x='timepoint', y='signal', hue='region', style='event', markers=True)

plt.xlabel('Punto en el tiempo')
plt.ylabel('Señal')
plt.title('Análisis de la señal cerebral por región y evento')
plt.legend(title='Región - Evento')
plt.show()

