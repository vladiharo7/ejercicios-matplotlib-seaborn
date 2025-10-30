import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [10, 20, 25, 30])
ax.set_title("Título del gráfico")
# ax.set_title("Título del gráfico", fontdict={'fontsize': 14, 'fontweight': 'bold'})
# ax.set_title("Título del gráfico", loc='left')
# ax.set_title("Título del gráfico", color='red', style='italic')
# ax.set_title("Título del gráfico", pad=20)
# ax.set_title(r"Expresión matemática: $E=mc^2$")


plt.show()



fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [10, 20, 25, 30])
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")

ax.annotate('Punto importante', xy=(3, 25), xytext=(3, 30),
            arrowprops=dict(facecolor='black', shrink=0.05))

ax.text(2, 15, "Texto libre", fontsize=12, color='blue')

ax.set_xlabel(r"Eje X ($\mu m$)")
ax.annotate(r'$\alpha > \beta$', xy=(1.2, 10), fontsize=12)


plt.show()




import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [10, 20, 25, 30], label='Serie 1')
ax.plot([1, 2, 3, 4], [30, 25, 20, 15], label='Serie 2')
ax.legend()
ax.legend(loc='upper right')
ax.legend(loc='upper right', fontsize='small', ncol=2)
ax.legend(frameon=False, shadow=True)
ax.legend(title='Datos de ejemplo')
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper left')


plt.show()
