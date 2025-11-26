#Calculadora IMC
#IMC = peso / (altura²)
#Abaixo de 18.5: Abaixo do peso
#Entre 18.5 e 24.9: Peso normal
#Entre 25 e 29.9: Sobrepeso
#Acima de 30: Obesidade


#Interface
print('--------------------')
print('-CALCULADORA - IMC-')
print('--------------------')

#Entrada de Dados
peso = float(input('Digite seu peso: ---\n'))
print('--------------------')

altura = float(input('Digite sua altura(m):\n'))
print('--------------------')

#Processamento de Dados
imc = peso / (altura**2)

#Interface
print('------SEU IMC------')

#Lógica + Saída de dados
if imc < 18.5:
    print('--Abaixo do Peso!--')
elif 18.5 <= imc <= 24.9:
    print('----Peso Normal!----')
elif  25 <= imc <= 29.9:
    print('-----Sobrepeso!-----')
else:
    print('-----Obesidade!-----')