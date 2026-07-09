# Guía de Trabajo - Clase 5: Taller Comparativo de Clasificadores

Este documento proporciona la guía para la quinta clase del módulo. Habiendo dominado la Regresión Logística, hoy expandiremos nuestro arsenal de Machine Learning a tres algoritmos de clasificación radicalmente distintos: **k-NN, Árboles de Decisión y Naive Bayes**.

---

## **Estructura de los Cuadernos**

La sesión está diseñada como un taller de experimentación donde los alumnos podrán comparar cómo "piensa" cada algoritmo de inteligencia artificial.

### **1. Cuaderno Principal Guiado: `05_Comparacion_Clasificadores.ipynb`**
*   **Propósito:** Enseñar la matemática e intuición detrás de los tres modelos utilizando un dataset de **Clasificación de Vinos (Calidad)**.
*   **Secciones Clave:**
    *   *k-Nearest Neighbors (k-NN):* El modelo "Perezoso". Aprenderemos por qué es obligatorio escalar (estandarizar) los datos para que el algoritmo calcule distancias geométricas correctas.
    *   *Árboles de Decisión:* El modelo "Basado en Reglas". Estudiaremos conceptos como Entropía y la trampa del Sobreajuste (Overfitting).
    *   *Naive Bayes:* El modelo "Probabilístico". Entenderemos por qué asumir independencia (Teorema de Bayes) lo hace increíblemente rápido.
    *   *Comparación Directa:* Enfrentaremos los 3 algoritmos y compararemos sus métricas de Exactitud.

### **2. Cuaderno de Laboratorio (Evaluación): `05_Laboratorio_Evaluacion.ipynb`**
*   **Propósito:** Reto médico crítico utilizando un dataset de **Diagnóstico de Cáncer de Mama (Wisconsin)**.
*   **Requerimientos a desarrollar:**
    *   Preprocesar y estandarizar datos oncológicos.
    *   Entrenar los 3 algoritmos en solitario.
    *   Comparar métricas y analizar cuál modelo comete menos "Falsos Negativos" (el error de decirle a alguien que tiene cáncer maligno que está sano).
    *   **Evaluación de Negocio:** Justificar analíticamente cuál modelo se debería implementar en el hospital.

---

## **Instrucciones de Ejecución para el Estudiante**

1.  **Carga de archivos:** Importar los cuadernos `05_Comparacion_Clasificadores.ipynb` y `05_Laboratorio_Evaluacion.ipynb` a su entorno de **Google Colaboratory**.
2.  **Ejecución Guiada:** Acompañar la exposición del docente, prestando especial atención a cómo cada modelo genera fronteras de decisión diferentes en los datos de los vinos.
3.  **Resolución de Ejercicios:** En su cuaderno de laboratorio asignado, completar el código faltante en los bloques `# TODO` para los tres modelos.
4.  **Reporte Final:** En la celda designada al final del laboratorio, justificar médicamente la elección de su modelo apoyándose estricta y únicamente en las métricas de Sensibilidad (Recall) y la Matriz de Confusión.
