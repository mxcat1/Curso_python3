# lo mismo que un array

lista1=[1,2,3,4,5,6]
lista2=[8,9]
print(lista1[:])
lista1.append(7)
print(lista1[:])
lista1.extend([8,9])
print(lista1[:])
lista1.remove(lista1[8])
print(lista1[:])
lista1.pop()
print(lista1[:])

lista3=lista1+lista2

print(lista3[:])
