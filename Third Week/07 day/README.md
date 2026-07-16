# Día 07: Modelos de Ensamble (La Sabiduría Colectiva)

Bienvenido al Día 07 del Diplomado en Ciencia de Datos. Durante esta sesión, daremos el salto evolutivo más importante en el aprendizaje automático supervisado: dejar de confiar en un solo modelo y comenzar a utilizar **Ensambles**.

## Estructura de la Sesión

1.  **`07_Ensambles_Guiado.ipynb` (Cuaderno Principal):** 
    En esta guía paso a paso, abordaremos un problema clásico corporativo: **La Retención de Clientes (Customer Churn)**. Aprenderemos cómo combinar la fuerza de múltiples Árboles de Decisión utilizando dos estrategias fundamentales:
    *   **Bagging (Random Forest):** Entrenar cientos de modelos en paralelo para reducir la varianza (votar de forma democrática).
    *   **Boosting (Gradient Boosting / XGBoost):** Entrenar modelos secuencialmente para reducir el sesgo (aprender de los errores del anterior).
2.  **`07_Laboratorio_Evaluacion.ipynb` (Reto Autónomo):** 
    Un desafío crítico del sector financiero: **Detección de Fraude con Tarjetas de Crédito**. Te enfrentarás a un dataset altamente desbalanceado donde cada Falso Negativo cuesta dinero. Deberás optimizar un modelo de Ensamble y defender tus decisiones de negocio.

## Requisitos
Asegúrate de haber instalado las dependencias más recientes para esta sesión:
*   `pip install scikit-learn pandas matplotlib seaborn xgboost`

¡Comencemos!
