from datetime import datetime

class Mantenimiento:
    def __init__(self, fecha, descripcion, costo):
        self._fecha = None
        self._costo = None

        self.fecha = fecha
        self.descripcion = descripcion
        self.costo = costo

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, dato_fecha):
        try:
            fecha = datetime.strptime(dato_fecha, "%Y-%m-%d").date()
            self._fecha = fecha
        except ValueError:
            raise ValueError("Error: La fecha ingresada no es válida. Debe estar en formato YYYY-MM-DD.")

    @property
    def costo(self):
        return self._costo

    @costo.setter
    def costo(self, valor_costo):
        if valor_costo <= 0:
            raise ValueError("El costo debe ser un numero positivo")
        self._costo = valor_costo