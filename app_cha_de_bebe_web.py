import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# Importando todas as funções dos seus módulos locais
from checklist import carregar_lista_tarefas, carregar_status_tarefas, adicionar_tarefa, remover_tarefa, concluir_tarefa, desmarcar_tarefa
from convidados import carregar_convidados, adicionar_convidado, remover_convidado
from presentes import carregar_presentes, adicionar_presente, remover_presente, atualizar_status_agradecimento
from gastos import carregar_gastos, adicionar_gasto, remover_gasto
from confirmacoes import carregar_confirmacoes, atualizar_confirmacao, remover_confirmacao
from orcamento import carregar_orcamento, salvar_orcamento
from sugestoes import carregar_sugestoes, adicionar_sugestao, remover_sugestao
from brincadeiras import carregar_brincadeiras, adicionar_brincadeira, remover_brincadeira
from fornecedores import carregar_fornecedores, adicionar_fornecedor, remover_fornecedor

st.set_page_config(page_title="Organizador de Chá de Bebê", layout="wide")

# --- ETAPA 1: QUESTIONÁRIO INICIAL ---
if 'nome_bebe' not in st.session_state:
    st.title("👶 Bem-vindo(a) ao Organizador de Chá de Bebê!")
    st.write("Primeiro, vamos personalizar o aplicativo para você.")
    with st.form(key="info_bebe_form"):
        nome_bebe = st.text_input("Qual é o nome do bebê?")
        sexo_bebe = st.selectbox("Qual é o sexo do bebê?", ("Menina", "Menino", "Prefiro não informar / Gêmeos"))
        st.divider()
        data_nao_definida = st.checkbox("Ainda não defini a data do chá", value=False)
        data_cha = st.date_input("Qual a data do Chá?", disabled=data_nao_definida, min_value=datetime.today())
        if st.form_submit_button("✨ Salvar e Iniciar!"):
            if nome_bebe:
                st.session_state['nome_bebe'] = nome_bebe
                st.session_state['sexo_bebe'] = sexo_bebe
                st.session_state['data_cha'] = None if data_nao_definida else data_cha
                st.rerun()
            else:
                st.error("Por favor, preencha o nome do bebê.")

# --- ETAPA 2: APLICATIVO PRINCIPAL ---
else:
    # --- LÓGICA DE PERSONALIZAÇÃO ---
    NOME_BEBE, SEXO_BEBE, DATA_CHA = st.session_state['nome_bebe'], st.session_state['sexo_bebe'], st.session_state.get('data_cha')
    if SEXO_BEBE == "Menina": ICONE, PREPOSICAO = "🎀", "da"
    elif SEXO_BEBE == "Menino": ICONE, PREPOSICAO = "🧸", "do"
    else: ICONE, PREPOSICAO = "🍼", "de"

    # --- BARRA LATERAL ---
    st.sidebar.title(f"{ICONE} Navegação")
    paginas = ["🗓️ Painel Principal", "✅ Checklist", "👥 Convidados", "🎁 Presentes", "💸 Gastos", "💡 Sugestões", "🎲 Brincadeiras", "📞 Fornecedores"]
    pagina = st.sidebar.radio("Ir para:", paginas)
    
    with st.sidebar.expander("⚙️ Configurações"):
        st.session_state['nome_bebe'] = st.text_input("Nome do bebê", value=NOME_BEBE)
        st.session_state['sexo_bebe'] = st.selectbox("Sexo", ("Menina", "Menino", "Prefiro não informar / Gêmeos"), index=["Menina", "Menino", "Prefiro não informar / Gêmeos"].index(SEXO_BEBE))
        st.session_state['data_cha'] = st.date_input("Data do Chá", value=DATA_CHA if DATA_CHA else datetime.today())

    # --- TÍTULO E CONTAGEM REGRESSIVA ---
    st.title(f"👶 Organizador do Chá {PREPOSICAO} {NOME_BEBE}")
    if DATA_CHA:
        delta = DATA_CHA - datetime.now().date()
        if delta.days > 0: st.subheader(f"🎉 Faltam {delta.days} dias para o grande dia!")
        elif delta.days == 0: st.subheader("🎉 É hoje o grande dia!")
        else: st.subheader("🎉 O grande dia já passou!")
    else:
        st.info("A data do chá ainda não foi definida. Você pode defini-la nas 'Configurações'.")
    st.divider()

    # --- PÁGINAS ---
    if pagina == "🗓️ Painel Principal":
        st.header("🗓️ Painel de Controle")
        col1, col2 = st.columns(2)
        with col1:
            with st.container(border=True):
                st.subheader("✅ Resumo da Checklist")
                tarefas, status = carregar_lista_tarefas(), carregar_status_tarefas()
                total, feitas = len(tarefas), sum(status)
                st.progress(feitas / total if total > 0 else 0)
                st.write(f"{feitas} de {total} tarefas concluídas.")
        with col2:
            with st.container(border=True):
                st.subheader("👥 Resumo dos Convidados")
                convidados, confirmacoes = carregar_convidados(), carregar_confirmacoes()
                confirmados = sum(1 for d in confirmacoes.values() if d.get("status") == "Confirmado")
                nao_vai = sum(1 for d in confirmacoes.values() if d.get("status") == "Não vai")
                sem_resposta = len(convidados) - confirmados - nao_vai
                fig = px.pie(values=[confirmados, nao_vai, sem_resposta], names=['Confirmados', 'Não Vão', 'Sem Resposta'], 
                             color_discrete_map={'Confirmados':'#63C5DA', 'Não Vão':'#FF6961', 'Sem Resposta':'#D3D3D3'}, hole=.3)
                fig.update_layout(showlegend=False, margin=dict(l=10, r=10, t=10, b=10), height=200)
                st.plotly_chart(fig, use_container_width=True)
        st.divider()
        with st.container(border=True):
            st.subheader("💰 Resumo do Orçamento")
            orcamento, gastos = carregar_orcamento(), carregar_gastos()
            total_gasto = sum(g['valor'] for g in gastos)
            c1, c2, c3 = st.columns(3)
            c1.metric("Orçamento Total", f"R$ {orcamento:.2f}")
            c2.metric("Total Gasto", f"R$ {total_gasto:.2f}", delta_color="inverse")
            c3.metric("Saldo Restante", f"R$ {orcamento - total_gasto:.2f}")
            st.progress(total_gasto / orcamento if orcamento > 0 else 0)

    elif pagina == "✅ Checklist":
        st.header("✅ Checklist de Preparativos")
        with st.expander("➕ Adicionar nova tarefa"):
            nova_tarefa = st.text_input("Digite a tarefa:", key="add_task_input")
            if st.button("Adicionar Tarefa"):
                if nova_tarefa:
                    adicionar_tarefa(nova_tarefa)
                    st.session_state.add_task_input = ""
                    st.rerun()
        st.divider()
        tarefas, status_tarefas = carregar_lista_tarefas(), carregar_status_tarefas()
        for i, tarefa in enumerate(tarefas):
            c1, c2 = st.columns([10, 1])
            status_atual = bool(status_tarefas[i]) if i < len(status_tarefas) else False
            if c1.checkbox(tarefa, value=status_atual, key=f"task_{i}") != status_atual:
                concluir_tarefa(i) if not status_atual else desmarcar_tarefa(i)
                st.rerun()
            if c2.button("🗑️", key=f"del_task_{i}"):
                remover_tarefa(i)
                st.rerun()

    elif pagina == "👥 Convidados":
        st.header("👥 Lista de Convidados")
        with st.expander("➕ Adicionar novo convidado"):
            nome_convidado = st.text_input("Nome do convidado:", key="add_guest_input")
            if st.button("Adicionar Convidado"):
                if nome_convidado:
                    adicionar_convidado(nome_convidado)
                    st.session_state.add_guest_input = ""
                    st.rerun()
        st.divider()
        convidados = carregar_convidados()
        st.subheader(f"📋 Convidados ({len(convidados)})")
        for i, c in enumerate(convidados):
            c1, c2 = st.columns([4, 1])
            c1.markdown(f"- {c}")
            if c2.button("🗑️", key=f"del_guest_{i}"):
                st.session_state[f'confirm_delete_guest_{i}'] = True
            if st.session_state.get(f'confirm_delete_guest_{i}'):
                st.warning(f"Tem certeza que deseja remover {c}?")
                c3, c4 = st.columns(2)
                if c3.button("Sim, remover", key=f"yes_del_guest_{i}", type="primary"):
                    remover_convidado(c); remover_confirmacao(c)
                    del st.session_state[f'confirm_delete_guest_{i}']
                    st.rerun()
                if c4.button("Não", key=f"no_del_guest_{i}"):
                    del st.session_state[f'confirm_delete_guest_{i}']
                    st.rerun()
        st.divider()
        st.subheader("📬 Confirmações de Presença")
        #... (O resto da lógica de confirmações)

    elif pagina == "💸 Gastos":
        st.header("💸 Controle de Gastos")
        orcamento = carregar_orcamento()
        novo_orcamento = st.number_input("Defina seu orçamento total:", min_value=0.0, value=orcamento, format="%.2f")
        if novo_orcamento != orcamento:
            salvar_orcamento(novo_orcamento)
            st.rerun()
        with st.expander("➕ Adicionar gasto"):
            # ... (Lógica para adicionar com limpeza de input)
            pass
        st.divider()
        gastos = carregar_gastos()
        # ... (Lógica para listar gastos com confirmação de exclusão)
        
    elif pagina == "📞 Fornecedores":
        st.header("📞 Agenda de Fornecedores")
        with st.expander("➕ Adicionar novo fornecedor"):
            servico = st.text_input("Serviço (ex: Bolo, Decoração):", key="add_forn_serv")
            nome = st.text_input("Nome do Fornecedor/Empresa:", key="add_forn_nome")
            contato = st.text_input("Contato (Telefone/Email):", key="add_forn_cont")
            status = st.selectbox("Status:", ["A definir", "Orçamento", "Contratado"], key="add_forn_stat")
            if st.button("Adicionar Fornecedor"):
                if servico and nome:
                    adicionar_fornecedor(servico, nome, contato, status)
                    st.session_state.add_forn_serv, st.session_state.add_forn_nome, st.session_state.add_forn_cont = "", "", ""
                    st.rerun()
        st.divider()
        st.subheader(f"📋 Fornecedores Contratados")
        fornecedores = carregar_fornecedores()
        for i, f in enumerate(fornecedores):
            c1, c2, c3, c4, c5 = st.columns([2, 3, 3, 2, 1])
            c1.markdown(f"**{f['servico']}**")
            c2.write(f['nome_fornecedor'])
            c3.write(f['contato'])
            c4.markdown(f"`{f['status']}`")
            if c5.button("🗑️", key=f"del_forn_{i}"):
                remover_fornecedor(i)
                st.rerun()

    # O código para as outras páginas (Presentes, Sugestões, Brincadeiras) segue o mesmo padrão
    # com limpeza de input e, opcionalmente, confirmação de exclusão.