class mesa():

    # Constructor
    # ENCAPSULACION
    def __init__(self):
        self.material = "Roble"
        self.__patas = 4
        self.anchoMesa = 150
        self.largoMesa = 200

    def estadomesa(self):
        return f"La mesa tiene %s Patas" % (self.__patas)

    def __funcionencapsuladaq(self):
        pass


mimesa=mesa()
mimesa.patas=8
print(f"%s" %(mimesa.estadomesa()))