"""Modulo para o Observatório."""

from services.observatorio import Observatorio

def menu():
    """Função para Armazenar a lista."""
    banco = Observatorio()

    while True:
        print("\n" + 30*"=")
        print("   SISTEMA OBSERVATÓRIO PI   ")
        print(30*"=")
        print("1. Cadastrar Novo Projeto")
        print("2. Listar Todos os Projetos")
        print("3. Buscar Projeto por Título")
        print("4. Alterar Descrição de um Projeto")
        print("0. Sair")
        print(30*"=")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título do projeto: ")
            curso = input("Curso: ")
            periodo = input("Período: ")
            descricao = input("Descrição inicial: ")

            # Chamamos o método passando o que o usuário digitou
            resultado = banco.adicionar_projeto(titulo, curso, periodo, descricao)
            print(f"\n>>> {resultado}")

        elif opcao == "2":
            print("\n--- LISTA DE PROJETOS ---")
            projetos = banco.listar_projetos()
            if not projetos:
                print("Nenhum projeto cadastrado.")
            for p in projetos:
                print(p)

        elif opcao == "3":
            busca = input("Digite o título exato para buscar: ")
            projeto = banco.buscar_projeto(busca)
            if projeto:
                projeto.mostrar_dados()
            else:
                print(">>> Projeto não encontrado.")

        elif opcao == "4":
            busca = input("De qual projeto você quer mudar a descrição? ")
            projeto = banco.buscar_projeto(busca)

            if projeto:
                nova_desc = input("Digite a nova descrição: ")
                print(f"\n>>> {projeto.alterar_descricao(nova_desc)}")
            else:
                print(">>> Erro: Projeto não encontrado.")

        elif opcao == "0":
            print("Saindo do sistema... Até logo!")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()