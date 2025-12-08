import streamlit as st
from datetime import datetime

from src.utils.clima import obter_clima_para_evento
from src.services.look import Look

if "eventos" in st.session_state and st.session_state.eventos:
    st.title("Próximos eventos 📅")

    eventos_por_data = st.session_state.eventos

    for data in sorted(eventos_por_data.keys()):
        data_formateada = datetime.strptime(data, "%Y-%m-%d").date()
        st.subheader(data_formateada.strftime("%d/%m/%Y"))

        for evento in eventos_por_data[data]:
            with st.container(border=True):
                col1, col2 = st.columns(2)

                with col1:
                    st.text(evento)

                with col2:
                    cols = st.columns(2)
                    with cols[0]:
                        clima_evento = obter_clima_para_evento(evento.cidade, evento.estado, evento.data, evento.horario)
                        st.text("PREVISÃO CLIMÁTICA")

                        st.text(f"Temperatura: {clima_evento['temperature']}°C\nProb. chuva: {clima_evento['precipitation_probability']}%")
                    
                    with cols[1]:
                        if clima_evento['precipitation_probability'] >= 75:
                            st.text('🌧️')
                        elif 75 > clima_evento['precipitation_probability'] >= 50:
                            st.text('🌦️', width='stretch')
                        elif 50 > clima_evento['precipitation_probability'] >= 25:
                            st.text('⛅', width='stretch')
                        else:
                            st.text('☀️')
            
                with st.expander("Ver look escolhido 🪞"):
                    if "prendas_por_parte" in st.session_state and st.session_state.prendas_por_parte:
                        cols = st.columns(3)
                        look = Look(st.session_state.prendas_por_parte)

                        for i, prenda in enumerate(look.prendas):
                            col = i % 3

                            with cols[col]:
                                st.image(prenda.imagem)

                    else:
                        st.text("Registre mais prendas para montar o seu look!")


else:
    st.title("Nenhum evento marcado!")

    adicionar_evento = st.button("Agendar novo evento ➕", type='primary')

    if adicionar_evento:
        st.switch_page('pages/04_Novo_evento_+.py')