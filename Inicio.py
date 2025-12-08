import streamlit as st

st.set_page_config(
    page_title="Venus4You",
    page_icon="👗"
)

USERS = {
    "Admin": "admin",
    "Florencia": '1234'
}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = None


def show_login():
    st.title("Login - Venus4You")

    with st.form("login_form"):
        username = st.text_input("Usuário")
        password = st.text_input("Senha", type="password")

        submit = st.form_submit_button("Entrar")

    if submit:
        if username in USERS and USERS[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username

            st.switch_page("pages/01_Meu_guarda_roupas.py")
        else:
            st.error("Usuário ou senha incorretos!")


def show_app():
    st.sidebar.write(f"Logado como: **{st.session_state.username}**")
    if st.sidebar.button("Sair"):
        st.session_state.logged_in = False
        st.session_state.username = None
        st.rerun()

    with st.container(horizontal_alignment="center"):
        st.image('images/venus4you_logo.jpg', width=250)
        st.title(f'Bem-vind@ {st.session_state.username}', text_alignment='center', width='content')
        st.subheader("Sobre nós:")

        st.text("""
                Venus4You é um aplicativo que transforma a forma de organizar e utilizar suas roupas. Aqui, você registra suas peças, adiciona fotos e informações para que, com esses dados, o sistema cria combinações ideais para cada ocasião, considerando clima, tipo de evento e a rotação das suas peças.

                O objetivo é facilitar o seu dia a dia, ajudar na escolha do look perfeito e promover um uso mais consciente do guarda-roupa. Tudo isso de maneira simples, intuitiva e personalizada.

                Experimente uma nova forma de se vestir com praticidade e inteligência.
                """, text_alignment='center')
        


if not st.session_state.logged_in:
    show_login()
else:
    show_app()


