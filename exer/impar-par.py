#Aqui recebe o número digitado pelo o usuario
def recebendo_numero ():
    num_digitado = (input(('\nDigite um número inteiro: ')))
    return num_digitado

# Aqui verficar se o número é impar ou par
def verificar_numero(num):
    num_digitado = int(num)
    if (num_digitado%2==0):
        return print(f'\nO número: {num_digitado} é par\n')
    else:
        return print(f'\nO número: {num_digitado} é impar\n')

def main():
    
    num = int(recebendo_numero())
    verificar_numero(num)


if __name__ == '__main__':
    main()