import csv
import os

ARQUIVO = "presentes.csv"
CAMPOS = ['convidado', 'presente', 'agradecimento_enviado']

def carregar_presentes():
    """Carrega a lista de presentes do arquivo CSV."""
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, newline='', encoding='utf-8') as f:
        # Usamos list() para carregar tudo em memória de uma vez
        return list(csv.DictReader(f))

def salvar_presentes(presentes):
    """Salva a lista completa de presentes no arquivo CSV."""
    with open(ARQUIVO, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=CAMPOS)
        writer.writeheader()
        writer.writerows(presentes)

def adicionar_presente(convidado, presente):
    """Adiciona um novo presente à lista."""
    presentes = carregar_presentes()
    presentes.append({'convidado': convidado, 'presente': presente, 'agradecimento_enviado': 'Não'})
    salvar_presentes(presentes)

def remover_presente(indice):
    """Remove um presente da lista pelo seu índice."""
    presentes = carregar_presentes()
    if 0 <= indice < len(presentes):
        presentes.pop(indice)
        salvar_presentes(presentes)

def atualizar_status_agradecimento(indice, status):
    """Atualiza o status de 'agradecimento_enviado' para um presente específico."""
    presentes = carregar_presentes()
    if 0 <= indice < len(presentes):
        # Converte o status booleano (True/False) para a string "Sim" ou "Não"
        presentes[indice]['agradecimento_enviado'] = "Sim" if status else "Não"
        salvar_presentes(presentes)