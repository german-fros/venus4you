import streamlit as st

from src.utils.clima import obter_clima_para_evento
from src.services.look import Look

if "eventos" in st.session_state and st.session_state.eventos:
    st.title("Próximos eventos")

    eventos_por_data = st.session_state.eventos

    for data in sorted(eventos_por_data.keys()):
        st.subheader(str(data))

        for evento in eventos_por_data[data]:
            with st.container(border=True):
                col1, col2 = st.columns(2)

                with col1:
                    st.text(evento)

                with col2:
                    clima_evento = obter_clima_para_evento(evento.cidade, evento.estado, evento.data, evento.horario)
                    st.text("PREVISÃO CLIMÁTICA")

                    st.text(f"Temperatura: {clima_evento['temperature']}°C")
                    st.text(f"Prob. chuva: {clima_evento['precipitation_probability']}%")
            
                with st.expander("Ver look escolhido"):
                    cols = st.columns(3)
                    look = Look(st.session_state.prendas_por_parte)
                    for i, prenda in enumerate(look.prendas):
                        with cols[i]:
                            st.image(prenda.imagem)


else:
    st.title("Nenhum evento marcado!")
    st.page_link('pages/04_Novo_evento_+.py', label="Marcar novo evento")