from sklearn.linear_model import LinearRegression
import numpy as np

# Datos: [Metros cuadrados] -> [Precio en miles]

X = np.array ([[50],[70],[80],[100],[120]])
y = np.array ([150,200,210,250,280])

# Creamos el modelo y lo entrenamos

modelo = LinearRegression()
modelo.fit(X,y)

# ¿Cuánto valdría una casa de 90m2?
nueva_casa = np.array([[90]])
prediccion = modelo.predict(nueva_casa)

print(f"Precio estimado: $ {prediccion[0]:.2f}k")

