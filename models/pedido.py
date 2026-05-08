
class Pedido:
    def __init__(self, fecha="07/05/2026"):
        self.fecha = fecha
        self.productos_solicitados = []
        self.total_pago = 0.0

    def agregar_item_al_pedido(self, nombre, cantidad, precio_unitario):
        subtotal = cantidad * precio_unitario
        self.productos_solicitados.append({
            "producto": nombre,
            "cantidad": cantidad,
            "subtotal": subtotal
        })
        self.total_pago += subtotal