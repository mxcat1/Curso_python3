class Coche():
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False

    def arrancar(self):
        self.enmarcha=True

    def estado(self):
        if (self.enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta apagado"

micoche = Coche()

print(f"El largo del coche es : %s" % (micoche.largoChasis))
print(f"El coche tiene %s ruedas" % (micoche.ruedas))
print(f" %s" % (micoche.estado()))
micoche.arrancar()
print(f" %s" % (micoche.estado()))

