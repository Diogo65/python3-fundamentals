# Faça um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.

n = float(input('Digite quanto dinheiro voçê possui na carteira: '))
dolar = n / 4.07

print('Voce pode comprar {:.2f} dólares'.format(dolar))