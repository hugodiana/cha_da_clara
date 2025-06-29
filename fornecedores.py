import csv
import os

ARQUIVO = "fornecedores.csv"
CAMPOS = ['servico', 'nome_fornecedor', 'contato', 'status']

def carregar_fornecedores():
    """Carrega a lista de fornecedores do arquivo CSV."""
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def salvar_fornecedores(fornecedores):
    """Salva a lista completa de fornecedores no arquivo CSV."""
    with open(ARQUIVO, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=CAMPOS)
        writer.writeheader()
        writer.writerows(fornecedores)

def adicionar_fornecedor(servico, nome, contato, status):
    """Adiciona um novo fornecedor à lista."""
    fornecedores = carregar_fornecedores()
    fornecedores.append({
        'servico': servico,
        'nome_fornecedor': nome,
        'contato': contato,
        'status': status
    })
    salvar_fornecedores(fornecedores)

def remover_fornecedor(indice):
    """Remove um fornecedor da lista pelo seu índice."""
    fornecedores = carregar_fornecedores()
    if 0 <= indice < len(fornecedores):
        fornecedores.pop(indice)
        salvar_fornecedores(fornecedores)