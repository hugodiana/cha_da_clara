from checklist import mostrar_checklist, concluir_tarefa
from convidados import adicionar_convidado, listar_convidados
from presentes import adicionar_presente, listar_presentes

def menu():
    while True:
        print("\n==== MENU PRINCIPAL ====")
        print("1. Ver checklist")
        print("2. Marcar tarefa como concluída")
        print("3. Adicionar convidado")
        print("4. Ver lista de convidados")
        print("5. Registrar presente recebido")
        print("6. Ver presentes recebidos")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mostrar_checklist()
        elif opcao == "2":
            try:
                numero = int(input("Digite o número da tarefa: ")) - 1
                concluir_tarefa(numero)
            except ValueError:
                print("Por favor, digite um número válido.")
        elif opcao == "3":
            nome = input("Digite o nome do convidado: ")
            adicionar_convidado(nome)
        elif opcao == "4":
            listar_convidados()
        elif opcao == "5":
            nome = input("Nome do convidado: ")
            presente = input("Presente dado: ")
            adicionar_presente(nome, presente)
        elif opcao == "6":
            listar_presentes()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()
