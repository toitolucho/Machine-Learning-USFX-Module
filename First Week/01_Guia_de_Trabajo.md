# Guía de Trabajo - Clase 1: Fundamentos de Machine Learning y Configuración del Entorno

Este documento proporciona una guía estructurada y descriptiva sobre el contenido y la ejecución del cuaderno práctico de la primera clase del módulo, titulado `01_Introduccion_y_Configuracion.ipynb`.

---

## **Estructura General del Cuaderno**

El cuaderno práctico está diseñado para introducir los conceptos teóricos fundamentales de Machine Learning (ML) y habilitar la verificación del entorno de desarrollo mediante Google Colab. Su estructura consta de cuatro secciones clave:

### **Sección 1: Configuración del Entorno e Importación de Librerías**
*   **Propósito:** Garantizar que el entorno de desarrollo cuente con las versiones correctas de las librerías base para la ciencia de datos.
*   **Librerías evaluadas:**
    *   `pandas`: Manipulación de conjuntos de datos en formato tabular.
    *   `numpy`: Operaciones matriciales y de vectores.
    *   `matplotlib`: Generación de gráficos y visualizaciones.
    *   `sklearn`: Implementación de utilidades y modelos de Machine Learning.
*   **Procedimiento:** Se ejecutan de manera secuencial la importación y la impresión directa de las versiones instaladas en el servidor de Google Colab.

### **Sección 2: Delimitación de la IA y Definición de Machine Learning**
*   **Propósito:** Establecer los límites teóricos del aprendizaje automático frente a la inteligencia artificial general y la programación clásica.
*   **Conceptos incluidos:**
    *   Relación jerárquica: Inteligencia Artificial $\supset$ Machine Learning $\supset$ Deep Learning.
    *   Definición según Arthur Samuel (1959).
    *   Definición axiomática según Tom Mitchell (1997), estructurada a través de los componentes **Tarea (T)**, **Experiencia (E)** y **Medida de Rendimiento (P)**.
    *   Diferenciación del paradigma de programación tradicional y del aprendizaje automático.

### **Sección 3: Representación de Datos y Metodología CRISP-DM**
*   **Propósito:** Definir el ciclo de vida estandarizado en la industria para minería de datos y estructurar formalmente las variables de entrada de un modelo de aprendizaje supervisado.
*   **Metodología:** Descripción de las 6 etapas iterativas de la metodología **CRISP-DM** (Comprensión del Negocio, Comprensión de los Datos, Preparación de los Datos, Modelado, Evaluación y Despliegue).
*   **Estructuración de Datos:**
    *   Matriz de Características ($X$): Conjunto de variables independientes descriptoras.
    *   Vector de Etiquetas ($y$): Variable dependiente u objetivo de predicción.
*   **Código de Guía:** Definición paso a paso de un DataFrame clínico simulado y la separación matricial de sus componentes.
*   **Ejercicio Práctico (Requerimiento para el Estudiante):** Desarrollo de un ejercicio autónomo de estructuración de un DataFrame financiero (Aprobación de créditos) y separación de sus características y etiquetas.

### **Sección 4: Validación de Modelos y División de Datos**
*   **Propósito:** Introducir los conceptos de generalización de modelos y evitar el sobreentrenamiento.
*   **Conceptos incluidos:**
    *   *Subajuste (Underfitting)* y *Sobreajuste (Overfitting)*.
    *   *La Regla de Oro:* Separar estrictamente el conjunto de entrenamiento del conjunto de prueba.
*   **Código de Guía:** Aplicación de la función `train_test_split` de Scikit-Learn sobre el dataset de ejemplo médico, con una partición del $70/30$.
*   **Ejercicio Práctico (Requerimiento para el Estudiante):** Aplicación de la división sobre el dataset financiero del ejercicio anterior reservando el $20\%$ de los datos para pruebas, con semilla aleatoria `random_state=123`.

---

## **Instrucciones de Ejecución para el Estudiante**

1.  **Carga del archivo:** Importar el archivo `01_Introduccion_y_Configuracion.ipynb` a su espacio personal en Google Drive y abrirlo utilizando el entorno de **Google Colaboratory**.
2.  **Ejecución Secuencial:** Ejecutar las celdas de código en el orden estrictamente establecido.
3.  **Resolución de Ejercicios:** Completar el código faltante en los bloques marcados con la etiqueta `# TODO`.
4.  **Entrega y Verificación:** Confirmar que los resultados de salida de las dimensiones matriciales impresas mediante la propiedad `.shape` coincidan de forma exacta con los requerimientos asignados.
