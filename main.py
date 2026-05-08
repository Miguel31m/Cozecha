import sys
import os

def _configurar_entorno_de_rutas_del_sistema_externo():

    ruta_raiz = os.path.dirname(os.path.abspath(__file__))
    if ruta_raiz not in sys.path:
        sys.path.append(ruta_raiz)
_configurar_entorno_de_rutas_del_sistema_externo()

from ui.menu_principal import MostrarMenuPrincipal

def main():
    
        inicio = MostrarMenuPrincipal()
        
      
        inicio.ejecutar_interfaz_menu_principal()
        

if __name__ == "__main__":
    main()