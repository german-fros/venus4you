import streamlit as st
from collections import defaultdict

if "guarda_roupas" in st.session_state and st.session_state.guarda_roupas:
    st.title("Prendas registradas")

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

        for prenda in prendas_por_categoria[cat]:
            with st.container(border=True):
                st.image(prenda.imagem)
                st.text(prenda)

else:
    st.title("Seu guarda roupas está vazío")
    st.page_link('pages/02_Nova_prenda_+.py', label="Registrar nova prenda")

