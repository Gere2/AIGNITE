import streamlit as st
import pandas as pd
import joblib

# Configuración de la página: debe ser la primera llamada de Streamlit
st.set_page_config(
    page_title="AIGNITE",
    page_icon="🔥",
    layout="centered"
)

# Cachear el modelo como recurso para optimizar rendimiento
@st.cache_resource
def load_model():
    modelo_bundle = joblib.load("models/aignite_model.pkl")
    clf = modelo_bundle['model']
    columns = modelo_bundle['columns']
    cat_cols = modelo_bundle['cat_cols']
    return clf, columns, cat_cols

# Cargar modelo y metadatos
clf, model_columns, cat_cols = load_model()

# Función de predicción
def predict_fire_risk(new_data: dict):
    df_new = pd.DataFrame([new_data])
    for col in cat_cols:
        df_new[col] = df_new[col].astype(str)
    df_new_enc = pd.get_dummies(df_new, columns=cat_cols)
    df_new_enc = df_new_enc.reindex(columns=model_columns, fill_value=0)
    pred_class = clf.predict(df_new_enc)[0]
    pred_proba = clf.predict_proba(df_new_enc)[0]
    return pred_class, pred_proba

# Mapeo de estilos para cada nivel de riesgo
RISK_STYLE = {
    'Bajo': {'func': st.success, 'icon': '🟢'},
    'Medio': {'func': st.warning, 'icon': '🟡'},
    'Alto': {'func': st.error,   'icon': '🔴'}
}

def main():
    st.title("🔥 AIGNITE – Evaluador de Riesgo de Incendio")
    st.write("Bienvenido a la demo de AIGNITE.")

    # Layout de inputs en dos columnas
    col1, col2 = st.columns(2)
    with col1:
        HEAT_SOURC = st.selectbox("Fuente de calor (HEAT_SOURC)", ['70','8','22','31','52'], help="Código de la fuente de calor según NFPA")
        TYPE_MAT   = st.selectbox("Tipo de material (TYPE_MAT)", ['Madera','Hormigón','Metal','Plástico'], help="Material principal combustible")
        DETECTOR   = st.radio("Detector presente (DETECTOR)", ['Y','N'], help="¿Hay detector de incendios instalado?")
    with col2:
        STRUC_STAT = st.selectbox("Estado estructural (STRUC_STAT)", ['Bueno','Regular','Malo'], help="Condición actual de la estructura")
        DET_TYPE   = st.selectbox("Tipo de detector (DET_TYPE)", ['1','2','3'], help="Tipo de detector (código interno)")
        AREA       = st.slider("Superficie (AREA) en m²", 1, 10000, value=100, help="Área total a evaluar")

    if st.button("Evaluar riesgo"):
        input_data = {
            'HEAT_SOURC': HEAT_SOURC,
            'TYPE_MAT': TYPE_MAT,
            'STRUC_STAT': STRUC_STAT,
            'DETECTOR': DETECTOR,
            'DET_TYPE': DET_TYPE,
            'AREA': AREA
        }
        risk, probabilities = predict_fire_risk(input_data)
        style = RISK_STYLE.get(risk, {'func': st.info, 'icon': 'ℹ️'})
        style['func'](f"{style['icon']} Nivel de riesgo: **{risk}**")

        st.markdown("---")
        st.write("**Probabilidades por clase:**")
        st.write(f"🟢 Bajo:  {probabilities[0]:.1%}")
        st.write(f"🟡 Medio: {probabilities[1]:.1%}")
        st.write(f"🔴 Alto:  {probabilities[2]:.1%}")

        if risk == 'Bajo':
            st.balloons()

if __name__ == "__main__":
    main()
