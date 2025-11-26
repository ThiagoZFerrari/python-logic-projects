from random import randint

#Jogo de adivinhar números

numero = randint(1,10)

#Entrada de Dados
usuario = int(input('Digite um número de 1 á 10:\n'))

#Lógica e Saída de Dados
if usuario == numero:
    print(f'Número da Máquina {numero}.')
    print('Parabéns! Você acertou o número.')
else:
    print(f'Número da Máquina {numero}.')
    print('A sorte não está com você hoje! :(')