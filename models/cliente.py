class Cliente:
    def __init__(self, **kwargs):
        self._nombre_cliente = kwargs.get("nombre_cliente", "Usuario externo")
        self._id_cliente = kwargs.get("id_cliente", "AAA111")
     
    @property
    def nombre_cliente(self):
        return self._nombre_cliente

    @property
    def id(self):
        return self._id_cliente