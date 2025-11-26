# SIMULADOR DE  EMPRÉSTIMO

#Entrada de Dados
print('Bem vindo ao Simulador de Empréstimo!')
valor_casa = float(input('Digite o valor da casa: (R$)'))
salario = float(input('Digite o seu Salário: (R$)'))
anos = int(input('Digite a duração do empréstimo: (Anos)'))

#Processamento de Dados
meses = anos * 12
prestacao = valor_casa / meses
limite_aprovacao = salario * 0.3

#Saída de Dados
print(f'Limite Aprovação: R${limite_aprovacao:.2f};')
print(f'Valor da prestação: R${prestacao:.2f};')
print(f'Total de parcelas: {meses} meses.;')

#Lógica
if prestacao <= limite_aprovacao:
    print('Limite de Crédito APROVADO!')
else: 
    print('Limite de Crédito REPROVADO!')