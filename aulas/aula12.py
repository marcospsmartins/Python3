nome = input('Qual é o seu nome? ')
altura = float(input('Qual é a sua altura? '))
peso = int(input('Qual é o seu peso? '))
imc = peso / (altura ** 2)

print(nome, ',tem ',altura, 'de altura, pesa ',peso, 'quilos e seu IMC é de ',imc)