import streamlit as st

from ui.streamlit_helpers import gerar_form_nova_prenda

st.title('Adicionar nova peça 👚')

if "guarda_roupas" not in st.session_state:
    st.session_state.guarda_roupas = {}

if "reset_form" not in st.session_state:
    st.session_state.reset_form = False

if st.session_state.reset_form:
    st.session_state.form_categoria = None

    st.session_state.reset_form = False

gerar_form_nova_prenda()
