# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

m = float(input('Digite um valor em metros: '))
cm = m * 100
mm = cm * 1000
print('Centímetros: {}, Milímetros: {}'.format(cm, mm))
