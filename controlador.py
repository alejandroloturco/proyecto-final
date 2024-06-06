from modelo import *
from vista import *
class Controlador():
    def __init__(self,listcui, listpac, listreg):
        self.aplicacion = QApplication(sys.argv)
        self.cuidador = Cuidador(listcui)
        self.paciente = Paciente(listpac)
        self.seguimiento = Seguimiento(listreg)
        self.puntaje = 0

    def inicio(self):
        self.menu = Botonera(controlador)
        self.menu.setWindowIcon(QIcon(r'Recursos_Interfaz\Alzcare.png'))
        self.menu.show()
        sys.exit(self.aplicacion.exec_())

    def validar_usuario(self, usuario: str, contrasena: str) -> bool:
        return self.cuidador.validar_usuario(usuario, contrasena)
    
    def registro_cuidador(self, nombre: str, apellido: str, telefono: int, cedula: int, formacion: str, usuario: str, contraseña: str) -> bool:
        return self.cuidador.registro_cuidador(nombre, apellido, telefono, cedula, formacion, usuario, contraseña)
    
    def registro_paciente(self, nombre: str, apellido: str, edad: int, telefono: int, cedula: int, residencia: str, nacimiento: str, fase: str, estudio: str, dominancia: str, tiempoalz: str) -> bool:
        return self.paciente.registro_paciente(nombre, apellido, edad, telefono, cedula, residencia, nacimiento, fase, estudio, dominancia, tiempoalz, self.cuidador.get_listcui())
    
    def registro_seguimiento(self, usuario, listaresp: list) -> bool:
        id = id_paciente(usuario)
        fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        bool = self.seguimiento.registro_seguimiento(id, fecha, listaresp, self.puntaje)
        self.puntaje = 0
        return bool
    
    def grafico(self, usuario: str):
        id = id_paciente(usuario)
        datos = self.seguimiento.datos_histograma(id)
        fechas = datos["fechas"]
        puntajes = datos["puntajes"]
        plt.bar(fechas, puntajes, color = 'blue')
        plt.xlabel('Fechas')
        plt.ylabel('Puntajes')
        plt.title('Puntajes de seguimiento')
        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        pixmap = QPixmap()
        pixmap.loadFromData(buf.getvalue(), 'PNG')
        return pixmap, puntajes[-1]
    
    def exportar_perfil(self, usuario: str) -> bool:
        return exportar_perfil(usuario)
    
    def importar_perfil(self, direccion: str) -> bool:
        return importar_perfil(direccion)
    
    def puntos(self, respuesta: str):
        self.puntaje += obtener_puntos(respuesta)

if __name__ == '__main__':
    crear_BDSQL()
    crear_tablasSQL()
    listcui, listpac, listreg = obtener_dataSQL()
    app = QApplication(sys.argv)
    controlador = Controlador(listcui, listpac, listreg)
    controlador.inicio()