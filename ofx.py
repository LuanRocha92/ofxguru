import streamlit as st
import re

st.title("Corretor de CHECKNUM - OFX")

uploaded_file = st.file_uploader("Envie o arquivo OFX", type=["ofx"])

def corrigir_checknum(texto):
    def repl(match):
        return f"<CHECKNUM>{match.group(1)[:5]}"
    return re.sub(r"<CHECKNUM>(\d+)", repl, texto)

if uploaded_file:
    conteudo = uploaded_file.read().decode("utf-8", errors="ignore")
    novo = corrigir_checknum(conteudo)

    st.success("Arquivo processado!")

    st.download_button(
        "Baixar OFX corrigido",
        novo,
        "ofx_corrigido.ofx"
    )