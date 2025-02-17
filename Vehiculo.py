from datetime import datetime
from ListaMantenimiento import ListaEnlazada
from Mantenimiento import Mantenimiento
import re
class Vehiculo:
    def __init__(self, placa, marca, modelo, anio, kilometraje):
        self._placa = None
        self._anio = None
        self._kilometraje = None

        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = kilometraje
        self.lista_mantenimientos = ListaEnlazada()

    @property
    def placa(self):
        return self._placa

    @placa.setter
    def placa(self, valor_placa):
        if re.fullmatch(r"[A-Z]{3}\d{2}", valor_placa):
            self._placa = valor_placa
        else:
            raise ValueError("No ingresaste un número de placa válido. ")

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, valor_anio):
        fecha = datetime.now().year
        if valor_anio < 1900 or valor_anio > fecha:
            raise ValueError("No ingresaste un año valido. ")
        self._anio = valor_anio

    @property
    def kilometraje(self):
        return self._kilometraje

    @kilometraje.setter
    def kilometraje(self, valor_kilometraje):
        if valor_kilometraje <= 0:
            raise ValueError("El kilometraje debe ser un numero positivo ")
        self._kilometraje = valor_kilometraje

    def agregar_mantenimiento(self):
        fecha = input("Ingresa una fecha en formato YYYY-MM-DD: ")
        descripcion = input("Ingresa una descripcion: ")
        costo = int(input("Ingresa el costo del mantenimiento: "))

        nuevo_mantenimiento = Mantenimiento(fecha, descripcion, costo)
        self.lista_mantenimientos.insertar(nuevo_mantenimiento)

    def consultar_matenimientos(self):
        self.lista_mantenimientos.mostrar()

    def consultar_costos_mantenimiento(self):
        costos = self.lista_mantenimientos.suma_costos()
        print(f"El total de los costos de mantenimientos es {costos}" )