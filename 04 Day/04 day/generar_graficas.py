import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, LogisticRegression
import os

# Crear directorio si no existe (opcional, en este caso guarda localmente)
output_dir = "imagenes_latex"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 1. Gráfica de por qué la regresión lineal falla en clasificación
np.random.seed(42)
X_lin = np.linspace(0, 10, 20).reshape(-1, 1)
y_lin = np.where(X_lin > 5, 1, 0).ravel()

model_lin = LinearRegression()
model_lin.fit(X_lin, y_lin)
X_test = np.linspace(-2, 12, 100).reshape(-1, 1)
y_pred_lin = model_lin.predict(X_test)

plt.figure(figsize=(8, 5))
plt.scatter(X_lin, y_lin, color='red', label='Datos (Clase 0 y 1)', zorder=5)
plt.plot(X_test, y_pred_lin, color='blue', label='Regresión Lineal', linewidth=2)
plt.axhline(1, color='gray', linestyle='--')
plt.axhline(0, color='gray', linestyle='--')
plt.axvline(5, color='green', linestyle=':', label='Frontera ideal')
plt.title("Falla de la Regresión Lineal en Clasificación Binaria", fontsize=14)
plt.xlabel("Característica (X)")
plt.ylabel("Probabilidad (Y)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig(os.path.join(output_dir, "linear_vs_logistic.png"), dpi=300, bbox_inches='tight')
plt.close()

# 2. Gráfica de la Función Sigmoide pura
def sigmoide(z):
    return 1 / (1 + np.exp(-z))

z = np.linspace(-10, 10, 200)
phi = sigmoide(z)

plt.figure(figsize=(8, 5))
plt.plot(z, phi, color='purple', linewidth=3, label=r'Función Sigmoide $\sigma(z)$')
plt.axhline(0.5, color='red', linestyle='--', label='Umbral (0.5)')
plt.axvline(0, color='black', linewidth=1)
plt.axhline(0, color='black', linewidth=1)
plt.axhline(1.0, color='gray', linestyle=':')
plt.axhline(0.0, color='gray', linestyle=':')
plt.yticks([0.0, 0.5, 1.0])
plt.title("La Función Sigmoide", fontsize=14)
plt.xlabel("z")
plt.ylabel(r"$\sigma(z)$")
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig(os.path.join(output_dir, "funcion_sigmoide.png"), dpi=300, bbox_inches='tight')
plt.close()

print("Imágenes generadas correctamente en la carpeta 'imagenes_latex'.")

# Forzar descarga automática si estamos en Google Colab
try:
    from google.colab import files
    print("Iniciando descarga automática de las imágenes...")
    files.download(os.path.join(output_dir, "linear_vs_logistic.png"))
    files.download(os.path.join(output_dir, "funcion_sigmoide.png"))
except ImportError:
    pass
