from NodoFlotaVehiculos import Nodo

class FlotaVehiculos():
    def __init__(self):
        self.__cabeza = None
        self.__final = None
        self.__contador = 0
        self.__actual = None

    def insertar_vehiculo(self, nuevo_vehiculo):
        nuevo_nodo_vehiculo = Nodo(nuevo_vehiculo)

        if not self.__cabeza:
            self.__cabeza = nuevo_nodo_vehiculo
            self.__final = nuevo_nodo_vehiculo
            nuevo_nodo_vehiculo.siguiente = nuevo_nodo_vehiculo
            self.__actual = nuevo_nodo_vehiculo
        else:
            nuevo_nodo_vehiculo.siguiente = self.__cabeza
            self.__final.siguiente = nuevo_nodo_vehiculo
            self.__final = nuevo_nodo_vehiculo

        self.__contador += 1

    def mostrar_vehiculos(self):

        actual = self.__cabeza
        while True:
            print(f"Placa: {actual.vehiculo.placa} - Marca: {actual.vehiculo.marca} - Modelo: {actual.vehiculo.modelo} "
                  f"- Año: {actual.vehiculo.anio} - Kilometraje: {actual.vehiculo.kilometraje}")
            actual = actual.siguiente
            if actual == self.__cabeza:
                break

    def buscar_vehiculo(self, placa):
        actual = self.__cabeza
        while actual.vehiculo.placa != placa:
            actual = actual.siguiente
            if actual == self.__cabeza:
                break

        return actual.vehiculo

    def eliminar_vehiculo(self, placa):
        temp = self.__cabeza
        previo = None

        while True:
            if temp.vehiculo.placa == placa:
                eliminado = temp
                if temp == self.__cabeza and temp.siguiente == self.__cabeza:
                    self.__cabeza = None
                elif temp == self.__cabeza:
                    self.final = self.__cabeza
                    while self.__final.siguiente != self.__cabeza:
                        self.__final = self.final.siguiente
                    self.cabeza = self.__cabeza.siguiente
                    self.__final.siguiente = self.__cabeza
                else:
                    previo.siguiente = temp.siguiente

                print(f"Vehiculo con placa {eliminado.vehiculo.placa}, marca {eliminado.vehiculo.marca} "
                      f"y modelo {eliminado.vehiculo.modelo}, eliminado correctamente de la flota.")

                return
            previo = temp
            temp = temp.siguiente
            if temp == self.__cabeza:
                break

        print("El numero de placa no existe dentro de la flota.")

    def esta_vacia(self):
        return self.__cabeza is None