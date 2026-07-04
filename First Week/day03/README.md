# Guía de Trabajo - Clase 3: Regresión Lineal Simple y Múltiple

Este documento proporciona una guía estructurada sobre el contenido y la ejecución de los cuadernos prácticos de la tercera clase del módulo. En esta sesión entraremos formalmente al mundo del Machine Learning Predictivo, dejando atrás la etapa exclusiva de preprocesamiento de datos.

---

## **Estructura de los Cuadernos**

La sesión consta de dos cuadernos de Jupyter diseñados para asimilar teórica y prácticamente la construcción de modelos de Regresión Lineal.

### **1. Cuaderno Principal Guiado: `03_Regresion_Lineal.ipynb`**
*   **Propósito:** Demostrar paso a paso la implementación de modelos predictivos de regresión lineal simple y múltiple utilizando un dataset público de costos de seguros médicos.
*   **Secciones Clave:**
    *   *Preprocesamiento:* Repaso del Día 2 (imputación, One-Hot Encoding, escalado).
    *   *Regresión Simple:* Predicción del costo del seguro utilizando un solo factor (Edad).
    *   *Evaluación:* Comprensión matemática y en código de las métricas de error (RMSE y $R^2$).
    *   *Regresión Múltiple:* Expansión de la ecuación a múltiples factores simultáneos para mejorar dramáticamente la precisión de las predicciones.
    *   *Inferencia de Negocios:* Extracción de los coeficientes algorítmicos para interpretar el impacto económico real de cada variable (por ejemplo, el sobrecosto de ser fumador).

### **2. Cuaderno de Laboratorio (Evaluación): `03_Laboratorio_Evaluacion.ipynb`**
*   **Propósito:** Reto práctico de aplicación autónoma utilizando un dataset del mercado inmobiliario (California Housing).
*   **Requerimientos a desarrollar:**
    *   Extraer los datos directamente desde la web y realizar una auditoría de valores faltantes.
    *   Imputar valores nulos en la columna de número de habitaciones y codificar la variable categórica sobre las cercanías al océano.
    *   Analizar la correlación entre los ingresos per cápita y el valor de las viviendas.
    *   Entrenar y comparar las métricas de desempeño (RMSE y $R^2$) entre un modelo simple y uno múltiple estandarizado.
    *   Extraer los coeficientes matemáticos para concluir teóricamente el impacto de devaluación que sufre una vivienda al ubicarse tierra adentro frente a una vivienda costera.

---

## **Instrucciones de Ejecución para el Estudiante**

1.  **Carga de archivos:** Importar los cuadernos `03_Regresion_Lineal.ipynb` y `03_Laboratorio_Evaluacion.ipynb` a su espacio de **Google Colaboratory** o abrirlos localmente mediante Jupyter Notebook.
2.  **Ejecución Guiada:** Acompañar la exposición del docente ejecutando y comprendiendo secuencialmente el cuaderno guiado de seguros médicos. 
3.  **Resolución de Ejercicios:** En su cuaderno de laboratorio asignado, completar estrictamente el código de Python faltante en los bloques marcados explícitamente con la etiqueta `# TODO`.
4.  **Reporte Final:** Asegurarse de completar las respuestas teóricas requeridas al final del laboratorio evaluativo (Sección 5), argumentando el impacto económico basándose de manera rigurosa en los coeficientes arrojados por el modelo.
