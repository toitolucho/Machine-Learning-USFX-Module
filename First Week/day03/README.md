# Día 3: Regresión Lineal Simple y Múltiple

Bienvenidos al tercer día del Módulo 4 del Diplomado en Ciencia de Datos. En esta sesión, los estudiantes darán el gran salto metodológico: dejarán atrás la etapa exclusiva de preprocesamiento de datos e ingresarán formalmente al mundo del **Machine Learning Predictivo**, entrenando, evaluando e interpretando sus primeros algoritmos de aprendizaje supervisado.

---

## Estructura del Directorio

Esta carpeta consolida de forma ordenada todo el ecosistema de aprendizaje preparado para la sesión 3:

### 1. Material de Clase (Exposición Docente)
- **`03_Presentacion_Clase.tex`**: Código fuente LaTeX para la presentación formal. Explica de manera muy didáctica (sin terminología excesivamente abstracta) los conceptos de regresión simple, múltiple, evaluación (RMSE/$R^2$) y uso de la librería de scikit-learn.
- **`generar_graficas.py`**: Utilidad de Python que descarga datos reales y genera las imágenes PNG (`grafica_simple.png` y `grafica_multiple.png`). **Nota Docente:** Debe ejecutar este script antes de compilar el archivo `.tex`.

### 2. Cuaderno Principal Guiado (Hands-On)
- **`03_Regresion_Lineal.ipynb`**: Cuaderno Jupyter (estilo Databricks) enfocado en estimar **Cargos de Seguros Médicos**. Combina teoría continua, celdas de reto `# TODO` para que apliquen el preprocesamiento aprendido el Día 2, y bloques de código explicados *paso a paso* para la regresión algorítmica.
- **`03_Guia_de_Trabajo_Soluciones.md`**: Su hoja de trucos. Contiene los fragmentos de código, sugerencias pedagógicas (como el uso de analogías) y las respuestas a las discusiones teóricas de los alumnos.

### 3. Laboratorio de Evaluación (Asignación Estudiantil)
- **`03_Laboratorio_Evaluacion.ipynb`**: Reto autónomo utilizando el clásico dataset de **Valuación Inmobiliaria en California**. El alumno se enfrenta a datos crudos en línea y debe aplicar el ciclo completo de vida del dato para predecir precios de viviendas.
- **`03_Soluciones_Laboratorio.md`**: Solucionario completo del laboratorio inmobiliario. Incluye justificaciones sobre la inferencia analítica (el gigantesco impacto económico que detecta el modelo cuando una casa se aleja de la costa).

---

## Dinámica Pedagógica Sugerida
1. Ejecute `generar_graficas.py` y compile la presentación. Exponga los cimientos teóricos y matemáticos utilizando el archivo PDF resultante.
2. Intercale la teoría con el cuaderno `03_Regresion_Lineal.ipynb`. Deje que los estudiantes completen de memoria el bloque 1 (preprocesamiento) y guíelos en los bloques posteriores (entrenamiento algorítmico e inferencia monetaria).
3. Entregue el cuaderno `03_Laboratorio_Evaluacion.ipynb` como asignación evaluativa o de fin de clase para confirmar la aprehensión del modelo lineal múltiple.
