from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout ,QPushButton, QLabel, QStackedWidget, QLineEdit, QFormLayout, QComboBox, QStackedLayout, QMessageBox, QGraphicsView, QGraphicsScene, QGraphicsProxyWidget, QLabel
from PyQt5.QtCore import QTimer, Qt, QTimer
from PyQt5.QtGui import QPixmap, QFont

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

        titulo = QLabel('Bienvenido a AlzCare')
        titulo.setStyleSheet("font-size: 30px; border: 1px solid black;")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.adjustSize()
        
        self.boton_login = QPushButton('Login')
        self.boton_login.setFixedSize(200, 50)
        self.boton_pre_registro = QPushButton('Registro')
        self.boton_pre_registro.setFixedSize(200, 50)
        self.boton_moca = QPushButton('MOCA')
        self.boton_moca.setFixedSize(200, 50)
        self.boton_salida = QPushButton('Salir.')
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
        self.boton_volver = QPushButton('Volver')
        
        setup.addLayout(organizador)
        setup.addWidget(self.boton_login)
        setup.addWidget(self.boton_volver)
        
        self.setLayout(setup)

class Menu_pre_registro(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Pre-Registro')
        self.setGeometry(100, 100, 640, 480)

        setup = QVBoxLayout()
        organizador = QFormLayout()

        self.boton_registro = QPushButton('Registrar')
        self.boton_registro.setFixedSize(200, 50)
        self.boton_importar = QPushButton('Importar perfil')
        self.boton_importar.setFixedSize(200, 50)
        self.boton_volver = QPushButton('Volver')
        self.boton_volver.setFixedSize(200, 50)

        organizador.addRow(self.boton_registro)
        organizador.addRow(self.boton_importar)
        organizador.addRow(self.boton_volver)
        organizador.setFormAlignment(Qt.AlignCenter)
        organizador.setLabelAlignment(Qt.AlignCenter)
        organizador.setSpacing(15)
        organizador.setContentsMargins(50, 50, 50, 50)

        setup.addLayout(organizador)

        self.setLayout(setup)
class Menu_registro_cuidador(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Registro')
        self.setGeometry(100, 100, 640, 480)

        titulo = QLabel('Registro del Cuidador')
        titulo.setStyleSheet("font-size: 30px; border: 1px solid black;")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.adjustSize()
        
        setup = QVBoxLayout()
        organizador = QFormLayout()
        self.opciones = QComboBox()
        self.setup_stakeado = QStackedLayout()
        self.salud_widget = QWidget()
        self.familiar_widget = QWidget()
        self.nada_widget = QWidget()
        widgets_stakeados = QWidget()
        
        self.usuario_respuesta = QLineEdit()
        self.usuario_respuesta.setPlaceholderText('Nombre de usuario')
        self.contraseña_respuesta = QLineEdit()
        self.contraseña_respuesta.setEchoMode(QLineEdit.Password)
        self.contraseña_respuesta.setPlaceholderText('Contraseña123')
        self.nombre_cuidador = QLineEdit()
        self.nombre_cuidador.setPlaceholderText('Pedro, Juan, Maria...')
        self.apellido_cuidador = QLineEdit()
        self.apellido_cuidador.setPlaceholderText('Perez, Rodriguez, Gomez...')
        self.cedula_cuidador = QLineEdit()
        self.cedula_cuidador.setPlaceholderText('1234567890')
        self.telefono_cuidador = QLineEdit()
        self.telefono_cuidador.setPlaceholderText('+57 1234567890')
        self.formacion_salud = QLineEdit()
        self.formacion_salud.setPlaceholderText('Enfermeria, Medicina, Psicologia...')
        self.tiempo_cuidado_salud = QLineEdit()
        self.tiempo_cuidado_salud.setPlaceholderText('1 año, 2 meses, 3 semanas...')
        self.relacion_familiar = QLineEdit()
        self.relacion_familiar.setPlaceholderText('Hijo, Hermano, Sobrino...')
        self.parentesco_familiar = QLineEdit()
        self.parentesco_familiar.setPlaceholderText('Padre, Madre, Abuelo...')
        self.opciones.currentIndexChanged.connect(self.limpiar_line_edits)
        self.opciones.addItem("...")
        self.opciones.addItem("Salud")
        self.opciones.addItem("Familiar")
        
        formato_1 = QVBoxLayout(self.salud_widget)
        formato_2 = QVBoxLayout(self.familiar_widget)

        formato_1.addWidget(QLabel('Formación:'))
        formato_1.addWidget(self.formacion_salud)
        formato_1.addWidget(QLabel('Tiempo de cuidado:'))
        formato_1.addWidget(self.tiempo_cuidado_salud)
        formato_2.addWidget(QLabel('Relación:'))
        formato_2.addWidget(self.relacion_familiar)
        formato_2.addWidget(QLabel('Parentesco:'))
        formato_2.addWidget(self.parentesco_familiar)

        self.setup_stakeado.addWidget(self.nada_widget)
        self.setup_stakeado.addWidget(self.salud_widget)
        self.setup_stakeado.addWidget(self.familiar_widget)
        self.opciones.currentIndexChanged.connect(self.setup_stakeado.setCurrentIndex)
        widgets_stakeados.setLayout(self.setup_stakeado)

        organizador.addRow('Usuario:', self.usuario_respuesta)
        organizador.addRow('Contraseña:', self.contraseña_respuesta)
        organizador.addRow('Nombre:', self.nombre_cuidador)
        organizador.addRow('Apellido:', self.apellido_cuidador)
        organizador.addRow('CC:', self.cedula_cuidador)
        organizador.addRow('Teléfono:', self.telefono_cuidador)
        organizador.addRow('Relacion:', self.opciones)
        organizador.addWidget(widgets_stakeados)
        organizador.setFormAlignment(Qt.AlignCenter)
        organizador.setLabelAlignment(Qt.AlignCenter)
        organizador.setSpacing(15)
        organizador.setContentsMargins(50, 50, 50, 50)

        self.boton_siguiente = QPushButton('Siguiente')
        self.boton_volver = QPushButton('Volver')
        
        setup.addWidget(titulo)
        setup.addLayout(organizador)
        setup.addWidget(self.boton_siguiente)
        setup.addWidget(self.boton_volver)
        
        self.setLayout(setup)

    def limpiar_line_edits(self):
        self.formacion_salud.clear()
        self.tiempo_cuidado_salud.clear()
        self.relacion_familiar.clear()
        self.parentesco_familiar.clear()
class Menu_registro_paciente(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Registro')
        self.setGeometry(100, 100, 640, 480)

class Advertencia_Moca(QWidget):
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

class Menu_moca_1(QWidget):
    def __init__(self, controlador):
        super().__init__()   
        self.controlador = controlador
        self.setWindowTitle('MOCA')

        color_normal = "rgb(144, 224, 239)"
        color_hover = "rgb(0, 119, 182)"
        color_pressed = "rgb(144, 224, 239)"
        color_fondo = "rgb(202, 240, 248)"
        
        self.setStyleSheet(f"background-color: {color_fondo};")

        setup = QVBoxLayout()
        self.view = QGraphicsView()
        self.scene = QGraphicsScene(self)
        self.view.setScene(self.scene)

        self.secuencia_molde = ['1', 'A', '2', 'B', '3', 'C', '4', 'D', '5', 'E']
        self.posicion = 0 
        self.primer_intento = True

        titulo = QLabel('1) Selecciona en el orden correcto la siguiente secuencia de botones')
        titulo.setStyleSheet(f"font-size: 20px; border: 1px solid black; background-color: {color_fondo};")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setFont(QFont("Arial", 14, QFont.Bold))
        titulo.adjustSize()

        self.siguiente = QPushButton('Siguiente')
        self.siguiente.setFixedSize(100, 50)
        self.siguiente.hide()
        self.siguiente.Aligned = Qt.AlignCenter
        self.siguiente.setStyleSheet(f"""
            QPushButton {{
                background-color: {color_normal};
                color: white;
                border: 2px solid {color_hover};
                border-radius: 25px;
                padding: 10px;
            }}
            QPushButton:hover {{
                background-color: {color_hover};
            }}
            QPushButton:pressed {{
                background-color: {color_pressed};
            }}
        """)

        self.botones_orden = {
            '1': QPushButton('1'),
            '2': QPushButton('2'),
            '3': QPushButton('3'),
            '4': QPushButton('4'),
            '5': QPushButton('5'),
            'A': QPushButton('A'),
            'B': QPushButton('B'),
            'C': QPushButton('C'),
            'D': QPushButton('D'),
            'E': QPushButton('E'),
        }

        self.posiciones = {
            '1': (210, 190),
            '2': (480, 130),
            '3': (480, 300),
            '4': (310, 270),
            '5': (80, 130),
            'A': (380, 60),
            'B': (340, 140),
            'C': (210, 330),
            'D': (100, 270),
            'E': (210, 70),
        }

        for boton in self.botones_orden.values():
            boton.setFixedSize(50, 50)
            boton.setStyleSheet(f"""
                QPushButton {{
                    background-color: {color_normal};
                    color: white;
                    border: 2px solid {color_hover};
                    border-radius: 25px;
                    padding: 10px;
                }}
                QPushButton:hover {{
                    background-color: {color_hover};
                }}
                QPushButton:pressed {{
                    background-color: {color_pressed};
                }}
            """)

        for boton, posicion in self.posiciones.items():
            configuracion = QGraphicsProxyWidget()
            configuracion.setWidget(self.botones_orden[boton])
            self.scene.addItem(configuracion)
            configuracion.setPos(*posicion)

        for x in self.botones_orden:
            self.botones_orden[x].clicked.connect(self.boton_secuenciado)

        setup.addWidget(titulo)
        setup.addWidget(self.view)
        setup.addWidget(self.siguiente)
        self.setLayout(setup)

    def boton_secuenciado(self):
        secuencia = self.sender().text()
        if secuencia == self.secuencia_molde[self.posicion]:
            self.posicion += 1
            if self.posicion == len(self.secuencia_molde):
                QMessageBox.information(self, 'Correcto', '¡Felicitaciones, la secuencia es correcta!')
                self.posicion = 0
                self.siguiente.show()
                if self.primer_intento:
                    self.controlador.conteo_puntos()
                    self.primer_intento = False
        else:
            QMessageBox.warning(self, 'Error', 'Secuencia incorrecta, intente de nuevo.')
            self.posicion = 0
            self.primer_intento = False


class Menu_moca_2(QWidget):
    def __init__(self, controlador):
        super().__init__()   
        self.controlador = controlador
        self.setWindowTitle('MOCA')
        setup = QVBoxLayout()
        self.stacked_widget = QStackedWidget()
        self.primer_intento = True
        titulo = QLabel('2) Seleccione la imagen que coincida con la que acaba de ver.')
        titulo.setStyleSheet("font-size: 20px; border: 1px solid black;")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.adjustSize()
        self.siguiente = QPushButton('Siguiente') 
        self.siguiente.hide()
        
        self.imagen = QLabel(self)
        pixmap = QPixmap('MoCA/CUBO/1.jpg')
        self.imagen.setPixmap(pixmap)
        self.imagen.setAlignment(Qt.AlignCenter)
        self.stacked_widget.addWidget(self.imagen)

        self.opciones_widget = QWidget()
        opciones_layout = QHBoxLayout()
        self.opciones_widget.setLayout(opciones_layout)
        self.opciones = []
        for i in range(1, 5):
            opcion_layout = QVBoxLayout()
            opcion_imagen = QLabel(self)
            pixmap = QPixmap(f'MoCA/CUBO/{i}.jpg')
            pixmap = pixmap.scaled(250, 250, Qt.KeepAspectRatio)
            opcion_imagen.setPixmap(pixmap)
            opcion_imagen.setAlignment(Qt.AlignCenter)
            boton = QPushButton(f'Opción {i}', self.opciones_widget)
            boton.clicked.connect(lambda checked, i=i: self.boton_precionado(i))
            self.opciones.append(boton)
            opcion_layout.addWidget(opcion_imagen)
            opcion_layout.addWidget(boton)
            opciones_layout.addLayout(opcion_layout)
        self.stacked_widget.addWidget(self.opciones_widget)

        setup.addWidget(titulo)
        setup.addWidget(self.stacked_widget)
        setup.addWidget(self.siguiente)
        self.setLayout(setup)
    
    def showEvent(self, event):
        super().showEvent(event)
        QTimer.singleShot(5000, self.mostrar_opciones)

    def mostrar_opciones(self):
        self.stacked_widget.setCurrentWidget(self.opciones_widget)

    def boton_precionado(self, opcion):
        if opcion == 1:
            QMessageBox.information(self, 'Correcto', 'Felicitaciones, la imagen es correcta!')
            self.siguiente.show()
            if self.primer_intento:
                self.controlador.conteo_puntos()
                self.primer_intento = False
                self.siguiente.show()
        else:
            QMessageBox.warning(self, 'Error', 'Imagen incorrecta, intente de nuevo.')
            self.primer_intento = False

class Menu_moca_3(QWidget):
    def __init__(self,controlador):
        super().__init__()
        self.controlador = controlador
        self.setWindowTitle('MOCA')
        setup = QVBoxLayout()
        self.stacked_widget = QStackedWidget()
        self.primer_intento = True
        titulo = QLabel('3) Seleccione el reloj que vea de mejor manera.')
        titulo.setStyleSheet("font-size: 20px; border: 1px solid black;")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.adjustSize()
        self.siguiente = QPushButton('Siguiente') 
        self.siguiente.hide()

        self.opciones_widget = QWidget()
        opciones_layout = QHBoxLayout()
        self.opciones_widget.setLayout(opciones_layout)
        self.opciones = []
        for i in range(1, 4):
            opcion_layout = QVBoxLayout()
            opcion_imagen = QLabel(self)
            pixmap = QPixmap(f'MoCA/RELOJ/{i}.jpg')
            pixmap = pixmap.scaled(250, 250, Qt.KeepAspectRatio)
            opcion_imagen.setPixmap(pixmap)
            opcion_imagen.setAlignment(Qt.AlignCenter)
            boton = QPushButton(f'Opción {i}', self.opciones_widget)
            boton.clicked.connect(lambda checked, i=i: self.boton_precionado(i))
            self.opciones.append(boton)
            opcion_layout.addWidget(opcion_imagen)
            opcion_layout.addWidget(boton)
            opciones_layout.addLayout(opcion_layout)
        self.stacked_widget.addWidget(self.opciones_widget)

        for i in range(4, 7):
            opcion_layout = QVBoxLayout()
            opcion_imagen = QLabel(self)
            pixmap = QPixmap(f'MoCA/RELOJ/{i}.jpg')
            pixmap = pixmap.scaled(250, 250, Qt.KeepAspectRatio)
            opcion_imagen.setPixmap(pixmap)
            opcion_imagen.setAlignment(Qt.AlignCenter)
            boton = QPushButton(f'Opción {i}', self.opciones_widget)
            boton.clicked.connect(lambda checked, i=i: self.boton_precionado(i))
            self.opciones.append(boton)
            opcion_layout.addWidget(opcion_imagen)
            opcion_layout.addWidget(boton)
            opciones_layout.addLayout(opcion_layout)
        self.stacked_widget.addWidget(self.opciones_widget)

        setup.addWidget(titulo)
        setup.addWidget(self.stacked_widget)
        setup.addWidget(self.siguiente)
        self.setLayout(setup)
    
class Menu_Principal(QStackedWidget):
    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador

    def setup(self):
        self.setWindowTitle('AlzCare')
        self.setGeometry(100, 100, 640, 480)
        self.setStyleSheet("""
                           QWidget {
                            background-color: rgba(144, 224, 239, 0.5);  /* Azul claro opaco */
                            }
                            QPushButton {
                                background-color: #333;
                                color: white;
                                border: none;
                                border-radius: 25px;
                                padding: 10px;
                            }
                            QPushButton:hover {
                                background-color: #666;
                            }
                            QPushButton:pressed {
                                background-color: #999;
                            }
                        """)

        
        self.advertencia = Advertencia()
        self.menu_inicial = Menu_inicial()
        self.menu_login = Menu_Login()
        self.menu_registro_cuidador = Menu_registro_cuidador()
        self.menu_registro_paciente = Menu_registro_paciente()
        self.menu_pre_registro = Menu_pre_registro()
        self.advertencia_moca = Advertencia_Moca()
        self.menu_moca_1 = Menu_moca_1(self.controlador)
        self.menu_moca_2 = Menu_moca_2(self.controlador)
        self.menu_moca_3 = Menu_moca_3(self.controlador)
        
        self.addWidget(self.advertencia)
        self.addWidget(self.menu_inicial)
        self.addWidget(self.menu_login)
        self.addWidget(self.menu_pre_registro)
        self.addWidget(self.menu_registro_cuidador)
        self.addWidget(self.menu_registro_paciente)
        self.addWidget(self.advertencia_moca)
        self.addWidget(self.menu_moca_1)
        self.addWidget(self.menu_moca_2)
        self.addWidget(self.menu_moca_3)
        
        QTimer.singleShot(500, self.ventana_principal)
        
        self.menu_inicial.boton_login.clicked.connect(self.ventana_login)
        self.menu_inicial.boton_pre_registro.clicked.connect(self.ventana_pre_registro)
        self.menu_inicial.boton_moca.clicked.connect(self.ventana_advertencia_moca)
        self.menu_inicial.boton_salida.clicked.connect(self.close)
        
        self.menu_login.boton_login.clicked.connect(self.ventana_principal)
        self.menu_login.boton_volver.clicked.connect(self.ventana_principal)

        self.menu_pre_registro.boton_registro.clicked.connect(self.ventana_registro_cuidador)
        self.menu_pre_registro.boton_importar.clicked.connect(self.ventana_principal)
        self.menu_pre_registro.boton_volver.clicked.connect(self.ventana_principal)

        self.menu_registro_cuidador.boton_siguiente.clicked.connect(self.ventana_registro_paciente)
        self.menu_registro_cuidador.boton_volver.clicked.connect(self.ventana_pre_registro)

        self.menu_moca_1.siguiente.clicked.connect(self.ventana_moca_2)
        self.menu_moca_2.siguiente.clicked.connect(self.ventana_moca_3)

    def ventana_principal(self):
        self.setCurrentWidget(self.menu_inicial)
        
    def ventana_login(self):
        self.setCurrentWidget(self.menu_login)
        
    def ventana_pre_registro(self):
        self.setCurrentWidget(self.menu_pre_registro)

    def ventana_registro_cuidador(self):
        self.setCurrentWidget(self.menu_registro_cuidador)

    def ventana_registro_paciente(self):
        self.setCurrentWidget(self.menu_registro_paciente)
        
    def ventana_moca_1(self):
        self.setCurrentWidget(self.menu_moca_1)

    def ventana_moca_2(self):
        self.setCurrentWidget(self.menu_moca_2)

    def ventana_moca_3(self):
        self.setCurrentWidget(self.menu_moca_3)
        
    def ventana_advertencia_moca(self):
        self.setCurrentWidget(self.advertencia_moca)
        QTimer.singleShot(500, self.ventana_moca_1)

