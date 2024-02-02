#Se le pide al usuario que ingrese una frase o serie de numeros
frase_del_usuario = input('Dime una frase o una serie de números y yo te dire si es palindromo o no: ')

#Se convierte la frase del usuario en un texto de solo letras mayúsculas, esto con la intensión de evitar confunfundir al software con la mezcla de mayúsculas y minisculas
frase_del_usuario = frase_del_usuario.upper()

#Se crea una lista y se eliminas los caracteres especiales y espacios para evitar confundir al programa (solo toma en cuenta caracteres alfanumericos)
lista_de_caracteres = list(''.join(filter(lambda char: char.isalnum(), frase_del_usuario)))

#Se realiza la comparación entre la lista y la misma lista inversa para así derterminar si es palindrome o no
if (lista_de_caracteres == lista_de_caracteres[::-1]):
    print('La frase o lista de números es exactamente palindromo')
else:
    print('La frase o lista de números no es palindromo')
