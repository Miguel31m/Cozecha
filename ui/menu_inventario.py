from tools.tools_ui.limpiar_pantalla import limpiar_terminal
import os
import sys

def _configurar_entorno_de_rutas_del_sistema_externo():
   
    ruta_raiz = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    if ruta_raiz not in sys.path:
        sys.path.append(ruta_raiz)

_configurar_entorno_de_rutas_del_sistema_externo()

from service.service_ui.seleccionar_tipo import SeleccionarTipoProducto

class MenuInventario:
    def __init__(self, funciones_inventario):
        self.funciones = funciones_inventario
        self.selector = SeleccionarTipoProducto(self.funciones)

    def mostrar_interfaz_inventario(self):
        while True:
            limpiar_terminal()
            print("\n", "=" * 10, "GESTION DE INVENTARIO", "=" * 10)
            print("-1. AGREGAR FERTILIZANTE")
            print("-2. AGREGAR CONTROL DE PLAGA")
            print("-3. AGREGAR ANTIBIOTICO")
            print("-4. CONSULTAR INVENTARIO COMPLETO")
            print("-5. VOLVER AL MENU PRINCIPAL")
            print("=" * 43)
            
            try:
                opcion_inventario = int(input("\nSeleccione una opcion: "))
                if opcion_inventario == 5:
                    break
                self.selector.redireccionar_alta_producto(opcion_inventario)
            except ValueError:
                print("Error: Ingrese un numero valido.")
                input("Presione Enter para continuar...")


