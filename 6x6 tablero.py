import numpy as np
import random as rnd

def tableroparejas(n):
    fichasunicas = (n*n)//2
    tablero = np.zeros(shape=(n,n),dtype =int)

    i = 1
    while i<=fichasunicas:
        f1 = int(rnd.random()*n)+0
        c1 = int(rnd.random()*n)+0
        while not(tablero[f1,c1]==0):
            f1 = int(rnd.random()*n)+0
            c1 = int(rnd.random()*n)+0
        tablero[f1,c1] = i
        f2 = int(rnd.random()*n)+0
        c2 = int(rnd.random()*n)+0
        while not(tablero[f2,c2]==0):
            f2 = int(rnd.random()*n)+0
            c2 = int(rnd.random()*n)+0
        tablero[f2,c2] = i
        i = i + 1
    return(tablero)

n = 6

tablero = tableroparejas(n)
descubiertas = np.zeros(shape=(n,n),dtype=int)
equivocado = 0
encontrado = 0
while (encontrado<(n*n)):
    
    print('estado del juego:')
    print(descubiertas)

    f1 = int(input('fila ficha1:'))
    c1 = int(input('columna ficha1:'))
    while not(descubiertas[f1,c1]==0):
        f1 = int(input('fila ficha1:'))
        c1 = int(input('columna ficha1:'))

    f2 = int(input('fila ficha2:'))
    c2 = int(input('columna ficha2:'))
    while not(descubiertas[f2,c2]==0):
        f2 = int(input('fila ficha2:'))
        c2 = int(input('columna ficha2:'))

    ficha1 = tablero[f1,c1]
    ficha2 = tablero[f2,c2]

    if ficha1==ficha2:
        descubiertas[f1,c1] = ficha1
        descubiertas[f2,c2] = ficha2
        encontrado = encontrado + 2
        print('ENCONTRO una pareja..!',ficha1,ficha2)
    else:
        equivocado = equivocado + 1
        print('Las fichas son diferentes: ',ficha1,ficha2)

print('Solucion del tablero:')
print(tablero)
print('Estado del juego:')
print(descubiertas)
if encontrado==(n*n):
    print(' Muy bien..!! todas las fichas encontradas')