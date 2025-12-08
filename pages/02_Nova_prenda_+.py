import streamlit as st

from config.config import CATEGORIAS_PRENDAS, FORMALIDADE_PRENDAS, CORES_PRENDAS
from src.domain.prenda import Prenda

st.title('Adicionar nova prenda 👚')

if "guarda_roupas" not in st.session_state:
    st.session_state.guarda_roupas = {}

if "reset_form" not in st.session_state:
    st.session_state.reset_form = False

if st.session_state.reset_form:
    st.session_state.form_categoria = None

    st.session_state.reset_form = False

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

limpar_form = st.button("Limpar")

if limpar_form:
    st.session_state.reset_form = True

    st.rerun()
