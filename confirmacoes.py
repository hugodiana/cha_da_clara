import csv
import os

ARQUIVO = "confirmacoes.csv"
confirmacoes = {}

def carregar_confirmacoes():
    global confirmacoes
    confirmacoes = {}
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                nome = row["nome"]
                confirmacoes[nome] = {
                    "status": row.get("status", "Não respondeu"),
                    "acompanhante": row.get("acompanhante", "Não"),
                    "observacao": row.get("observacao", "")
                }
    return confirmacoes

def salvar_confirmacoes():
    with open(ARQUIVO, "w", newline="", encoding="utf-8") as f:
        campos = ["nome", "status", "acompanhante", "observacao"]
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        for nome, dados in confirmacoes.items():
            writer.writerow({
                "nome": nome,
                "status": dados.get("status", "Não respondeu"),
                "acompanhante": dados.get("acompanhante", "Não"),
                "observacao": dados.get("observacao", "")
            })

def atualizar_confirmacao(nome, status, acompanhante, observacao):
    confirmacoes[nome] = {
        "status": status,
        "acompanhante": acompanhante,
        "observacao": observacao
    }
    salvar_confirmacoes()

def remover_confirmacao(nome):
    if nome in confirmacoes:
        del confirmacoes[nome]
        salvar_confirmacoes()

# Inicializa confirmacoes ao importar
carregar_confirmacoes()