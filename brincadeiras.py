import csv
import os

ARQUIVO = "brincadeiras.csv"
CAMPOS = ['nome', 'regras']

def carregar_brincadeiras():
    if not os.path.exists(ARQUIVO): return []
    with open(ARQUIVO, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def salvar_brincadeiras(brincadeiras):
    with open(ARQUIVO, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=CAMPOS)
        writer.writeheader()
        writer.writerows(brincadeiras)

def adicionar_brincadeira(nome, regras):
    brincadeiras = carregar_brincadeiras()
    brincadeiras.append({'nome': nome, 'regras': regras})
    salvar_brincadeiras(brincadeiras)

def remover_brincadeira(indice):
    brincadeiras = carregar_brincadeiras()
    if 0 <= indice < len(brincadeiras):
        brincadeiras.pop(indice)
        salvar_brincadeiras(brincadeiras)