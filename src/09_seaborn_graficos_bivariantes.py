import seaborn as sns
import matplotlib.pyplot as plt

datos = sns.load_dataset('tips')

sns.scatterplot(data=datos, x='total_bill', y='tip')
plt.show()




import seaborn as sns
import matplotlib.pyplot as plt

datos = sns.load_dataset('iris')

sns.scatterplot(data=datos, x='petal_length', y='petal_width')
plt.show()


sns.scatterplot(data=datos, x='petal_length', y='petal_width', hue='species')
plt.show()



sns.scatterplot(data=datos, x='petal_length', y='petal_width', hue='species', size='sepal_width', style='species')
plt.show()



sns.scatterplot(data=datos, x='petal_length', y='petal_width', alpha=0.7)
plt.show()



sns.scatterplot(data=datos, x='petal_length', y='petal_width', hue='species', palette='Set2')
plt.show()



sns.scatterplot(data=datos, x='petal_length', y='petal_width', hue='species')
plt.xlabel('Longitud del pétalo')
plt.ylabel('Ancho del pétalo')
plt.title('Relación entre longitud y ancho del pétalo por especie')
plt.show()





import seaborn as sns
import matplotlib.pyplot as plt

datos = sns.load_dataset('fmri')


sns.lineplot(data=datos, x='timepoint', y='signal')
plt.show()


sns.lineplot(data=datos, x='timepoint', y='signal', hue='event')
plt.show()


sns.lineplot(data=datos, x='timepoint', y='signal', hue='event', style='region')
plt.show()


sns.lineplot(data=datos, x='timepoint', y='signal', hue='event', errorbar='sd')
plt.show()


sns.lineplot(data=datos, x='timepoint', y='signal', hue='event', errorbar=None)
plt.show()



sns.lineplot(data=datos, x='timepoint', y='signal', hue='event', style='region')
plt.xlabel('Tiempo')
plt.ylabel('Señal')
plt.title('Actividad neuronal por evento y región')
plt.legend(title='Evento', loc='upper right')
plt.show()


sns.lineplot(data=datos, x='timepoint', y='signal', hue='event', palette='dark')
plt.show()




datos_vuelos = sns.load_dataset('flights')




sns.lineplot(data=datos_vuelos, x='year', y='passengers')
plt.xlabel('Año')
plt.ylabel('Pasajeros')
plt.title('Tendencia anual de pasajeros aéreos')
plt.show()



sns.lineplot(data=datos_vuelos, x='month', y='passengers', hue='year', palette='coolwarm')
plt.xlabel('Mes')
plt.ylabel('Pasajeros')
plt.title('Pasajeros aéreos por mes y año')
plt.legend(title='Año', bbox_to_anchor=(1.05, 1), loc=2)
plt.show()




import seaborn as sns
import matplotlib.pyplot as plt

datos_vuelos = sns.load_dataset('flights')


tabla_pivote = datos_vuelos.pivot(index='month', columns='year', values='passengers')


sns.heatmap(tabla_pivote)
plt.show()


sns.heatmap(tabla_pivote, annot=True, fmt='d')
plt.show()


sns.heatmap(tabla_pivote, cmap='YlGnBu', annot=True, fmt='d')
plt.show()


media_pasajeros = datos_vuelos['passengers'].mean()
sns.heatmap(tabla_pivote, cmap='coolwarm', center=media_pasajeros, annot=True, fmt='d')
plt.show()





tabla_pivote_normalizada = tabla_pivote.div(tabla_pivote.sum(axis=0), axis=1)
sns.heatmap(tabla_pivote_normalizada, cmap='viridis')
plt.show()






import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

datos_propinas = sns.load_dataset('tips')

# Seleccionar solo las columnas numéricas
matriz_correlacion = datos_propinas.select_dtypes(include=[np.number]).corr()
sns.heatmap(matriz_correlacion, annot=True, cmap='coolwarm')
plt.show()

mascara = np.triu(np.ones_like(matriz_correlacion, dtype=bool))
sns.heatmap(matriz_correlacion, annot=True, cmap='coolwarm', mask=mascara)
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.show()




import seaborn as sns
import matplotlib.pyplot as plt

datos = sns.load_dataset('tips')

sns.catplot(data=datos, x='day', y='tip', hue='sex', kind='bar', errorbar=None)
plt.ylabel('Propina promedio')
plt.title('Propina promedio por día y sexo')
plt.show()



sns.catplot(data=datos, x='day', y='tip', hue='sex', kind='bar', errorbar=None, palette='Set2')
plt.ylabel('Propina promedio')
plt.title('Propina promedio por día y sexo')
plt.show()




tabla_pivot = datos.pivot_table(values='tip', index='day', columns='sex', aggfunc='sum', observed=False)


tabla_pivot.plot(kind='bar', stacked=True, color=['#ff9999','#66b3ff'])
plt.ylabel('Propina total')
plt.title('Propina total por día y sexo (apilado)')
plt.legend(title='Sexo')
plt.xticks(rotation=0)
plt.show()



ax = tabla_pivot.plot(kind='bar', stacked=True, color=['#ff9999','#66b3ff'])
plt.ylabel('Propina total')
plt.title('Propina total por día y sexo (apilado)')
plt.legend(title='Sexo')
plt.xticks(rotation=0)

for container in ax.containers:
    ax.bar_label(container, fmt='%.2f', label_type='center')

plt.show()



tabla_porcentajes = tabla_pivot.div(tabla_pivot.sum(axis=1), axis=0)

ax = tabla_porcentajes.plot(kind='bar', stacked=True, color=['#ff9999','#66b3ff'])
plt.ylabel('Proporción de propinas')
plt.title('Proporción de propinas por día y sexo')
plt.legend(title='Sexo')
plt.xticks(rotation=0)

for container in ax.containers:
    labels = [f'{v.get_height()*100:.1f}%' for v in container]
    ax.bar_label(container, labels=labels, label_type='center')

plt.show()






sns.barplot(data=datos, x='day', y='tip', estimator=sum, errorbar=None, color='lightblue')
plt.ylabel('Propina total')
plt.title('Propina total por día')
plt.show()






sns.set_style('whitegrid')

sns.catplot(data=datos, x='day', y='total_bill', hue='sex', kind='bar', errorbar=None, palette='muted')
plt.ylabel('Cuenta total promedio')
plt.title('Cuenta total promedio por día y sexo')
plt.show()






dias = ['Thur', 'Fri', 'Sat', 'Sun']

sns.catplot(data=datos, x='day', y='tip', hue='sex', kind='bar', errorbar=None, order=dias)
plt.ylabel('Propina promedio')
plt.title('Propina promedio por día ordenado')
plt.show()





import seaborn as sns
import matplotlib.pyplot as plt

datos = sns.load_dataset('tips')



sns.regplot(data=datos, x='total_bill', y='tip')
plt.xlabel('Total de la cuenta')
plt.ylabel('Propina')
plt.title('Relación entre la cuenta y la propina')
plt.show()




sns.residplot(data=datos, x='total_bill', y='tip')
plt.xlabel('Total de la cuenta')
plt.ylabel('Residuo')
plt.title('Análisis de residuos')
plt.show()



sns.lmplot(data=datos, x='total_bill', y='tip', hue='sex')
plt.xlabel('Total de la cuenta')
plt.ylabel('Propina')
plt.title('Propina vs. cuenta por sexo')
plt.show()




sns.lmplot(data=datos, x='total_bill', y='tip', hue='sex', col='smoker')
plt.xlabel('Total de la cuenta')
plt.ylabel('Propina')
plt.suptitle('Propina vs. cuenta por sexo y hábito de fumar')
plt.tight_layout()
plt.show()






import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

datos = sns.load_dataset('tips')

# Crear gráfico de dispersión
sns.scatterplot(data=datos, x='total_bill', y='tip')
plt.xlabel('Total de la cuenta')
plt.ylabel('Propina')
plt.title('Propina vs. Total de la cuenta')

# Calcular línea de regresión
slope, intercept, r_value, p_value, std_err = stats.linregress(datos['total_bill'], datos['tip'])
x = np.linspace(datos['total_bill'].min(), datos['total_bill'].max(), 100)
y = intercept + slope * x

# Añadir línea de regresión
plt.plot(x, y, color='red')
plt.show()



sns.regplot(data=datos, x='total_bill', y='tip', order=2)
plt.xlabel('Total de la cuenta')
plt.ylabel('Propina')
plt.title('Regresión polinomial de grado 2')
plt.show()





sns.regplot(data=datos, x='total_bill', y='tip', robust=True)
plt.xlabel('Total de la cuenta')
plt.ylabel('Propina')
plt.title('Regresión lineal robusta')
plt.show()








sns.jointplot(data=datos, x='total_bill', y='tip', kind='reg')
plt.show()



# Suponiendo que tenemos una variable binaria 'alta_propina'
datos['alta_propina'] = (datos['tip'] > datos['tip'].median()).astype(int)

sns.regplot(data=datos, x='total_bill', y='alta_propina', logistic=True, scatter_kws={'alpha':0.3})
plt.xlabel('Total de la cuenta')
plt.ylabel('Probabilidad de alta propina')
plt.title('Regresión logística')
plt.show()
