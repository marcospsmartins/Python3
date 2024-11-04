nome = input('Qual é o seu nome? ')
altura = float(input('Qual é a sua altura? '))
peso = float(input('Qual é o seu peso? '))
imc = peso / (altura ** 2)

print(f'{nome} tem {altura} de altura pesa {peso} kg e seu IMC é de {imc:.2f}')