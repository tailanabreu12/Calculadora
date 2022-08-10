def calculate():
    operation = input('''
    ================ WEB ACADEMY ==================
    == Digite a operação matemática que deseja:  ==
    == + Adicao                                  == 
    == - Subtracao                               ==
    == * Multiplicacao                           ==   
    == / Divisao                                 ==
    : ''')

    number_1 = int(input('Entre com o primeiro numero: '))
    number_2 = int(input('Entre com o segundo numero: '))
    #adicao
    if operation == '+':
        print(f'O resultado de {number_1} + {number_2} é ', number_1 + number_2)

    #subtração
    elif operation == '-':
        print(f'O resultado de {number_1} - {number_2} é ', number_1 - number_2)

    #multiplicação
    elif operation == '*':
        print(f'O resultado de {number_1} * {number_2} é ', number_1 * number_2)

    #divisão
    elif operation == '/':
        print(f'O resultado de {number_1} / {number_2} é ', number_1 / number_2)
    else:
        print('Voce não escolheu uma operação válida, tente novamente.')
    again()

def again():
    calc_again = input('''
 Deseja calcular novamente?
    
 Selecione S para SIM ou N para NAO: ''')
    if calc_again.upper() == 'S':
        calculate()
    elif calc_again.upper() == 'N':
        print('Até mais!! :-)')
    else:
        again()

calculate()