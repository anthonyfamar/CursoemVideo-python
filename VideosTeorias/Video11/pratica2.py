a = 3
b = 5
print(f'Os valores são \33[32m{a}\033[m e \033[31m{b}\033[m!')

nome = 'Python'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
        'pretoebranco':'\033[7;107m'}

print(f'Olá {cores["azul"]}{nome}{cores["limpa"]}')