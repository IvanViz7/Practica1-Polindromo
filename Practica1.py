#Se le pide al usuario que ingrese una frase o serie de numeros
frase_del_usuario = input('Dime una frase o una serie de números y yo te dire si es palindromo o no: ')

#Se cuentan los caracteres alfanumericos que el usurario 
cantidad_de_caracteres = len(''.join(filter(lambda char: char.isalnum(), frase_del_usuario)))
print(cantidad_de_caracteres)

#Los caracteres alfanumericos de frase_de_usuario se pasan a una lista
lista_de_caracteres = list(''.join(filter(lambda char: char.isalnum(), frase_del_usuario)))
lista_reverse = lista_de_caracteres
lista_reverse.reverse()

if (lista_de_caracteres == lista_reverse):
    print('La frase o lista de números es exactamente palindromo')
else:
    print('La frase o lista de números no es palindromo')
