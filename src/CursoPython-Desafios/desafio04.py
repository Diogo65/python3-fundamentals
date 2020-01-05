#Faça um programa que leia algo pelo teclado e mostra na tela o seu tipo primitivo e todas as informalções possíveis sobre ela

n = input('Digite algo: ')

#varifica se é um número
print(n.isnumeric())

#verifica se é alfabético
print(n.isalpha())

#verifica se é alfabético e numérico
print(n.isalnum())

#verifica se é maiscúclo
print(n.isupper())