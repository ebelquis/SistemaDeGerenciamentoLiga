# main.py
from controladores.controlador_sistema import ControladorSistema

if __name__ == "__main__":
    sistema = ControladorSistema()
    sistema.iniciar()