# Faça um programa que leia algo pelo teclado e mostre na telas o seu tipo primitivo e todadas as informações possíveis

a = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Éstá em maiúscula? ', a.isupper())
print('Está em minúsculas? ', a.islower())
print('Está captalizada? ', a.istitle())
