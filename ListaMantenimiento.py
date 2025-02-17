from NodoMantenimiento import Nodo

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, mantenimiento):
        nuevo_nodo = Nodo(mantenimiento)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                    actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar(self):
        if not self.cabeza:
            print("No existen registros de mantenimientos")
            return

        actual = self.cabeza
        i = 1
        while actual != None:
            print(f"{i}. Descripcion: {actual.mantenimiento.descripcion} - Fecha: {actual.mantenimiento.fecha} - Costo: {actual.mantenimiento.costo} ")
            i += 1
            actual = actual.siguiente

    def suma_costos(self):
        if not self.cabeza:
            print("No existen registros de mantenimientos")
            return

        actual = self.cabeza
        costos = 0
        while actual != None:
            costos += actual.mantenimiento.costo
            actual = actual.siguiente
        return costos