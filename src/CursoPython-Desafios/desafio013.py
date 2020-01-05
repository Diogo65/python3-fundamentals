# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input('Digite o valor do salário: '))
res = s + (s * 0.15)
print('Salário com aumento: {}'.format(res))