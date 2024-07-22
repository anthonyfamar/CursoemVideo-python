frase = 'Curso em Video Python'
print(frase.replace('Python', 'Android')) #procura 'python' e substitui por 'android'
print(frase.upper()) #deixa tudo maiusculo
print(frase.lower()) #deixa tudo minusculo
print(frase.capitalize()) #só o primeiro maiusculo)
print(frase.title()) #primeira letra de cada palavra

frase2 = '   Aprenda Python  '
print(frase2.strip()) #remove os espaços desnecessários no inicio e no final
print(frase2.rstrip()) #remove os espaços do lado direito(final)
print(frase2.lstrip()) #remove os espaços do lado esquerdo(começo)