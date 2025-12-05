import streamlit as st

if "guarda_roupas" in st.session_state and st.session_state.guarda_roupas:
    st.title("Prendas registradas")

    prendas = list(st.session_state.guarda_roupas.values())

    cols = st.columns(3)

    for i, prenda in enumerate(prendas):
        col = cols[i % 3]

        with col:
            st.image(prenda.imagem)
            st.text(prenda)

else:
    st.title("Seu guarda roupas está vazío")
    st.page_link('pages/02_registro_de_prenda.py', label="Registrar nova prenda")

