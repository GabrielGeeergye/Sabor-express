import os

restaurantes = []

def exibir_titulo():
    print("Sabor express\n")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair')

def finalizar_program():
    os.system('cls')
    print('\n Finalizar programa... \n')

def opcao_invailida():
    print('Opção inválida!\n')
    print('Digite uma tecla para voltar ao menu principal')

def  cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastrar novos restaurantes\n')
    nome_do_restaurante = input('\nDigite o nome do restaurante que você deseja cadastrar:')
    restaurantes.append(nome_do_restaurante)
    print(f'\nO resturante: {nome_do_restaurante} foi cadastrado com sucesso!')
    input('Digite uma tecla para voltar para o menu principal...')
    main()

def escolher_opcao():

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()

        elif opcao_escolhida == 2:
            print('Listar Restaurante')

        elif opcao_escolhida == 3:
            print('Ativar restaurante')

        elif opcao_escolhida == 4:
                finalizar_program()
        else:
                opcao_invailida()
            
    except:
        opcao_invailida()


# aqui a gente está fazendo como se fosse a classe principal do programa
#Onde tudo vai ser executado nessa linha principal que é a do main

def main():
    os.system('cls')
    exibir_titulo()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()