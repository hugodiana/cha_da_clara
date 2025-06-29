import csv
import os

ARQUIVO = "gastos.csv"

def carregar_gastos():
    gastos = []
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["valor"] = float(row["valor"])
                gastos.append(row)
    return gastos

def salvar_gastos(gastos):
    with open(ARQUIVO, "w", newline="", encoding="utf-8") as f:
        campos = ["descricao", "valor", "forma_pagamento"]
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        for gasto in gastos:
            writer.writerow(gasto)

def adicionar_gasto(descricao, valor, forma_pagamento):
    gastos = carregar_gastos()
    novo = {
        "descricao": descricao,
        "valor": float(valor),
        "forma_pagamento": forma_pagamento
    }
    gastos.append(novo)
    salvar_gastos(gastos)

def remover_gasto(indice):
    gastos = carregar_gastos()
    if 0 <= indice < len(gastos):
        gastos.pop(indice)
        salvar_gastos(gastos)