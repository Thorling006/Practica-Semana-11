import matplotlib.pyplot as plt

# Datos de ejemplo (respuestas de 10 personas)
redes = ['Facebook', 'Instagram', 'TikTok', 'Twitter', 'YouTube']
cantidades = [3, 2, 2, 1, 2]  # número de personas que usan cada una

# Colores opcionales
colores = ['#3b5998', '#C13584', '#69C9D0', '#1DA1F2', '#FF0000']

# Crear gráfico de pastel
plt.figure(figsize=(7, 7))
plt.pie(
    cantidades, 
    labels=redes, 
    colors=colores, 
    autopct='%1.1f%%',  # muestra el porcentaje
    startangle=90,       # inicia el gráfico desde arriba
    shadow=True          # agrega sombra para mejor visualización
)

# Título del gráfico
plt.title('Red social más usada por 10 personas')

# Mostrar gráfico
plt.show()
