import os

ARQUIVO = "orcamento.txt"

def carregar_orcamento():
    if not os.path.exists(ARQUIVO):
        return 0.0
    with open(ARQUIVO, 'r') as f:
        try:
            return float(f.read())
        except (ValueError, TypeError):
            return 0.0

def salvar_orcamento(valor):
    with open(ARQUIVO, 'w') as f:
        f.write(str(float(valor)))