# Crie um programa que o usuario digite o nome, salario e bonus, com as informações imprima a saudação com o  nome do usuario e valor da salario com o bonus
nome_usuario = input("Digiete seu nome: ")
salario = float(input("Digiete seu salario: "))
bonus_salario = float(input("Digiete seu bonus: "))
CONSTANTE_BONUS = 1000
valor_bonus = CONSTANTE_BONUS + salario * bonus_salario

print(F"O usuario {nome_usuario} possui o bonus de {valor_bonus}")