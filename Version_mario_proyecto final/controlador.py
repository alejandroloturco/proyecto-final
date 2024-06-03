from modelo import *
from vista import *
class Controlador():
    def __init__(self,listcui, listpac, listreg):
        self.aplicacion = QApplication(sys.argv)
        self.cuidador = Cuidador(listcui)
        self.paciente = Paciente(listpac)
        self.seguimiento = Seguimiento(listreg)
        self.puntos_moca = 0

    def inicio(self):
        self.menu = Botonera(controlador)
        self.menu.show()
        sys.exit(self.aplicacion.exec_())  

    def conteo_puntos(self):
        self.puntos_moca += 1
        print(self.puntos_moca)

    def validar_usuario(self, usuario, contrasena):
        return self.cuidador.validar_usuario(usuario, contrasena)

if __name__ == '__main__':
    crear_BDSQL()
    crear_tablasSQL()
    listcui, listpac, listreg = obtener_dataSQL()
    app = QApplication(sys.argv)
    controlador = Controlador(listcui, listpac, listreg)
    controlador.inicio()