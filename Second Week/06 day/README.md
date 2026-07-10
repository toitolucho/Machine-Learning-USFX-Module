# Guía de Trabajo - Clase 6: Mini Proyecto y Pipelines en Scikit-Learn

Este documento delinea los objetivos y la estructura de la sexta clase del módulo. El propósito central de esta sesión es la transición de la experimentación manual al desarrollo estructurado mediante **Pipelines**.

---

## **Objetivos de la Sesión**

1.  Comprender el concepto de *Data Leakage* (fuga de datos) y cómo la ejecución manual de preprocesamientos incrementa este riesgo.
2.  Estructurar flujos de trabajo profesionales utilizando la clase `Pipeline` de la librería `scikit-learn`.
3.  Empaquetar el proceso de Imputación de datos nulos, Escalado de características y Modelado Predictivo en un único objeto secuencial.

---

## **Estructura de los Cuadernos**

### **1. Cuaderno Principal Guiado: `06_Pipelines_Mini_Proyecto.ipynb`**
*   **Propósito:** Demostración práctica de la construcción de una línea de ensamblaje (Pipeline). Se utilizará el dataset de supervivencia del **Titanic** dado que presenta datos faltantes (nulos), lo cual justifica la inclusión de una etapa de imputación.
*   **Contenido:**
    *   Exposición de la problemática del preprocesamiento segmentado.
    *   Definición de las etapas (estaciones) del pipeline: `SimpleImputer`, `StandardScaler` y el modelo predictor.
    *   Ensamblaje y ejecución centralizada mediante el método `.fit()`.

### **2. Cuaderno de Laboratorio (Evaluación): `06_Laboratorio_Evaluacion.ipynb`**
*   **Propósito:** Ejercicio de aplicación autónoma. Se evaluará la capacidad del estudiante para construir un pipeline completo desde cero.
*   **Contenido:**
    *   Dataset diagnóstico orientado a la predicción de **Diabetes**, el cual contiene valores nulos pre-inyectados.
    *   El estudiante deberá estructurar un Pipeline que contenga al menos tres fases secuenciales, justificando la inclusión de cada una.
