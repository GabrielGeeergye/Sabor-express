import os

restaurantes = [{'nome' : 'Praça', 'categoria': 'Japonesa', 'ativo':False}]

def  exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

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
    exibir_subtitulo('Cadastrar novos restaurantes')
    nome_do_restaurante = input('\nDigite o nome do restaurante que você deseja cadastrar: ')
    
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')

    dados_do_restaurnate = {'nome':nome_do_restaurante, 
    'categoria': categoria, 'ativo':False}
    
    
    restaurantes.append(dados_do_restaurnate)
    print(f'\nO resturante: {nome_do_restaurante} foi cadastrado com sucesso!')
    input('Digite uma tecla para voltar para o menu principal...')
    main()

def listar_restaurante():
    os.system('cls')
    exibir_subtitulo('Listando restaurantes')

    for restaurante in restaurantes:
        nome_do_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'

        print(f'- {'Nome'.ljust(20)}| {'Categoria'.ljust(20) } | {'Ativo'.ljust(20) }')
        print(f'- {nome_do_restaurante.ljust(20) }| {categoria.ljust(20) } | {ativo.ljust(20) }')

    input('Digite uma tecla para voltar para o menu principal...')
    main()

def  alterar_estado_restaurante():
    exibir_subtitulo('ALterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    main()


def escolher_opcao():

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()

        elif opcao_escolhida == 2:
           listar_restaurante()

        elif opcao_escolhida == 3:
            alterar_estado_restaurante()

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