
def multiplos_ambos(a):
    """
    Função que retorna multiplos de 5 e 7
    """
    try:
        if (a % 5 == 0) and (a % 7 == 0):
            return 'fizzbuzz'
        else:
            return 'Número digitado não é múltiplo de 5 e nem de 7!'
    except TypeError as e:
        return f'Você precisa informar um número natural. Por favor, digite um número positivo e inteiro! - {e}'


def multiplos5(a):
    """ 
    Função que retorna multiplos de 5
    """
    try:
        if a % 5 == 0:
            return 'fizz'
        else:
            return 'Número digitado não é múltiplo de 5!'
    except TypeError as e:
        return f'Você precisa informar um número natural. Por favor, digite um número positivo e inteiro! - {e}'


def multiplos7(a):
    """
    Função que retorna multiplos de 7
    """
    try:
        if a % 7 == 0:
            return 'buzz'
        else:
            return 'Número digitado não é múltiplo de 7!'
    except TypeError as e:
        return f'Você precisa informar um número natural. Por favor, digite um número positivo e inteiro! - {e}'


def multiplos_vazio(a):
    """
    Função que retorna quando o número não é múltiplo de 5 nem de 7
    """
    try:
        if (a % 7 != 0) and (a % 7 != 0):
            return 'miss'
    except TypeError as e:
        return f'Você precisa informar um número natural. Por favor, digite um número positivo e inteiro! - {e}'
    return None


def main():
    """
    Função principal que obtém a entrada do usuário e chama as funções de verificação.
    """
    try:
        a = int(input('Digite um número natural: '))
        
        print(multiplos_ambos(a))
        print(multiplos5(a))
        print(multiplos7(a))
        print(multiplos_vazio(a))
        
    except ValueError:
        print('Você precisa informar um número natural. Por favor, digite um número positivo e inteiro!')


if __name__ == '__main__':
    main()
