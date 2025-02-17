class Nodo:
    def __init__(self, mantenimiento):
        self.__mantenimiento = mantenimiento
        self.__siguiente = None

    @property
    def mantenimiento(self):
        return self.__mantenimiento
    @mantenimiento.setter
    def mantenimiento(self, nuevo_valor):
        self.__mantenimiento = nuevo_valor

    @property
    def siguiente(self):
        return self.__siguiente
    @siguiente.setter
    def siguiente(self, nuevo_siguiete):
        self.__siguiente = nuevo_siguiete