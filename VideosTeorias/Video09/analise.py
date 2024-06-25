frase = 'Curso em Video Python'
print(len(frase))
print(frase.count('o')) #conta quantos o tem na frase
print(frase.count('o', 0, 13)) #contar quantos 'o' ele acha do 0 ao 13
print(frase.find('deo')) #onde ele entra a frase "deo"
print(frase.find('Android')) #volta -1 pois é uma string q n existe
print('Curso' in frase) #existe a palavra 'curso' na frase?