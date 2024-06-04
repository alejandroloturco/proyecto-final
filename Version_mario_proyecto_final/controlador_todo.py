from modelo_todo import *
from vista_todo import *
class Controlador():
    def __init__(self,listcui, listpac, listreg):
        self.aplicacion = QApplication(sys.argv)
        self.cuidador = Cuidador(listcui)
        self.paciente = Paciente(listpac)
        self.seguimiento = Seguimiento(listreg)

    def inicio(self):
        self.menu = Botonera(controlador) 
        self.menu.show()
        sys.exit(self.aplicacion.exec_())

    def validar_usuario(self, usuario, contrasena):
        return self.cuidador.validar_usuario(usuario, contrasena)
    
    def registro_cuidador(self, nombre, apellido, telefono, cedula, formacion, usuario, contraseña):
        return self.cuidador.registro_cuidador(nombre, apellido, telefono, cedula, formacion, usuario, contraseña)
    
    def registro_paciente(self, nombre, apellido, telefono, cedula, residencia, nacimiento, fase, estudio, dominancia, tiempoalz):
        return self.paciente.registro_paciente(nombre, apellido,telefono, cedula, residencia, nacimiento, fase, estudio, dominancia, tiempoalz, self.cuidador.get_listcui())

if __name__ == '__main__':
    crear_BDSQL()
    crear_tablasSQL()
    listcui, listpac, listreg = obtener_dataSQL()
    app = QApplication(sys.argv)
    controlador = Controlador(listcui, listpac, listreg)
    controlador.inicio()