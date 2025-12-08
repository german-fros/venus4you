import streamlit as st
from datetime import time, datetime, timedelta

from config.config import CIDADES_RS_EVENTO, FORMALIDADE_PRENDAS
from src.domain.evento import Evento

st.title('Agendar novo evento')

if "eventos" not in st.session_state:
    st.session_state.eventos = {}

if "reset_event_form" not in st.session_state:
    st.session_state.reset_event_form = False

if st.session_state.reset_event_form:
    st.session_state.form_nome = ''
    st.session_state.form_data = None
    st.session_state.form_hora = time(12,00)
    st.session_state.form_cidade = None

    st.session_state.reset_form = False

with st.form("form_novo_evento"):
    nome = st.text_input("Nome", key='form_nome')
    formalidade = st.selectbox("Formalidade", options=FORMALIDADE_PRENDAS, index=1,  key="form_formalidade")

    daqui_a_7_dias = datetime.today() + timedelta(7)

    cols = st.columns(2)
    with cols[0]:
        data = st.date_input('Data', min_value='today', max_value = daqui_a_7_dias, key='form_data')
    with cols[1]:
        horario = st.time_input('Horario', step=1800, value=time(12,00),key='form_hora')

    cols = st.columns(2)
    with cols[0]:
        estado = st.selectbox(label="Estado", options=['RS'], index=0, disabled=True, key="form_estado")
    with cols[1]:
        cidade = st.selectbox(label="Cidade", options=CIDADES_RS_EVENTO, accept_new_options=False, index=None, key='form_cidade')

    enviado = st.form_submit_button("Adicionar", type='primary')

    if enviado:
        if nome and data and horario and estado and cidade:
            if datetime.combine(data, horario) < datetime.today():
                st.warning("Data/horário selecionados são inválidos!")

            else:
                evento = Evento(nome=nome, formalidade=formalidade, data=data, horario=horario, estado=estado, cidade=cidade)

                if f"{evento.data}" not in st.session_state.eventos.keys():
                    st.session_state.eventos[f"{evento.data}"] = []

                st.session_state.eventos[f"{evento.data}"].append(evento)

                st.success('Evento marcado com sucesso!')
        
        else:
            st.warning("Campos sem preencher!")

limpar_form = st.button("Limpar")

if limpar_form:
    st.session_state.reset_event_form = True

    st.rerun()
