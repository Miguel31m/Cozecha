from .producto_control import ProductoControl

class Fertilizantes(ProductoControl):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._fecha_ultima_aplicacion = kwargs.get("fecha_ultima_aplicacion", "01/01/2026")
    
    @property
    def fecha_ultima_aplicacion(self):
        return self._fecha_ultima_aplicacion