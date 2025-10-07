import matplotlib.pyplot as plt

# Datos de ejemplo (respuestas de 10 personas)
# Minutos que tardan en llegar a la universidad
tiempos = [15, 20, 25, 30, 10, 35, 40, 20, 25, 15]

# Crear el histograma
plt.figure(figsize=(8, 6))
plt.hist(
    tiempos, 
    bins=5,                # número de barras (puedes ajustarlo)
    color='skyblue',       # color de las barras
    edgecolor='black'      # borde negro para distinguir mejor
)

# Títulos y etiquetas
plt.title('Tiempo para llegar a la universidad (muestra de 10 personas)')
plt.xlabel('Minutos')
plt.ylabel('Cantidad de personas')

# Mostrar el gráfico
plt.show()
