# Crie um algoritmo que leia um número e mostre o seu dobro, triplo, e rais quadrada.

n = int(input('Digite um número: '))
dobro = n * 2
triplo = n * 3
#raiz = n ** (1/2)
raiz = pow(n, (1/2))

print('Dobro: {}, \nTriplo: {}, \nRaiz: {:.2f}'.format(dobro, triplo, raiz))