import csv
import os

arquivo = "convidados.csv"
convidados = []

# Carrega convidados do CSV
def carregar_convidados():
    if os.path.exists(arquivo):
        with open(arquivo, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                convidados.append(row[0])

# Salva convidados no CSV
def salvar_convidado(nome):
    with open(arquivo, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([nome])

carregar_convidados()

def adicionar_convidado(nome):
    convidados.append(nome)
    salvar_convidado(nome)
    print(f"Convidado '{nome}' adicionado com sucesso!")

def listar_convidados():
    print("\n==== LISTA DE CONVIDADOS ====")
    for i, nome in enumerate(convidados):
        print(f"{i+1}. {nome}")
