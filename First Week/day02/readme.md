# README / Guía de Trabajo - Clase 2: Preparación de Variables

Este documento sirve como guía oficial y resumen para la segunda sesión del módulo, donde trabajaremos de manera práctica en el cuaderno de Google Colab/Jupyter titulado `02_Preparacion_de_Variables.ipynb`.

---

## **Requisitos Previos (Para Ejecución Local)**

Si decides ejecutar este repositorio en tu máquina local en lugar de la nube (Google Colab), debes asegurarte de cumplir con los siguientes requisitos:

1.  **Soporte de Long Paths en Windows:** Asegúrate de habilitar el soporte para rutas largas en el registro de Windows, ya que Jupyter y sus dependencias lo requieren para su instalación.
2.  **Instalación de Dependencias:** Ejecuta el archivo global de requerimientos que se encuentra en la raíz del módulo utilizando el siguiente comando:
    ```bash
    pip install -r ../requirements.txt --no-cache-dir
    ```
3.  **Lanzamiento del Entorno:** Inicia el servidor de cuadernos ejecutando `jupyter notebook` en la terminal.

---

## **Resumen del Cuaderno de la Clase 2**

El cuaderno `02_Preparacion_de_Variables.ipynb` está enfocado en la **preparación de variables**, el paso más importante y laborioso en el ciclo de vida de los datos antes del entrenamiento de un modelo matemático. A través de este laboratorio, el estudiante pasará por 4 etapas clave:

### **Sección 1: Carga y Exploración de Datos "Sucios"**
*   **Concepto Central:** "Basura entra, basura sale" (*Garbage in, Garbage out*). Un modelo es tan bueno como los datos con los que se alimenta.
*   **Contenido Práctico:** Se ha simulado un conjunto de **100 registros** de clientes con fallas inyectadas intencionalmente (edades imposibles, valores nulos, e ingresos desproporcionados). Se emplea resaltado visual avanzado (`highlight_null`) para auditar la base de datos visualmente.

### **Sección 2: Limpieza de Datos (Data Cleaning)**
*   **Concepto Central:** Estrategias estadísticas de imputación.
*   **Contenido Práctico:**
    *   Uso de estadística descriptiva básica (`.describe()`) para encontrar los valores anómalos.
    *   Filtrado explícito para eliminar filas que carecen de lógica semántica.
    *   **Imputación:** Reemplazo de valores `NaN` utilizando medidas de tendencia central como la Mediana (para evitar el sesgo estadístico por valores atípicos).

### **Sección 3: Ingeniería de Características (Feature Engineering)**
*   **Concepto Central:** Transformación de texto a formato numérico/matricial.
*   **Contenido Práctico:** Explicación y aplicación de **One-Hot Encoding** (*Dummy Variables*) para transformar la columna categórica `Genero` en múltiples columnas binarias, posibilitando el cálculo algebraico.

### **Sección 4: Transformación y Escalado de Variables**
*   **Concepto Central:** Homogeneización de la magnitud de las variables.
*   **Contenido Práctico:**
    *   Explicación e implementación de **Estandarización (Z-Score)** mediante `StandardScaler` de Scikit-Learn para llevar características dispares (Edad e Ingresos) a una media de $0$ y desviación estándar de $1$.
    *   Teoría sobre **Normalización Min-Max** y el ajuste en el rango numérico de $[0, 1]$.

---

## **Requerimientos y Retos para el Estudiante**

Durante el desarrollo del cuaderno, el estudiante deberá completar los fragmentos de código etiquetados con `# TODO`. Específicamente, será evaluado en:
1.  Filtrar un valor atípico de `Ingresos` extremo e imputar los valores faltantes utilizando la media aritmética (*Sección 2*).
2.  Transformar la columna categórica `Pais` utilizando variables *Dummy*, concatenarlas a la matriz central y eliminar las columnas nominales originales (*Sección 3*).
3.  Implementar matemáticamente un objeto `MinMaxScaler` sobre una columna, y comprobar mediante métodos matriciales básicos (`.min()` y `.max()`) su compresión en el rango establecido (*Sección 4*).
