'''
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata-Frita')
print(sorted(lanche)) # sorted() Coloca em ordem albética ou númerica
print(lanche)

# 1 Forma
for comida in lanche:
    print(f'Eu vou comer {comida}')
# 2 Forma
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
# 3 Forma
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi bastante!')
'''

# Tuplas são imutáveis
# lanche[1] = 'Refrigerante' - Não funciona em tupla!

#print(lanche[2])
#print(len(lanche))

'''
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(sorted(c))
print(len(c))
print(c.count(5)) # Quantidade de 5 no 'c'
print(c.index(8)) # Index mostra a posição do item
'''

pessoa = ('Ian', 24, 'M', 59.10, 'Dev. Back End', 'Need a portifolio')
print(pessoa)
