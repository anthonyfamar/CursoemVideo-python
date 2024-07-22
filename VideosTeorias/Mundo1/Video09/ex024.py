#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO"
cidade = str(input('Digite o nome da cidade: ')).strip()
separado = cidade.split()
print(f'A cidade começa com santo?? {'SANTO' in separado[0].upper()}')

#ou

#cid = str(input('Digite o nome da cidade: ')).strip()
#print(cid[:5].upper() == 'SANTO')