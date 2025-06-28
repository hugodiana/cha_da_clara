import csv
import os

arquivo = "presentes.csv"
presentes = []

# Carrega os presentes do CSV
def carregar_presentes():
    if os.path.exists(arquivo):
        with open(arquivo, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                presentes.append({"convidado": row[0], "presente": row[1]})

# Salva um novo presente no CSV
def salvar_presente(convidado, presente):
    with open(arquivo, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([convidado, presente])

carregar_presentes()

def adicionar_presente(convidado, presente):
    presentes.append({"convidado": convidado, "presente": presente})
    salvar_presente(convidado, presente)
    print(f"Presente registrado: {convidado} deu '{presente}'.")

def listar_presentes():
    print("\n==== PRESENTES RECEBIDOS ====")
    for i, p in enumerate(presentes):
        print(f"{i+1}. {p['convidado']} - {p['presente']}")
