import csv
import os

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

# Carrega o status das tarefas do CSV
def carregar_tarefas():
    if not os.path.exists(arquivo):
        salvar_tarefas()
    with open(arquivo, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        return [int(row[1]) for row in reader]

# Salva o status das tarefas no CSV
def salvar_tarefas():
    with open(arquivo, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for i, status in enumerate(concluidas):
            writer.writerow([tarefas[i], status])

# Inicializa a lista de tarefas concluídas
concluidas = carregar_tarefas()

def mostrar_checklist():
    print("\n==== CHECKLIST DO CHÁ DE BEBÊ ====")
    for i, tarefa in enumerate(tarefas):
        status = "✅" if concluidas[i] else "❌"
        print(f"{i+1}. {tarefa} - {status}")

def concluir_tarefa(numero):
    if 0 <= numero < len(tarefas):
        if not concluidas[numero]:
            concluidas[numero] = 1
            salvar_tarefas()
            print("Tarefa marcada como concluída!")
        else:
            print("Essa tarefa já foi concluída.")
    else:
        print("Número inválido.")
