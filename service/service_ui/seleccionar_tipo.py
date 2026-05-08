import os
import sys

def _configurar_entorno_de_rutas_del_sistema_externo():
   
    ruta_raiz = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    if ruta_raiz not in sys.path:
        sys.path.append(ruta_raiz)

_configurar_entorno_de_rutas_del_sistema_externo()

from models.models_producto.antibiotico import Antibiotico
from models.models_producto.fertilizante import Fertilizantes
from models.models_producto.control_plaga import ControlPlaga

class SeleccionarTipoProducto:
    def __init__(self, funciones_inventario):
        self.funciones = funciones_inventario

    def redireccionar_alta_producto(self, opcion):
        if opcion == 4:
            self.funciones.consultar_inventario()
            input("Presione Enter para continuar...")
            return

      
        nombre = input("Nombre del producto: ")
        try:
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad a ingresar: "))
            
            if opcion == 1: 
                ica = input("Registro ICA: ")
                frecuencia = int(input("Frecuencia de aplicacion: "))
                fecha = input("Fecha última aplicación (DD/MM/YYYY): ")
                producto = Fertilizantes(nombre_producto=nombre, precio_producto=precio, 
                                        registro_ICA=ica, frecuencia_aplicacion=frecuencia, 
                                        fecha_ultima_aplicacion=fecha)
                
            elif opcion == 2: 
                ica = input("Registro ICA: ")
                frecuencia = int(input("Frecuencia de aplicación: "))
                carencia = int(input("Periodo de carencia: "))
                producto = ControlPlaga(nombre_producto=nombre, precio_producto=precio, 
                                       registro_ICA=ica, frecuencia_aplicacion=frecuencia, 
                                       periodo_carencia=carencia)
                
            elif opcion == 3: 
                dosis = float(input("Dosis (400-600): "))
                animal = input("Tipo de animal: ")
                producto = Antibiotico(nombre_producto=nombre, precio_producto=precio, 
                                      dosis=dosis, tipo_animal=animal)
            else:
                print("Opción no valida.")
                return

            
            self.funciones.agregar_producto(producto, cantidad)
            input("\nPresione Enter para continuar...")

        except ValueError as error:
            print(f"Error en los datos ingresados: {error}")
            input("Presione Enter para reintentar...")