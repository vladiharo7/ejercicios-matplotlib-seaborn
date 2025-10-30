import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


fig, axs = plt.subplots(2, 2)

for ax in axs.flat:
    ax.grid(True)

fig, axs = plt.subplots(2, 3)

plt.subplots_adjust(wspace=0.4, hspace=0.6)



gs = gridspec.GridSpec(3, 3)
ax1 = plt.subplot(gs[0, :])
ax2 = plt.subplot(gs[1, :-1])
ax3 = plt.subplot(gs[1:, -1])
ax4 = plt.subplot(gs[-1, 0])
ax5 = plt.subplot(gs[-1, -2])




fig = plt.figure(constrained_layout=True)
gs = gridspec.GridSpec(2, 2, figure=fig)
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[1, :])

ax1.plot([1, 2, 3], [4, 5, 6])
ax2.plot([1, 2, 3], [6, 5, 4])
ax3.plot([1, 2, 3], [5, 5, 5])

plt.show()



# Listar todos los estilos disponibles
print(plt.style.available)



# Aplicar un tema predefinido
plt.style.use('ggplot')

# Personalizar parámetros de estilo
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelsize'] = 12

plt.plot([1, 2, 3], [4, 5, 6], color='red')  # Usando nombre de color
plt.plot([1, 2, 3], [6, 5, 4], color='#FF5733')  # Usando código hexadecimal
plt.show()

plt.plot([1, 2, 3], [4, 5, 6], color=(0.1, 0.2, 0.5))  # RGB
plt.plot([1, 2, 3], [6, 5, 4], color=(0.1, 0.2, 0.5, 0.3))  # RGBA
plt.show()



import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Crear un generador de números aleatorios con una semilla específica
rng = np.random.default_rng(seed=42)

# Generación de datos aleatorios
data = rng.random((10, 10))

# Creación del heatmap utilizando el colormap 'viridis'
plt.imshow(data, cmap=cm.viridis)  # Usando un colormap predefinido
plt.colorbar()  # Agrega una barra de color para referencia
plt.show()


from matplotlib.colors import LinearSegmentedColormap

custom_cmap = LinearSegmentedColormap.from_list('custom_cmap', ['red', 'blue', 'green'])
plt.imshow(data, cmap=custom_cmap)
plt.colorbar()
plt.show()

# Aplicar un estilo predefinido válido
plt.style.use('ggplot')

# Graficar con el estilo aplicado
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()

# Personalizar estilo ajustando parámetros rcParams
plt.rcParams['lines.linewidth'] = 2.5
plt.rcParams['lines.markersize'] = 8

plt.plot([1, 2, 3], [4, 5, 6], marker='o')
plt.show()


# Contenido de un archivo custom.mplstyle
"""
axes.titlesize : 16
axes.labelsize : 14
lines.linewidth : 3
lines.markersize : 10
"""

# Aplicar el estilo personalizado
#plt.style.use('custom.mplstyle')

#plt.plot([1, 2, 3], [4, 5, 6], marker='s')
#plt.show()
