**Prompt/Guide for AI Agent: Google Colab Exercise Generation for Class 1 (Foundations & Setup)**

**Context & Objective (For the AI Agent):**
Your task is to generate a comprehensive Python notebook designed to be executed in Google Colab. This notebook is for the 1st class of a Machine Learning module, focusing on "Artificial Intelligence Map, Foundations of ML, and Environment Setup". The output you generate must include executable Python code blocks, explanatory text (in Spanish, as the course is in Spanish), and expected outputs. The focus is on introducing the environment, basic data structures, and the theoretical concepts of ML.

**Target Audience (For the Teacher and Students):**
*   **Teacher:** Use this guide to ensure students understand the difference between AI, ML, and Data Science, and that their Google Colab environments are correctly configured with the necessary libraries.
*   **Students:** This is your introductory laboratory. You will learn how to navigate Google Colab, import standard ML libraries, understand how data is represented, and learn the fundamental terminology of Machine Learning.

---

### **Section 1: Workspace Configuration and Library Imports**
**Pedagogical Goal:** Teach students how to set up their Google Colab environment and introduce the core Python libraries used in Data Science and ML.
**Agent Instructions:**
1.  **Markdown Cell:** Welcome the students and briefly explain what Google Colab is (a hosted Jupyter notebook service that requires no setup and provides free access to computing resources).
2.  **Code Cell (Imports):** Generate the code to import the foundational libraries: `pandas`, `numpy`, `matplotlib.pyplot`, and `sklearn`. 
3.  **Code Cell (Version Check):** Provide a simple script to print the versions of these libraries so students can confirm their environment is ready.

---

### **Section 2: The "AI Map" and Defining Machine Learning (Theory in Practice)**
**Pedagogical Goal:** Establish the theoretical definitions of ML using the core bibliography and differentiate it from traditional programming.
**Agent Instructions:**
1.  **Markdown Cell (Definitions):** Provide the formal definitions of Machine Learning. Include Arthur Samuel's definition ("the field of study that gives computers the ability to learn without being explicitly programmed") and Tom Mitchell's definition involving Experience (E), Task (T), and Performance (P).
2.  **Markdown Cell (The AI Map):** Explain the relationship between Artificial Intelligence (the broader goal of intelligent systems), Machine Learning (the data-driven sub-branch), and Deep Learning (neural networks). 

---

### **Section 3: Data Representation and the CRISP-DM Lifecycle**
**Pedagogical Goal:** Show students how data (the "Experience") is fed into an algorithm, distinguishing between features (inputs) and labels (outputs). Introduce the CRISP-DM methodology.
**Dataset Suggestion:** A simple toy dataset created directly in code using `pandas`, or loading a basic dataset like the Iris flower dataset.

**Agent Instructions:**
1.  **Markdown Cell (CRISP-DM):** Briefly list the 6 steps of the Cross Industry Standard Process for Data Mining (CRISP-DM): Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, and Deployment.
2.  **Code Cell (Loading Data):** Write code to create a simple `pandas` DataFrame representing a labeled dataset (e.g., columns for 'Height', 'Weight', and a label 'Species' or 'Category').
3.  **Markdown Cell (Features vs. Labels):** Explain that the independent variables (Height, Weight) are the *features*, and the dependent variable (Category) is the *label*. Explain the difference between *Labeled data* (used for Supervised Learning) and *Unlabeled data* (used for Unsupervised Learning).

---

### **Section 4: The Golden Rule - Splitting Data**
**Pedagogical Goal:** Introduce the most critical concept in ML validation: never evaluating a model on the data it was trained on to avoid overfitting. 

**Agent Instructions:**
1.  **Markdown Cell (Bias, Variance, and Overfitting):** Explain that if a model learns the training data too perfectly, it will fail on new data (Overfitting/High Variance). If it is too simple, it won't capture the pattern (Underfitting/High Bias).
2.  **Code Cell (Train/Test Split):** Generate code utilizing `sklearn.model_selection.train_test_split`. Take the DataFrame created in Section 3 and split it into training sets (e.g., 75%) and testing sets (e.g., 25%). 
3.  **Code Cell (Verification):** Print the shapes (`.shape`) of the resulting training and testing sets so students can visually verify that the data was divided correctly.
