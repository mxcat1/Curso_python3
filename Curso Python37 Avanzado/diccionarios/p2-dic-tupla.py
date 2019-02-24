tupla1=["España","Francia","Reino Unido","Alemania"]
diccionario1={tupla1[0]:"Madrid",tupla1[1]:"Paris",tupla1[2]:"Londres",tupla1[3]:"Berlin"}
print(diccionario1)
#tupla y diccionarios unidos

diccionario2={"Anillos":[1991,1992,1993,1996,1997,1998],"Anillos2":{"Temporadas2":[1991,1992,1993,1996,1997,1999]}}
print(diccionario2["Anillos"])
print(diccionario2["Anillos"][0])

# adiccionario dentro de un diccionario con una tupla

print(diccionario2["Anillos2"]["Temporadas2"])

# imprimir los indices del diccionario

print(diccionario2.keys())

# solo valores

print(diccionario2.values())

#cantidad de valores en un diccionario

print(len(diccionario2))