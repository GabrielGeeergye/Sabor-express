print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░\n""")

print('1. Cadastrar restaurante')
print('2. Listar restaurante')
print('3. Ativar restaurante')
print('4. Sair')

#Criando uma variavel
#Nele não é necessário colocar o tipo da variavel
opcao_escolhida = int(input('Escolha uma opção: '))

# Diferença do "" e '', defini uma para o projeto
# É do time, e não de algo diferente

# Interpolação está abaixo
print(f'Você escolheu a opção:{opcao_escolhida}')

#Retornar tipo da var
#print(type(opcao_escolhida))

if opcao_escolhida == 1:
    print('Cadastrar Restaurante')
elif opcao_escolhida == 2:
    print('Listar Restaurante')
elif opcao_escolhida == 3:
    print('Ativar restaurante')
else:
    print('Encerrar programa')
