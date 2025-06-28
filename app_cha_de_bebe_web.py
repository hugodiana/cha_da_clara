import streamlit as st
from checklist import tarefas, concluir_tarefa, concluidas, salvar_tarefas
from convidados import adicionar_convidado, convidados
from presentes import adicionar_presente, presentes

st.set_page_config(page_title="Organizador do Chá de Bebê", layout="wide")

st.title("👶 Organizador do Chá de Bebê")

# Checklist de Tarefas
st.header("✅ Checklist")

for i, tarefa in enumerate(tarefas):
    concluida = concluidas[i]
    novo_estado = st.checkbox(tarefa, value=bool(concluida), key=f"tarefa_{i}")
    if novo_estado != bool(concluida):
        if novo_estado:
            concluir_tarefa(i)
        else:
            concluidas[i] = 0
            salvar_tarefas()

# Lista de Convidados
st.header("👥 Lista de Convidados")
col1, col2 = st.columns([2, 3])

with col1:
    nome_convidado = st.text_input("Adicionar novo convidado:")
    if st.button("Adicionar Convidado"):
        if nome_convidado:
            adicionar_convidado(nome_convidado)
            st.experimental_rerun()

with col2:
    st.subheader("Convidados")
    for c in convidados:
        st.markdown(f"- {c}")

# Registro de Presentes
st.header("🎁 Presentes Recebidos")
col3, col4 = st.columns(2)

with col3:
    nome_presente = st.text_input("Nome do convidado:", key="presente_nome")
    presente = st.text_input("Presente:", key="presente_item")
    if st.button("Registrar Presente"):
        if nome_presente and presente:
            adicionar_presente(nome_presente, presente)
            st.experimental_rerun()

with col4:
    st.subheader("Presentes Recebidos")
    for p in presentes:
        st.markdown(f"- **{p['convidado']}**: {p['presente']}")
