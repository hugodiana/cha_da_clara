import os

ARQUIVO = "convidados.csv"

def carregar_convidados():
    if not os.path.exists(ARQUIVO): return []
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return [linha.strip() for linha in f if linha.strip()]

def salvar_convidados(convidados):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for nome in convidados:
            f.write(nome + "\n")

def adicionar_convidado(nome):
    convidados = carregar_convidados()
    if nome and nome not in convidados:
        convidados.append(nome)
        convidados.sort()
        salvar_convidados(convidados)

def remover_convidado(nome):
    convidados = carregar_convidados()
    convidados = [c for c in convidados if c != nome]
    salvar_convidados(convidados)