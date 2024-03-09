def factorial(numero):
    num_factorial = numero
    while numero > 1:
        num_factorial = num_factorial * (numero - 1)
        numero -= 1
    return num_factorial
numero = int(input('Introduce un número para calcular su factorial: '))
resultado = factorial(numero)
print(f'{resultado}')    