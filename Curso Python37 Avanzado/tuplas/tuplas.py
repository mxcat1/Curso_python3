tupla1=("cinco",4,"hola",34)

print(tupla1)

# convertir una tupla en lista

lista1=list(tupla1)
print(lista1)

#convertir una lista en tupla

tupla2=tuple(lista1)
print(tupla2)

#metodo in
print("cinco" in tupla2)

# metodo para saber la cantidad de elementos

print(tupla2.count(4))
# metodo len para saber la logitud de una tupla

print(len(tupla2))
#tupla de un unico elemento

tuplauno=("Pedro",)
print(tuplauno," ",len(tuplauno))

# DESEMPAQUETADO DE TUPLA
tuplades=("Juan",13,1,1995)
nombre,dia,mes,anio=tuplades
print(nombre," ",dia,"/",mes,"/",anio)


#sacar el indice de un elemento de una tupla o una lista
print(tuplades.index(13))