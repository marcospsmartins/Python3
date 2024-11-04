nome = input('Qual é o seu nome? ')
altura = float(input('Qual é a sua altura? '))
peso = float(input('Qual é o seu peso? '))
imc = peso / (altura ** 2)

print('{} tem {} de altura pesa {} kg e seu IMC é de {:.2f}'.format(nome, altura, peso, imc))