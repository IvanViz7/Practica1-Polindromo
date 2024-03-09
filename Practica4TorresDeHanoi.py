n = 3
movimientos_minimos_requeridos = 2 ** n -1
print(f'El número de movimientos minimos por {n} discos son: {movimientos_minimos_requeridos} movimientos')

def torre_hanoi(n, origen, destino, auxiliar):
    if (n == 1):
        print(f'Mueve Disco {n} de {origen} a {destino}')
        return
    torre_hanoi(n-1, origen, auxiliar, destino)
    print(f'Mueve Disco {n} de {origen} a {destino}')
    torre_hanoi(n-1, auxiliar, destino, origen)
        
torre_hanoi(n, 'A', 'C', 'B')
#(3, A, C ,B)
#(2, A, B, C)
#(1, A, C, B)