# AIGNITE
# AIGNITE – Evaluador de Riesgo de Incendio

¡Bienvenido a **AIGNITE**! Esta aplicación web permite evaluar el riesgo de incendio de una instalación o vivienda de manera rápida e intuitiva, usando un modelo de **Random Forest** entrenado sobre datos reales.

---

## 📂 Estructura del proyecto

```
AIGNITE_web/
├── app.py              # Aplicación Streamlit
├── train_model.py      # Script de entrenamiento y serialización del modelo
├── requirements.txt    # Dependencias del proyecto
├── data/
│   └── raw/
│       └── fireincident.txt   # Datos de entrada crudos
└── models/
    └── aignite_model.pkl      # Modelo entrenado y metadatos serializados
```

---

## 🛠️ Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tu-usuario/AIGNITE_web.git
   cd AIGNITE_web
   ```

2. Crea y activa un entorno virtual (recomendado):

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate    # Windows
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Asegúrate de tener los datos crudos en `data/raw/fireincident.txt`.

---

## 🎯 Entrenamiento del modelo

Ejecuta el script `train_model.py` para procesar los datos, entrenar el modelo y serializarlo:

```bash
python train_model.py
```

Al finalizar, se generará el fichero `models/aignite_model.pkl`.

---

## 🚀 Uso de la aplicación

1. Lanza la aplicación Streamlit:

   ```bash
   streamlit run app.py
   ```

2. Abre tu navegador en `http://localhost:8501`.

3. Ajusta los parámetros de la columna lateral y haz clic en **Evaluar riesgo**.

4. Visualiza el nivel de riesgo (`Bajo`, `Medio`, `Alto`) y las probabilidades.

---

## 🎨 Mejoras UX/UI

* Diseño ancho (`layout="wide"`).
* CSS personalizado para títulos, inputs y contenedor de resultados.
* Expander en sidebar para agrupar parámetros.
* Resultados estilizados con colores e iconos.

---

## 📦 Dependencias

Ver `requirements.txt` para más detalles:

```
streamlit==1.45.1
pandas==2.2.3
scikit-learn==1.6.1
joblib==1.5.0
shap (opcional para explicabilidad)
```

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Abre un issue o envía un pull request para sugerir mejoras.

---

## 📄 Licencia

Este proyecto está bajo la [MIT License](LICENSE).
