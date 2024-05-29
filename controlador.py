from modelo import *
from vista import *
class Controlador():
    def __init__(self, usuario, contrasena, nombre_cuidador, cedula_cuidador, numero_cuidador, email_cuidador, ocupacion_cuidador, nombre_paciente, cedula_paciente, edad_paciente, numero_paciente, residencia_paciente, nacimiento_paciente, fase_paciente, estudio_paciente, dominancia_paciente, tiempo_alz_paciente):
        self.aplicacion = QApplication(sys.argv)
        self.cuidador = Cuidador(usuario, contrasena, nombre_cuidador, cedula_cuidador, numero_cuidador, email_cuidador, ocupacion_cuidador)
        self.paciente = Paciente(nombre_paciente, cedula_paciente, edad_paciente, numero_paciente, residencia_paciente, nacimiento_paciente, fase_paciente, estudio_paciente, dominancia_paciente, tiempo_alz_paciente)
        self.seguimiento = Seguimiento()

    def inicio(self):
        self.menu = Menu_Principal()
        self.menu.show()
        sys.exit(self.aplicacion.exec_())  


if __name__ == '__main__':
    crear_BDSQL()
    crear_tablasSQL()
    listcui, listpac, listreg = obtener_dataSQL()
    
    controlador = Controlador("usuario", "contrasena", "nombre_cuidador", "cedula_cuidador", "numero_cuidador", "email_cuidador", "ocupacion_cuidador", "nombre_paciente", "cedula_paciente", "edad_paciente", "numero_paciente", "residencia_paciente", "nacimiento_paciente", "fase_paciente", "estudio_paciente", "dominancia_paciente", "tiempo_alz_paciente")
    controlador.inicio()