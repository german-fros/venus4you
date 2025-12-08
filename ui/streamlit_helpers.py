import streamlit as st
from datetime import datetime, timedelta, time

from config.config import CATEGORIAS_PRENDAS, FORMALIDADE_PRENDAS, CIDADES_COORDS
from src.domain.prenda import Prenda
from src.domain.evento import Evento


def gerar_form_nova_prenda():
    with st.form("form_nova_prenda"):
        categoria = st.selectbox("Categoría", CATEGORIAS_PRENDAS, index=None, key='form_categoria')
        imagem = st.file_uploader("Carregar imagem", type = ['jpg', 'png'], accept_multiple_files=False, key='form_imagem')

        enviado = st.form_submit_button("Adicionar", type='primary')

        if enviado:
            if categoria and imagem:
                prenda = Prenda(categoria=categoria, imagem=imagem)

                st.session_state.guarda_roupas[prenda.id] = prenda

                st.success('Prenda registrada com sucesso!')
            
            elif categoria:
                st.warning("Deve adjuntar uma imagem da prenda!")

            else:
                st.warning("Deve especificar a categoria da prenda!")
    
    btn_limpar_form()


def gerar_form_novo_evento():
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
            cidade = st.selectbox(label="Cidade", options=list(CIDADES_COORDS.keys()), accept_new_options=False, index=None, key='form_cidade')

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

    btn_limpar_form()

    
def btn_limpar_form():
    limpar_form = st.button("Limpar")
    if limpar_form:
        st.session_state.reset_form = True

        st.rerun()