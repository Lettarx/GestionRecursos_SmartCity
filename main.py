import streamlit as st
from logica_difusa import logica_difusa, calcular_intensidad, observar_intensidad

st.set_page_config("Logica Difusa para Alumbrado Publico")

st.title("Logica Difura para Alumbrado Publico")
sistema, intensidad = logica_difusa()

with st.form("form_logica_difusa"):  
  hora_dia = st.slider("Ingrese Hora del día",0,23)
  cant_trafico = st.slider("Ingrese intensidad del flujo de trafico, siendo 0 flujo bajo y 10 flujo alto",0,10)
  clima = st.slider("Condiciones climaticas, siendo 0 buen clima y 10 mal clima",0,10)

  envio = st.form_submit_button("Enviar Datos")

if envio:
    
  sistema_calculo = calcular_intensidad(sistema, hora_dia, cant_trafico, clima)

  st.markdown(f"### Intensidad de la luz: {sistema_calculo.output['Intensidad_luces']:.2f}%")
    
  try:
    with st.spinner('Generando gráfico...'):
        fig = observar_intensidad(sistema, intensidad)
        st.pyplot(fig)
  except Exception as e:
    st.error(f"Error al mostrar el gráfico: {str(e)}")