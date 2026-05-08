import os
import sys

def _configurar_entorno_de_rutas_del_sistema_externo():
    ruta_raiz = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    if ruta_raiz not in sys.path:
        sys.path.append(ruta_raiz)

_configurar_entorno_de_rutas_del_sistema_externo()


from crud.crud_pedido.funcion_pedido import FuncionPedido
from crud.crud_factorizacion.factorizacion import Facturacion

class SeleccionarOpcionFacturacion:
    def __init__(self, funciones_inventario):
        self.funcion_pedido = FuncionPedido(funciones_inventario)
        self.funcion_factura = Facturacion()

    def ejecutar_accion(self, opcion):
        if opcion == 1:
            self._flujo_nueva_venta()
        elif opcion == 2:
            self._flujo_consulta_cliente()
        else:
            print("Opción no valida.")
            input("Presione Enter para continuar...")

    def _flujo_nueva_venta(self):
    
        try:
    
            self.funcion_pedido.crear_pedido_para_cliente()
            
            input("\nPresione Enter para volver al menu de facturación...")
        except Exception as error:
            print(f"Error crítico en el proceso de venta: {error}")
            input("Presione Enter para continuar...")

    def _flujo_consulta_cliente(self):
        print("\n" + "─" * 20 + " CONSULTA DE CLIENTE " + "─" * 20)
        cedula = input("Ingrese la Cédula o ID a consultar: ").strip()
        
        if not cedula:
            print("Error: Debe ingresar una identificación válida.")
        else:
            
            self.funcion_factura.buscar_cliente_e_imprimir_pedidos(cedula)
            
        input("Presione Enter para continuar...")