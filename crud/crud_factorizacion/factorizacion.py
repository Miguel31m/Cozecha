import os
import sys 

def _configurar_entorno_de_rutas_del_sistema_externo():
    ruta_raiz = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    if ruta_raiz not in sys.path:
        sys.path.append(ruta_raiz)

_configurar_entorno_de_rutas_del_sistema_externo()

from crud.crud_cliente.data_cliente import dato_cliente

class Facturacion:

    def buscar_cliente_e_imprimir_pedidos(self, identificacion_cliente_a_buscar):
        
        if identificacion_cliente_a_buscar not in dato_cliente:
            print(f"Error: El cliente con identificacion {identificacion_cliente_a_buscar} no tiene historial de pedidos.")
            return

        informacion_completa_cliente = dato_cliente[identificacion_cliente_a_buscar]
        
        print("\n" + "=" * 60)
        print(f"HISTORIAL DE FACTURACION: {informacion_completa_cliente['nombre'].upper()}")
        print(f"ID CLIENTE: {identificacion_cliente_a_buscar}")
        print("=" * 60)

        if not informacion_completa_cliente["pedidos"]:
            print("El cliente existe pero no ha registrado compras en el sistema.")
            return

        for indice_pedido, diccionario_pedido in enumerate(informacion_completa_cliente["pedidos"], 1):
            print(f"\nPEDIDO NUMERO {indice_pedido} - Fecha: {diccionario_pedido['fecha']}")
            print(f"{'PRODUCTO':<25} | {'CANTIDAD':<10} | {'SUBTOTAL'}")
            print("-" * 60)
            
            for diccionario_item in diccionario_pedido["items"]:
                nombre_producto_item = diccionario_item['producto']
                cantidad_producto_item = diccionario_item['cantidad']
                subtotal_producto_item = diccionario_item['subtotal']
                print(f"{nombre_producto_item:<25} | {cantidad_producto_item:<10} | ${subtotal_producto_item:,.2f}")
            
            print("-" * 60)
            print(f"{'TOTAL DE ESTE PEDIDO:':>45} ${diccionario_pedido['total']:,.2f}")
        
        valor_total_historico_acumulado = sum(pedido_individual['total'] for pedido_individual in informacion_completa_cliente['pedidos'])
        
        print("\n" + "=" * 60)
        print(f"{'TOTAL ACUMULADO DEL CLIENTE:':>45} ${valor_total_historico_acumulado:,.2f}")
        print("=" * 60 + "\n")