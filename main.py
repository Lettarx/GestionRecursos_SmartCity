import streamlit as st
from logica_difusa import logica_difusa, calcular_intensidad, observar_intensidad

st.set_page_config("Logica Difusa para Alumbrado Publico")

st.title("Logica Difura para Alumbrado Publico")
sistema, intensidad = logica_difusa()

with st.form("form_logica_difusa"):
  hora_dia = st.number_input("Ingrese Hora del día",0,23,placeholder="valor entre 0 y 23")
  cant_trafico = st.number_input("Ingrese intensidad del flujo de trafico, siendo 0 flujo bajo y 10 flujo alto",0,10)
  clima = st.number_input("Condiciones climaticas, siendo 0 buen clima y 10 mal clima",0,10)

  envio = st.form_submit_button("Enviar Datos")

if envio:
    sistema_calculo = calcular_intensidad(sistema, hora_dia, cant_trafico, clima)
    st.markdown(f"### Intensidad de la luz: {sistema.output['Intensidad_luces']:.2f}%")
    
    try:
        with st.spinner('Generando gráfico...'):
            fig = observar_intensidad(sistema, intensidad)
            st.pyplot(fig)
    except Exception as e:
        st.error(f"Error al mostrar el gráfico: {str(e)}")
fuzzy 
