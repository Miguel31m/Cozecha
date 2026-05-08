class Producto:
    def __init__(self, **kwargs):
       
        defaults_producto = {
            "nombre_producto": "Producto genérico",
            "precio_producto": 0.0,
            "cantidad_producto": 0
            
        }
      
        defaults_producto.update(kwargs)

       
        self._nombre = defaults_producto["nombre_producto"]
        self._valor = defaults_producto["precio_producto"]
        self._cantidad = defaults_producto["cantidad_producto"]
        

    @property
    def nombre_producto(self):
        return self._nombre  
    
    @property
    def cantidad_producto(self): 
        return self._cantidad
    
    @cantidad_producto.setter
    def cantidad_producto(self, valor):
        if valor >= 0:
            self._cantidad = valor
        else:
            print("La cantidad no puede ser negativa")

    @property    
    def precio_producto(self):
        return self._valor   