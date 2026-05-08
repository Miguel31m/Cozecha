from .producto import Producto

class ProductoControl(Producto):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._registro_ICA = kwargs.get("registro_ICA", "AAAAAA")
        self._frecuencia_aplicacion = kwargs.get("frecuencia_aplicacion", 0)
        
    @property
    def registro_ICA(self):
        return self._registro_ICA

    @property
    def frecuencia_aplicacion(self):
        return self._frecuencia_aplicacion