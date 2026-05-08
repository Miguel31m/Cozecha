from .producto_control import ProductoControl

class ControlPlaga(ProductoControl):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._periodo_carencia = kwargs.get("periodo_carencia", 0)
    
    @property
    def periodo_carencia(self):
        return self._periodo_carencia