import os
import sys

def _configurar_entorno_de_rutas_del_sistema_externo():
    
    ruta_raiz = os.path.dirname(os.path.dirname(__file__))
    if ruta_raiz not in sys.path:
        sys.path.append(ruta_raiz)

_configurar_entorno_de_rutas_del_sistema_externo()


from tools.tools_ui.limpiar_pantalla import limpiar_terminal
from ui.saliendo_programa import saliendo_del_programa
from ui.menu_inventario import MenuInventario
from ui.menu_facturacion import MenuFacturacion  


from crud.crud_inventario.inventario import Inventario
from crud.crud_inventario.funciones_productos import FuncionesInventario

class MostrarMenuPrincipal:

    def __init__(self):
        
        self.inventario = Inventario()
        self.funcion_inventario = FuncionesInventario(self.inventario)
        
        
        self.menu_inventario = MenuInventario(self.funcion_inventario)
        self.menu_facturacion_inventario = MenuFacturacion(self.funcion_inventario)

    def ejecutar_interfaz_menu_principal(self):
       
        selector_opcion = SeleccionarMenuPrincipal(self.menu_inventario, self.menu_facturacion_inventario)
        
        while True:
            self._limpiar_pantalla_externa()
            self._dibujar_interfaz()
            
            resultado = selector_opcion.gestionar_entrada_usuario()

            if resultado == "salir_del_programa":
                break
    
    def _dibujar_interfaz(self):
        print("\n", "=" * 10, "CO-ZECHA SYSTEM 2.0", "=" * 10)
        print("-1. MODULO DE FACTURACION (Ventas y Clientes)")
        print("-2. MODULO DE INVENTARIO (Productos)")
        print("-3. SALIR")
        print("=" * 43)

    def _limpiar_pantalla_externa(self):
        limpiar_terminal()


class SeleccionarMenuPrincipal:

    def __init__(self, menu_inventario, menu_facturacion):  
        self.menu_inv = menu_inventario
        self.menu_fact = menu_facturacion
    
    def gestionar_entrada_usuario(self):
        try:
            opcion = int(input("\nSeleccione un modulo (1/2/3): "))
        except ValueError:
            print("Error: Ingrese un valor numerico válido.")
            input("Presione Enter para continuar...")
            return "volver_anterior"

        return self._redireccionar(opcion)

    def _redireccionar(self, opcion):
        
        opciones = {  
            1: self.menu_fact.mostrar_interfaz_facturacion, 
            2: self.menu_inv.mostrar_interfaz_inventario,   
            3: self._ejecutar_salida_externa,       
        }

        if opcion in opciones:
          
            return opciones[opcion]()  
        else:
            print("Opción no válida.")
            input("Presione Enter para continuar...")
            return "volver_anterior"

    def _ejecutar_salida_externa(self):
        return saliendo_del_programa()