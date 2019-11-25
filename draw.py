from random import *

listaP =[]
splited = []
draw1 = []
draw2 = []
lista1 = []
lista2 = []

def draw():
    x = len(lista1)-1
    y = len(lista1)-1
    if len(lista1) == len(lista2):
        for i in range (len(lista1)):
            print(lista1[draw1[x-i]]+' fará par com ' + lista2[draw2[y-i]])
    else:
        print('A quantidade de elementos das duas lista tem que ser igual')
         
def teste():
    p = input("Coloque o numero de pessoas,ele tem que ser par!!: ")
    for j in range(0,int(p)):
        listaP.append(input())
        
    splited = [listaP[i::2] for i in range(2)] 
    lista1 = splited[0]
    lista2 = splited[1]
    
    while len(draw1) != len(lista1):
        c = randint(0,len(lista1)-1)
        if c not in draw1:
            draw1.append(c)
            
    while len(draw2) != len(lista1):
        z = randint(0,len(lista1)-1)
        if z not in draw2:
            draw2.append(z)

    return lista1,lista2


lista1,lista2 = teste()
print('\n')
draw()
print('\n')

