#Este código calcula tu edad
#año_de_nacimiento = int(input("¿En que año naciste? "))
#mes_de_nacimiento = int(input("¿En que mes es tu cuempleaños en digitos? "))
#año_corriente = 2024
#mes_corriente = 2
# edad = año_corriente - año_de_nacimiento

#if (mes_de_nacimiento >= mes_corriente):
#    edad = edad - 1

#print(f'Tienes {edad} años de edad')

##Covertidor de temperatura
##celcius = int(input('Introduce una temperatura que quieras convertir de ° Celcius a ° Fahrenheits: '))
##fahrenheit = celcius * (9/5) + 32
##print(f'La conversión de {celcius}°C a Fahrenheits es de: {fahrenheit}°F')

###Contador de palabras
###frase = input('Ingresa una frase y este programa te ayudará a contar las palabras: ')
###palabras = len(frase.split())
###print(f'Tu frase cuenta con {palabras} palabras')

####Sumador de números pares
####nume = 100
####num = 1
####suma = 0
####while num <= nume:
####    num += 1
####    if(num%2 == 0):
####        suma = suma + num
####
####print(f'{suma}')
    
####Sumador de números pares Chat GPT    
def suma_numeros_pares():
    suma = 0
    for numero in range(2, 101, 2):
        suma += numero
    return suma

resultado = suma_numeros_pares()
print('La suma de todos los números pares del 1 al 100 es:', resultado)







   # Suma de números pares: Escribe un programa que sume todos los números pares del 1 al 100 e imprima el resultado.

    #Cálculo del factorial: Escribe una función que calcule el factorial de un número dado. El factorial de un número n se define como el producto de todos los enteros positivos menores o iguales a n. Por ejemplo, el factorial de 5 (denotado como 5!) es 5 * 4 * 3 * 2 * 1.

    #Adivina el número: Crea un juego donde el programa elija un número aleatorio entre 1 y 100, y luego pida al usuario que adivine el número. Proporciona pistas como "más alto" o "más bajo" según sea necesario hasta que el usuario adivine correctamente.

    #Cuenta regresiva: Escribe un programa que solicite al usuario ingresar un número y luego imprima una cuenta regresiva desde ese número hasta 0.

    #Calculadora de áreas: Crea un programa que permita calcular el área de diferentes formas geométricas, como círculos, triángulos y rectángulos. Pide al usuario que elija la forma y luego ingrese los valores necesarios para el cálculo