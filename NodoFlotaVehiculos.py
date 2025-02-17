class Nodo:
    def __init__(self, nuevo_vehiculo):
        self.__vehiculo = nuevo_vehiculo
        self.__siguiente = None

    @property
    def vehiculo(self):
        return self.__vehiculo
    @vehiculo.setter
    def vehiculo(self, nuevo_valor):
        self.__vehiculo = nuevo_valor

    @property
    def siguiente(self):
        return self.__siguiente
    @siguiente.setter
    def siguiente(self, nuevo_siguiete):
        self.__siguiente = nuevo_siguiete