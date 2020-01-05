# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária
# para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m^2.

l = float(input('Digite a Largura: '))
h = float(input('Digite a Altura: '))
a = (l * h) / 2

print('Será necessário {} Litros de tinta para pintar a parede'.format(a))