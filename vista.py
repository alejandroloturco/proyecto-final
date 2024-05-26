import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QStackedWidget, QLineEdit, QFormLayout, QComboBox
from PyQt5.QtCore import QTimer, Qt

class Advertencia(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Aviso de Seguridad')
        self.setGeometry(100, 100, 640, 480)
        self.setStyleSheet("background-color: green;")
        
        setup = QVBoxLayout()
        texto_1 = QLineEdit('!ADIVOS DE SALUD Y SEGURIDAD¡')
        texto_1.setStyleSheet("color: white; font-size: 35px;")
        texto_1.setReadOnly(True)
        texto_1.setAlignment(Qt.AlignCenter)
        setup.addWidget(texto_1)
        texto_2 = QLabel('Para el ingreso de info se debe de tener al cuidador en la sala')
        texto_2.setStyleSheet("color: white; font-size: 30px;")
        texto_2.setAlignment(Qt.AlignCenter)
        setup.addWidget(texto_2)
        self.setLayout(setup)

class Menu_inicial(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ventana de Inicio')
        self.setGeometry(100, 100, 640, 480)

        setup = QVBoxLayout()
        organizador = QFormLayout()

        titulo = QLineEdit('Bienvenido a AlzCare')
        titulo.setStyleSheet("font-size: 30px; border: 1px solid black;")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.adjustSize()
        titulo.setReadOnly(True)
        
        self.boton_login = QPushButton('Login')
        self.boton_login.setFixedSize(200, 50)
        self.boton_pre_registro = QPushButton('Registro')
        self.boton_pre_registro.setFixedSize(200, 50)
        self.boton_moca = QPushButton('MOCA')
        self.boton_moca.setFixedSize(200, 50)
        self.boton_salida = QPushButton('Salir')
        self.boton_salida.setFixedSize(200, 50)

        organizador.addRow(self.boton_login)
        organizador.addRow(self.boton_pre_registro)
        organizador.addRow(self.boton_moca)
        organizador.addRow(self.boton_salida)
        organizador.setFormAlignment(Qt.AlignCenter)
        organizador.setLabelAlignment(Qt.AlignCenter)
        organizador.setSpacing(15)
        organizador.setContentsMargins(50, 50, 50, 50)

        setup.addWidget(titulo)
        setup.addLayout(organizador)
        
        self.setLayout(setup)

class Menu_Login(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')
        self.setGeometry(100, 100, 320, 240)
        
        setup = QVBoxLayout()
        organizador = QFormLayout()
        
        self.usuario_respuesta = QLineEdit()
        self.contraseña_respuesta = QLineEdit()
        self.contraseña_respuesta.setEchoMode(QLineEdit.Password)
        
        organizador.addRow('Usuario:', self.usuario_respuesta)
        organizador.addRow('Contraseña:', self.contraseña_respuesta)
        organizador.setFormAlignment(Qt.AlignCenter)
        organizador.setLabelAlignment(Qt.AlignCenter)
        organizador.setSpacing(15)
        organizador.setContentsMargins(50, 50, 50, 50)

        self.boton_login = QPushButton('Entrar')
        self.boton_salida = QPushButton('Salir')
        
        setup.addLayout(organizador)
        setup.addWidget(self.boton_login)
        setup.addWidget(self.boton_salida)
        
        self.setLayout(setup)

class Menu__pre_registro(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Pre-Registro')
        self.setGeometry(100, 100, 640, 480)

        setup = QVBoxLayout()
        organizador = QFormLayout()

        self.boton_registro = QPushButton('Registrar')
        self.boton_registro.setFixedSize(200, 50)
        self.boton_importar = QPushButton('Importar')
        self.boton_importar.setFixedSize(200, 50)
        self.boton_salida = QPushButton('Salir')
        self.boton_salida.setFixedSize(200, 50)

        organizador.addRow(self.boton_registro)
        organizador.addRow(self.boton_importar)
        organizador.addRow(self.boton_salida)
        organizador.setFormAlignment(Qt.AlignCenter)
        organizador.setLabelAlignment(Qt.AlignCenter)
        organizador.setSpacing(15)
        organizador.setContentsMargins(50, 50, 50, 50)

        setup.addLayout(organizador)

        self.setLayout(setup)
class Menu_registro(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Registro')
        self.setGeometry(100, 100, 640, 480)
        
        setup = QVBoxLayout()
        organizador = QFormLayout()
        
        self.usuario_respuesta = QLineEdit()
        self.contraseña_respuesta = QLineEdit()
        self.contraseña_respuesta.setEchoMode(QLineEdit.Password)
        self.nombre_cuidador = QLineEdit()
        self.cedula_cuidador = QLineEdit()
        self.cecular_cuidador = QLineEdit()
        
        self.opciones = QComboBox()
        self.opciones.addItem("Opción 1")
        self.opciones.addItem("Opción 2")
        self.opciones.addItem("Opción 3")

        organizador.addRow('Usuario:', self.usuario_respuesta)
        organizador.addRow('Contraseña:', self.contraseña_respuesta)
        organizador.addRow('Nombre:', self.nombre_cuidador)
        organizador.addRow('CC:', self.cedula_cuidador)
        organizador.addRow('Teléfono:', self.cecular_cuidador)
        organizador.addRow('Formación:', self.opciones)
        organizador.setFormAlignment(Qt.AlignCenter)
        organizador.setLabelAlignment(Qt.AlignCenter)
        organizador.setSpacing(15)
        organizador.setContentsMargins(50, 50, 50, 50)
        
        self.boton_registro = QPushButton('Registrar')
        
        setup.addLayout(organizador)
        setup.addWidget(self.boton_registro)
        
        self.setLayout(setup)

class Menu_moca(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('MOcA')
        self.setGeometry(100, 100, 640, 480)
        
        setup = QVBoxLayout()
        self.texto = QLabel('Opcional: NO SE GUARDA')
        self.texto.setStyleSheet("color: white; font-size: 18px;")
        setup.addWidget(self.texto)
        self.setLayout(setup)

class MainApp(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('AlzCare')
        self.setGeometry(100, 100, 640, 480)
        
        self.advertencia = Advertencia()
        self.menu_inicial = Menu_inicial()
        self.menu_login = Menu_Login()
        self.menu_registro = Menu_registro()
        self.menu_moca = Menu_moca()
        
        self.addWidget(self.advertencia)
        self.addWidget(self.menu_inicial)
        self.addWidget(self.menu_login)
        self.addWidget(self.menu_registro)
        self.addWidget(self.menu_moca)
        
        QTimer.singleShot(5000, self.show_main_window)
        
        self.menu_inicial.boton_login.clicked.connect(self.show_login_window)
        self.menu_inicial.boton_pre_registro.clicked.connect(self.show_registro_window)
        self.menu_inicial.boton_moca.clicked.connect(self.show_moca_window)
        self.menu_inicial.boton_salida.clicked.connect(self.close)
        
        self.menu_login.boton_login.clicked.connect(self.show_main_window)
        self.menu_login.boton_salida.clicked.connect(self.close)
        
    def show_main_window(self):
        self.setCurrentWidget(self.menu_inicial)
        
    def show_login_window(self):
        self.setCurrentWidget(self.menu_login)
        
    def show_registro_window(self):
        self.setCurrentWidget(self.menu_registro)
        
    def show_moca_window(self):
        self.setCurrentWidget(self.menu_moca)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())