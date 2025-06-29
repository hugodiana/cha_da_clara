import csv
import os

# Arquivo para os status (0 ou 1)
ARQUIVO_STATUS = "checklist.csv" 
# Novo arquivo para os nomes das tarefas
ARQUIVO_TAREFAS = "checklist_tarefas.csv"

# Lista de tarefas padrão para o primeiro uso
TAREFAS_PADRAO = [
    "Escolher local", "Enviar convites", "Comprar decoração",
    "Organizar comidas e bebidas", "Confirmar lista de presentes",
    "Montar brincadeiras", "Preparar lembrancinhas", "Organizar música",
    "Montar espaço para fotos", "Definir horário"
]

# --- Funções para gerenciar a LISTA DE TAREFAS ---

def carregar_lista_tarefas():
    """Carrega os nomes das tarefas do arquivo."""
    if not os.path.exists(ARQUIVO_TAREFAS):
        # Se o arquivo não existe, cria com as tarefas padrão
        salvar_lista_tarefas(TAREFAS_PADRAO)
        # E também cria um arquivo de status correspondente
        salvar_status_tarefas([0] * len(TAREFAS_PADRAO))
        return TAREFAS_PADRAO
    
    with open(ARQUIVO_TAREFAS, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        try:
            return next(reader)
        except StopIteration:
            return []

def salvar_lista_tarefas(tarefas):
    """Salva os nomes das tarefas no arquivo."""
    with open(ARQUIVO_TAREFAS, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(tarefas)

# --- Funções para gerenciar os STATUS das tarefas ---

def carregar_status_tarefas():
    """Carrega a lista de status (0 ou 1) do arquivo."""
    if not os.path.exists(ARQUIVO_STATUS):
        return []
    
    with open(ARQUIVO_STATUS, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        try:
            status_str = next(reader)
            return [int(s) for s in status_str if s.isdigit()]
        except StopIteration:
            return []

def salvar_status_tarefas(status):
    """Salva a lista de status no arquivo."""
    with open(ARQUIVO_STATUS, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(status)

# --- Funções para MODIFICAR a checklist ---

def adicionar_tarefa(nova_tarefa):
    """Adiciona uma nova tarefa e um status correspondente."""
    if not nova_tarefa:
        return

    tarefas = carregar_lista_tarefas()
    status = carregar_status_tarefas()
    
    tarefas.append(nova_tarefa)
    status.append(0) # Nova tarefa começa como não concluída
    
    salvar_lista_tarefas(tarefas)
    salvar_status_tarefas(status)

def remover_tarefa(indice):
    """Remove uma tarefa e seu status pelo índice."""
    tarefas = carregar_lista_tarefas()
    status = carregar_status_tarefas()
    
    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)
        status.pop(indice)
        salvar_lista_tarefas(tarefas)
        salvar_status_tarefas(status)

def concluir_tarefa(indice):
    """Marca o status de uma tarefa como concluída (1)."""
    status = carregar_status_tarefas()
    if 0 <= indice < len(status):
        status[indice] = 1
        salvar_status_tarefas(status)

def desmarcar_tarefa(indice):
    """Marca o status de uma tarefa como não concluída (0)."""
    status = carregar_status_tarefas()
    if 0 <= indice < len(status):
        status[indice] = 0
        salvar_status_tarefas(status)