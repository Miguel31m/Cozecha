

import os
import sys 

def _configurar_entorno_de_rutas_del_sistema_externo():
    ruta_raiz = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    if ruta_raiz not in sys.path:
        sys.path.append(ruta_raiz)

_configurar_entorno_de_rutas_del_sistema_externo()

from crud.crud_cliente.data_cliente import dato_cliente
from models.pedido import Pedido
from models.cliente import Cliente 

class FuncionPedido:

    def __init__(self, funciones_inventario_externo):
        self.funciones_inventario = funciones_inventario_externo

    def crear_pedido_para_cliente(self): 
    
        print("\n" + "-"*20 + " REGISTRO DE VENTA " + "-"*20)
     
        nombre_cliente_capturado = input("Ingrese nombre del cliente: ").strip()
        identificacion_cliente_capturada = input("Ingrese identificacion del cliente: ").strip()
        
        if not nombre_cliente_capturado or not identificacion_cliente_capturada:
            print("Error: Nombre e Identificacion son obligatorios para facturar.")
            return

        cliente_instancia_actual = Cliente(nombre_cliente=nombre_cliente_capturado, id_cliente=identificacion_cliente_capturada)
        pedido_instancia_nuevo = Pedido()
        
        while True:
            nombre_producto_solicitado = input("\nProducto a pedir (o fin para terminar): ").strip()
            if nombre_producto_solicitado.lower() == "fin": 
                break
            
            if nombre_producto_solicitado not in self.funciones_inventario.inventario.dato_inventario:
                print(f"Error: {nombre_producto_solicitado} no existe en inventario.")
                continue
                
            cantidad_stock_disponible = self.funciones_inventario.inventario.dato_inventario[nombre_producto_solicitado]["cantidad"]
            
            try:
                cantidad_producto_pedida = int(input(f"Cantidad (Disponible: {cantidad_stock_disponible}): "))
                
                if cantidad_producto_pedida <= 0:
                    print("La cantidad debe ser mayor a 0.")
                    continue
                if cantidad_producto_pedida > cantidad_stock_disponible:
                    print(f"Stock insuficiente. Solo hay {cantidad_stock_disponible}.")
                    continue
                
                self.funciones_inventario.inventario.dato_inventario[nombre_producto_solicitado]["cantidad"] -= cantidad_producto_pedida
                precio_unitario_producto = self.funciones_inventario.inventario.dato_inventario[nombre_producto_solicitado]["detalles"]["precio"]
                
                pedido_instancia_nuevo.agregar_item_al_pedido(nombre_producto_solicitado, cantidad_producto_pedida, precio_unitario_producto)
                print(f"Registrado: {nombre_producto_solicitado} x{cantidad_producto_pedida}")

            except ValueError:
                print("Error: Ingrese un valor numerico entero.")

        self._guardar_en_base_de_datos_cliente(cliente_instancia_actual, pedido_instancia_nuevo)

    def _guardar_en_base_de_datos_cliente(self, objeto_cliente, objeto_pedido):
        if objeto_pedido.total_pago == 0:
            print("\nVenta cancelada: No se agregaron productos al pedido.")
            return

        identificador_unico_cliente = objeto_cliente.id  
        nombre_completo_cliente = objeto_cliente.nombre_cliente

        if identificador_unico_cliente not in dato_cliente:
            dato_cliente[identificador_unico_cliente] = {
                "nombre": nombre_completo_cliente,
                "pedidos": []
            }
        
        dato_cliente[identificador_unico_cliente]["pedidos"].append({
            "fecha": objeto_pedido.fecha,
            "items": objeto_pedido.productos_solicitados,
            "total": objeto_pedido.total_pago
        })
        
        print("\n" + "="*50)
        print("VENTA EXITOSA")
        print(f"CLIENTE: {nombre_completo_cliente} (ID: {identificador_unico_cliente})")
        print(f"TOTAL A COBRAR: ${objeto_pedido.total_pago}")
        print("="*50)