# GENERADOR DE NUMEROS PARES CON GENERADOR Y CON FUNCION NOMRLA

#PRIMERA FUNCION UE GENERA NUMEROS PARES SOLO FUNCION SIN GENERADOR

def generaPares(limite):

    num = 1

    lista1 = []

    while num < limite:
        lista1.append(num*2)
        num += 1

    return lista1

print(generaPares(10))

# NUMEROS PARES CON GENERADOR

def generaPares2(limite):

    num1=1

    while num1 < limite:

        yield  num1*2

        num1+=1

paresgen=generaPares2(10)

#
# print(paresgen)
#
# for i in paresgen:
#     print(i)

#con el metodo next para sacar el valor de un generador

print(next(paresgen))
print("Aqui podria ir mi codigo")
print(next(paresgen))
print("Aqui podria ir mi codigo")
print(next(paresgen))
print("Aqui podria ir mi codigo")