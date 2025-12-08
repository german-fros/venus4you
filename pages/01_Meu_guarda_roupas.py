import streamlit as st
from collections import defaultdict

st.set_page_config(
    page_title="Meu guarda roupas",
    page_icon="👗"
)

if "guarda_roupas" in st.session_state and st.session_state.guarda_roupas:
    st.title("Peças registradas")

    prendas = list(st.session_state.guarda_roupas.values())

    for prenda in prendas:
        if "prendas_por_parte" not in st.session_state:
            st.session_state.prendas_por_parte = {}

        if prenda.parte_do_corpo not in st.session_state.prendas_por_parte:
            st.session_state.prendas_por_parte[prenda.parte_do_corpo] = []

        st.session_state.prendas_por_parte[prenda.parte_do_corpo].append(prenda)

    prendas_por_categoria = defaultdict(list)
    
    for prenda in prendas:
        prendas_por_categoria[prenda.categoria].append(prenda)

    for cat in sorted(prendas_por_categoria.keys()):
        st.subheader(cat)

        cols = st.columns(3)

        for i, prenda in enumerate(prendas_por_categoria[cat]):
            col = i % 3
            try:
                with cols[col]:
                    with st.container(border=True):
                        st.image(prenda.imagem)
            except IndexError:
                raise(f"Coluna fora de rango: {col}")

else:
    st.title("Seu guarda roupas está vazío 🪹")

    adicionar_prenda = st.button("Registrar nova peça ➕", type='primary')
    if adicionar_prenda:
        st.switch_page('pages/02_Nova_peça_+.py')

