
import os
import sys

def _configurar_entorno_de_rutas_del_sistema_externo():
    ruta_raiz = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    if ruta_raiz not in sys.path:
        sys.path.append(ruta_raiz)

_configurar_entorno_de_rutas_del_sistema_externo()

from tools.tools_ui.limpiar_pantalla import limpiar_terminal
from service.service_ui.seleccionar_opcion_facturacion import SeleccionarOpcionFacturacion

class MenuFacturacion:
    def __init__(self, funciones_inventario):
    
        self.funciones_inv = funciones_inventario
        self.selector = SeleccionarOpcionFacturacion(self.funciones_inv)

    def mostrar_interfaz_facturacion(self):
        while True:
            limpiar_terminal()
            print("\n", "=" * 10, "MODULO DE FACTURACION", "=" * 10)
            print("-1. CREAR PEDIDO")
            print("-2. CONSULTAR HISTORIAL DE CLIENTE")
            print("-3. VOLVER AL MENU PRINCIPAL")
            print("=" * 43)
            
            try:
                opcion_facturacion = int(input("\nSeleccione una opcion: "))
                if opcion_facturacion == 3:
                    break
                self.selector.ejecutar_accion(opcion_facturacion)
            except ValueError:
                print("Error: Ingrese un numero válido.")
                input("Presione Enter para continuar...")