operation = input('''
Digite a operação matemática que deseja:
+ Adicao
- Subtracao
* Multiplicacao
/ Divisao
''')

number_1 = int(input('Entre com o primeiro numero: '))
number_2 = int(input('Entre com o segundo numero: '))

if operation == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

#subtração
elif operation == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

#multiplicação
elif operation == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)

#divisão
elif operation == '/':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)
else:
    print('Voce não escolheu uma operação válida, tente novamente.')