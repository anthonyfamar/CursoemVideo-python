#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Digite seu salário R$ '))
if salario <= 1250:
    novo_salario = 0.15 * salario + salario
else:
    novo_salario = 0.10 * salario + salario
print(f'Seu novo salário será de R$ {novo_salario:.2f}')