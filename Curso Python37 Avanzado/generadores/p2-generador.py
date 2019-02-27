
#ç
#¡GENERADORES 2 GENERADORES CON BUCLES ANIDADOS

def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        # for subelemento in elemento:
        # yie/8d from en vez de usar otro bucle anidado
        yield from elemento

ciudades_devueltas=devuelve_ciudades("Arequipa","Barcelona","Bilbao","Valencia")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))