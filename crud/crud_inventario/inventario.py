from .data_inventario import dato_inventario_producto

class Inventario:
    def __init__(self):
      
        self._dato_inventario = dato_inventario_producto["productos"]

    @property
    def dato_inventario(self):
        return self._dato_inventario