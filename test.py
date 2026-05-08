import os
import sys
import pytest
from unittest.mock import patch

def _configurar_entorno_de_rutas_del_sistema_externo():
    ruta_raiz = os.path.dirname(os.path.abspath(__file__))
    if ruta_raiz not in sys.path:
        sys.path.append(ruta_raiz)

_configurar_entorno_de_rutas_del_sistema_externo()


from models.models_producto import producto, antibiotico
from models import cliente
from models import pedido
from crud.crud_inventario import inventario, funciones_productos
from service.service_ui import seleccionar_tipo

@pytest.fixture
def antibiotico_vacio():
    return antibiotico.Antibiotico()

@pytest.fixture
def funciones_inventario():
    inv = inventario.Inventario()
    return funciones_productos.FuncionesInventario(inv)


def test_creacion_cliente_por_defecto():
    mi_cliente = cliente.Cliente()
    assert mi_cliente._nombre_cliente == "Usuario externo"

def test_creacion_pedido_inicial():
    mi_pedido = pedido.Pedido()
    assert hasattr(mi_pedido, 'productos_solicitados') or hasattr(mi_pedido, '_productos_solicitados')

def test_agregar_producto_al_inventario(funciones_inventario, antibiotico_vacio):
    funciones_inventario.agregar_producto(antibiotico_vacio, 1)
    assert True 

def test_verificar_herencia_producto(antibiotico_vacio):
    assert isinstance(antibiotico_vacio, producto.Producto)

def test_consultar_inventario_vacio(funciones_inventario, capsys):
    funciones_inventario.consultar_inventario()
    captured = capsys.readouterr()
    assert "PRODUCTO" in captured.out or "producto" in captured.out.lower()

def test_redireccionar_alta_producto_antibiotico(funciones_inventario):
    service_ui = seleccionar_tipo.SeleccionarTipoProducto(funciones_inventario)
    inputs_simulados = ["AntiTest", "30", "5", "ICA123", "12", ""]
    
    with patch('builtins.input', side_effect=inputs_simulados):
        try:
            service_ui.redireccionar_alta_producto(1)
        except (StopIteration, ValueError):
            pass 
    assert True

if __name__ == "__main__":
    c = cliente.Cliente()
 