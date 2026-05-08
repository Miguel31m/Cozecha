import sys
import os

def _configurar_entorno_de_rutas_del_sistema_externo():
   
    ruta_raiz = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    if ruta_raiz not in sys.path:
        sys.path.append(ruta_raiz)

_configurar_entorno_de_rutas_del_sistema_externo()

from models.cliente import Cliente
from models.models_producto.antibiotico import Antibiotico
from models.models_producto.fertilizante import Fertilizantes
from models.models_producto.control_plaga import ControlPlaga
from models.models_producto.producto_control import ProductoControl 
from crud.crud_inventario.inventario import Inventario


class FuncionesInventario:
    
    def __init__(self, inventario):
        self.inventario = inventario

    def agregar_producto(self, producto, cantidad_a_sumar):
      
        if cantidad_a_sumar <= 0:
            print("Error: La cantidad a agregar debe ser mayor a cero.")
            return

        nombre_producto = producto.nombre_producto
        
        
        if nombre_producto in self.inventario.dato_inventario:
           
            self.inventario.dato_inventario[nombre_producto]["cantidad"] += cantidad_a_sumar
            print(f"Inventario actualizado: {nombre_producto}. Cantidad total: {self.inventario.dato_inventario[nombre_producto]['cantidad']}")
        else:
       
            self.inventario.dato_inventario[nombre_producto] = {
                "cantidad": cantidad_a_sumar,
                "detalles": self._extraer_informacion(producto)
            }
            print(f"Nuevo producto registrado: {nombre_producto} . Cantidad total {cantidad_a_sumar} unidades.")

    def consultar_inventario(self):
        
        print("\n" + "="*50)
        print(f"{'PRODUCTO':<20} | {'CANTIDAD':<10} | {'INFORMACION'}")
        print("-" * 50)
        
        if not self.inventario.dato_inventario:
            print("El inventario esta vacío.")
        else:
            for nombre_producto, informacion_producto in self.inventario.dato_inventario.items():
                cantidad_inventario = informacion_producto["cantidad"]
                informacion_producto = informacion_producto["detalles"]
                print(f"{nombre_producto:<20} | {cantidad_inventario:<10} | {informacion_producto}")
        
        print("="* 50 + "\n")

    def _extraer_informacion(self, producto):
     
        informacion_producto = {"precio": producto.precio_producto}
    
        if hasattr(producto, 'registro_ICA'):
            informacion_producto["ICA"] = producto.registro_ICA
            informacion_producto["frecuencia"] = producto.frecuencia_aplicacion
        
    

        if isinstance(producto, Fertilizantes):
            informacion_producto["ultima_aplicacion"] = producto.fecha_ultima_aplicacion
        elif isinstance(producto, ControlPlaga):
            informacion_producto["carencia"] = producto.periodo_carencia
        elif isinstance(producto, Antibiotico):
            informacion_producto["dosis"] = producto.dosis
            informacion_producto["tipo_animal"] = producto.tipo_animal
            
        return informacion_producto
    



