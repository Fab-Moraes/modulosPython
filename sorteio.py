import random
'''
n1 = input('Primeiro Aluno:  ')
n2 = input('Segundo aluno:  ')
n3 = input('Terceiro aluno:  ')
n4 = input('Quarto aluno:  ')

lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)

print(f'O aluno escolhido foi: {escolhido}')
'''



# Agora pra fazer a escolha e mostrar a ordem de apresentação

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')

lista = [n1,n2,n3,n4]
random.shuffle(lista)

print(f'A ordem de apresentação será: {lista}')