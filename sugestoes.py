import csv
import os

ARQUIVO = "sugestoes.csv"
CAMPOS = ['item', 'detalhes']

def carregar_sugestoes():
    if not os.path.exists(ARQUIVO): return []
    with open(ARQUIVO, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def salvar_sugestoes(sugestoes):
    with open(ARQUIVO, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=CAMPOS)
        writer.writeheader()
        writer.writerows(sugestoes)

def adicionar_sugestao(item, detalhes):
    sugestoes = carregar_sugestoes()
    sugestoes.append({'item': item, 'detalhes': detalhes})
    salvar_sugestoes(sugestoes)

def remover_sugestao(indice):
    sugestoes = carregar_sugestoes()
    if 0 <= indice < len(sugestoes):
        sugestoes.pop(indice)
        salvar_sugestoes(sugestoes)