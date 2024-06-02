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
        self.menu = Menu_Principal(self)
        self.menu.setup()
        self.menu.show()
        sys.exit(self.aplicacion.exec_())  

    def conteo_puntos(self):
        self.puntos_moca += 1
        print(self.puntos_moca)

if __name__ == '__main__':
    crear_BDSQL()
    crear_tablasSQL()
    listcui, listpac, listreg = obtener_dataSQL()

    controlador = Controlador(listcui, listpac, listreg)
    controlador.inicio()