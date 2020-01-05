# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Digite o preço do produto: '))
res = p - (p * 0.05)
print('Preço com desconto: {}'.format(res))