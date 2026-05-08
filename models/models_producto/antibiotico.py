from .producto import Producto

class Antibiotico(Producto):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._dosis = kwargs.get("dosis", 400.0)
        self._tipo_animal = kwargs.get("tipo_animal", "Bovinos, caprinos o porcinos")
    
    @property
    def dosis(self):
        return self._dosis

    @dosis.setter
    def dosis(self, valor):
        # Validador solicitado en tu lógica
        if 400 <= valor <= 600:
            self._dosis = valor
        else:
            print("Dosis no permitida")
    
    @property
    def tipo_animal(self):
        return self._tipo_animal