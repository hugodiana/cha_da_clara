import csv
import os

concluidas = []
arquivo = "checklist.csv"

tarefas = [
    "Definir data e horário",
    "Escolher local",
    "Enviar convites",
    "Montar lista de convidados",
    "Decorar o local",
    "Comprar comidas e bebidas",
    "Organizar brincadeiras",
    "Anotar presentes recebidos"
]

# Inicia com todos zerados se não houver arquivo
concluidas = [0] * len(tarefas)

# Salva o status atual das tarefas
def salvar_tarefas():
    with open(arquivo, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for i in range(len(tarefas)):
            writer.writerow([tarefas[i], concluidas[i]])

# Carrega do CSV ou inicia com zeros
def carregar_tarefas():
    global concluidas
    if os.path.exists(arquivo):
        with open(arquivo, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            concluidas = [int(row[1]) for row in reader]
    else:
        concluidas = []

    # Garante que o tamanho bata com tarefas
    while len(concluidas) < len(tarefas):
        concluidas.append(0)
    # Remove extras caso o CSV tenha mais do que a lista atual
    concluidas = concluidas[:len(tarefas)]

# Inicializa ao carregar
carregar_tarefas()

# Função para mostrar no terminal (usada no modo terminal)
def mostrar_checklist():
    print("\\n==== CHECKLIST DO CHÁ DE BEBÊ ====")
    for i, tarefa in enumerate(tarefas):
        status = "✅" if concluidas[i] else "❌"
        print(f"{i+1}. {tarefa} - {status}")

# Marca tarefa como concluída
def concluir_tarefa(numero):
    if 0 <= numero < len(tarefas):
        concluidas[numero] = 1
        salvar_tarefas()
