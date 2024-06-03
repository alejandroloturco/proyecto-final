from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QVBoxLayout, QHBoxLayout ,QPushButton, QLabel, QStackedWidget, QLineEdit, QFormLayout, QComboBox, QStackedLayout, QMessageBox, QGraphicsView, QGraphicsScene, QGraphicsProxyWidget, QLabel, QGridLayout, QSpacerItem, QSizePolicy, QStatusBar
from PyQt5.QtCore  import QTimer, Qt, QTimer, QSize, QRect, QCoreApplication, QMetaObject
from PyQt5.QtGui  import QPixmap, QFont, QIcon

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

class Menu_moca_1(QWidget):
        def __init__(self, controlador):
            super().__init__()   
            self.controlador = controlador
            self.setWindowTitle('MOCA')
            setup = QVBoxLayout()
            self.view = QGraphicsView()
            self.scene = QGraphicsScene(self)
            self.view.setScene(self.scene)    
            self.secuencia_molde = ['1', 'A', '2', 'B', '3', 'C', '4', 'D', '5', 'E']
            self.posicion = 0 
            self.primer_intento = True
            titulo = QLabel('1) Selecciona en el orden correcto la siguiente secuencia de botones')
            titulo.setStyleSheet("font-size: 20px; border: 1px solid black;")
            titulo.setAlignment(Qt.AlignCenter)
            titulo.adjustSize()
            self.siguiente = QPushButton('Siguiente') 
            self.siguiente.hide()
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
                boton.setStyleSheet("""
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
                    QMessageBox.information(self, 'Correcto', 'Felicitaciones, la secuencia es correcta!')
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, controlador):
        self.ventanas_extra = QStackedWidget()
        self.controlador = controlador

        self.menu_moca_1 = Menu_moca_1(self.controlador)
        self.menu_moca_2 = Menu_moca_2(self.controlador)
        self.menu_moca_3 = Menu_moca_3(self.controlador)

        self.ventanas_extra.addWidget(self.menu_moca_1)
        self.ventanas_extra.addWidget(self.menu_moca_2)
        self.ventanas_extra.addWidget(self.menu_moca_3)


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(921, 612)
        MainWindow.setStyleSheet("QWidget {\n"
"    background-color: rgb(225, 250, 255);\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.icon_2 = QWidget(self.centralwidget)
        self.icon_2.setStyleSheet("QWidget {\n"
"    background-color:  rgb(144, 224, 239);\n"
"}\n"
"QPushButton{\n"
"    color: #0077b6;\n"
"    height: 30px;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: rgb(245, 250, 254);\n"
"    color: #1f95ef;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.icon_2.setObjectName("icon_2")
        self.verticalLayout_3 = QVBoxLayout(self.icon_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QLabel(self.icon_2)
        self.label.setMinimumSize(QSize(40, 40))
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setText("")
        self.label.setPixmap(QPixmap(r"Version_mario_proyecto_final/Recursos_Interfaz/Alzcare.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.boton_inicio1 = QPushButton(self.icon_2)
        self.boton_inicio1.setText("")
        icon = QIcon()
        icon.addPixmap(QPixmap(r"Version_mario_proyecto_final/Recursos_Interfaz/ppal.2.png"), QIcon.Normal, QIcon.Off)
        icon.addPixmap(QPixmap(r"Version_mario_proyecto_final/Recursos_Interfaz/ppal.png"), QIcon.Normal, QIcon.On)
        self.boton_inicio1.setIcon(icon)
        self.boton_inicio1.setIconSize(QSize(30, 30))
        self.boton_inicio1.setCheckable(True)
        self.boton_inicio1.setAutoExclusive(True)
        self.boton_inicio1.setObjectName("boton_inicio1")
        self.verticalLayout.addWidget(self.boton_inicio1)
        self.boton_ingreso1 = QPushButton(self.icon_2)
        self.boton_ingreso1.setText("")
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(r"Version_mario_proyecto_final/Recursos_Interfaz/ingresar1.png"), QIcon.Normal, QIcon.Off)
        icon1.addPixmap(QPixmap(r"Version_mario_proyecto_final/Recursos_Interfaz/ingresar.png"), QIcon.Normal, QIcon.On)
        self.boton_ingreso1.setIcon(icon1)
        self.boton_ingreso1.setIconSize(QSize(30, 30))
        self.boton_ingreso1.setCheckable(True)
        self.boton_ingreso1.setAutoExclusive(True)
        self.boton_ingreso1.setObjectName("boton_ingreso1")
        self.verticalLayout.addWidget(self.boton_ingreso1)
        self.boton_registro1 = QPushButton(self.icon_2)
        self.boton_registro1.setText("")
        icon2 = QIcon()
        icon2.addPixmap(QPixmap(r"Version_mario_proyecto_final/Recursos_Interfaz/Registro.png"), QIcon.Normal, QIcon.Off)
        icon2.addPixmap(QPixmap(r"Version_mario_proyecto_final/Recursos_Interfaz/Registro2.png"), QIcon.Normal, QIcon.On)
        self.boton_registro1.setIcon(icon2)
        self.boton_registro1.setIconSize(QSize(30, 30))
        self.boton_registro1.setCheckable(True)
        self.boton_registro1.setAutoExclusive(True)
        self.boton_registro1.setObjectName("boton_registro1")
        self.verticalLayout.addWidget(self.boton_registro1)
        self.boton_moca1 = QPushButton(self.icon_2)
        self.boton_moca1.setText("")
        icon3 = QIcon()
        icon3.addPixmap(QPixmap(r"Version_mario_proyecto_final/Recursos_Interfaz/Moca2.png"), QIcon.Normal, QIcon.Off)
        icon3.addPixmap(QPixmap(r"Version_mario_proyecto_final/Recursos_Interfaz/Moca1.png"), QIcon.Normal, QIcon.On)
        self.boton_moca1.setIcon(icon3)
        self.boton_moca1.setIconSize(QSize(30, 30))
        self.boton_moca1.setCheckable(True)
        self.boton_moca1.setAutoExclusive(True)
        self.boton_moca1.setObjectName("boton_moca1")
        self.verticalLayout.addWidget(self.boton_moca1)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem = QSpacerItem(20, 288, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.pushButton_6 = QPushButton(self.icon_2)
        self.pushButton_6.setText("")
        icon4 = QIcon()
        icon4.addPixmap(QPixmap(r"Version_mario_proyecto_final/Recursos_Interfaz/salir2.png"), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setIconSize(QSize(20, 20))
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_3.addWidget(self.pushButton_6)
        self.gridLayout.addWidget(self.icon_2, 0, 0, 1, 1)
        self.icon_1 = QWidget(self.centralwidget)
        self.icon_1.setStyleSheet("QWidget {\n"
"    background-color: rgb(144, 224, 239);\n"
"}\n"
"QPushButton{\n"
"    color: #F5FAFE;\n"
"    text-align: left;\n"
"    height: 30px;\n"
"    border: none;\n"
"    padding-left: 10px;\n"
"    border-top-left-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: rgb(245, 250, 254);\n"
"    color: #1f95ef;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.icon_1.setObjectName("icon_1")
        self.verticalLayout_4 = QVBoxLayout(self.icon_1)
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 10, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QLabel(self.icon_1)
        self.label_2.setMinimumSize(QSize(40, 40))
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setText("")
        self.label_2.setPixmap(QPixmap(r"Version_mario_proyecto_final/Recursos_Interfaz/Alzcare.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.boton_inicio2 = QPushButton(self.icon_1)
        font = QFont()
        font.setFamily("Montserrat")
        font.setBold(True)
        font.setWeight(75)
        self.boton_inicio2.setFont(font)
        self.boton_inicio2.setIcon(icon)
        self.boton_inicio2.setIconSize(QSize(30, 30))
        self.boton_inicio2.setCheckable(True)
        self.boton_inicio2.setAutoExclusive(True)
        self.boton_inicio2.setObjectName("boton_inicio2")
        self.verticalLayout_2.addWidget(self.boton_inicio2)
        self.boton_ingreso2 = QPushButton(self.icon_1)
        font = QFont()
        font.setFamily("Montserrat")
        font.setBold(True)
        font.setWeight(75)
        self.boton_ingreso2.setFont(font)
        self.boton_ingreso2.setIcon(icon1)
        self.boton_ingreso2.setIconSize(QSize(30, 30))
        self.boton_ingreso2.setCheckable(True)
        self.boton_ingreso2.setAutoExclusive(True)
        self.boton_ingreso2.setObjectName("boton_ingreso2")
        self.verticalLayout_2.addWidget(self.boton_ingreso2)
        self.boton_registro2 = QPushButton(self.icon_1)
        font = QFont()
        font.setFamily("Montserrat")
        font.setBold(True)
        font.setWeight(75)
        self.boton_registro2.setFont(font)
        self.boton_registro2.setIcon(icon2)
        self.boton_registro2.setIconSize(QSize(30, 30))
        self.boton_registro2.setCheckable(True)
        self.boton_registro2.setAutoExclusive(True)
        self.boton_registro2.setObjectName("boton_registro2")
        self.verticalLayout_2.addWidget(self.boton_registro2)
        self.boton_moca2 = QPushButton(self.icon_1)
        font = QFont()
        font.setFamily("Montserrat")
        font.setBold(True)
        font.setWeight(75)
        self.boton_moca2.setFont(font)
        self.boton_moca2.setIcon(icon3)
        self.boton_moca2.setIconSize(QSize(30, 30))
        self.boton_moca2.setCheckable(True)
        self.boton_moca2.setAutoExclusive(True)
        self.boton_moca2.setObjectName("boton_moca2")
        self.verticalLayout_2.addWidget(self.boton_moca2)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem1 = QSpacerItem(20, 288, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.pushButton_10 = QPushButton(self.icon_1)
        font = QFont()
        font.setFamily("Montserrat")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setIcon(icon4)
        self.pushButton_10.setIconSize(QSize(20, 20))
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_4.addWidget(self.pushButton_10)
        self.gridLayout.addWidget(self.icon_1, 0, 1, 1, 1)
        self.icon_menu = QWidget(self.centralwidget)
        self.icon_menu.setObjectName("icon_menu")
        self.verticalLayout_5 = QVBoxLayout(self.icon_menu)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget = QWidget(self.icon_menu)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Boton_menu = QPushButton(self.widget)
        self.Boton_menu.setStyleSheet("border: none;")
        self.Boton_menu.setText("")
        icon5 = QIcon()
        icon5.addPixmap(QPixmap(r"Version_mario_proyecto_final/Recursos_Interfaz/Menu.png"), QIcon.Normal, QIcon.Off)
        self.Boton_menu.setIcon(icon5)
        self.Boton_menu.setIconSize(QSize(30, 30))
        self.Boton_menu.setCheckable(True)
        self.Boton_menu.setObjectName("Boton_menu")
        self.horizontalLayout_3.addWidget(self.Boton_menu)
        spacerItem2 = QSpacerItem(450, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pushButton_13 = QPushButton(self.widget)
        self.pushButton_13.setStyleSheet("border:none;\n"
"")
        self.pushButton_13.setText("")
        icon6 = QIcon()
        icon6.addPixmap(QPixmap(r"Version_mario_proyecto_final/Recursos_Interfaz/ingresar.png"), QIcon.Normal, QIcon.Off)
        self.pushButton_13.setIcon(icon6)
        self.pushButton_13.setIconSize(QSize(30, 30))
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_3.addWidget(self.pushButton_13)
        self.verticalLayout_5.addWidget(self.widget)
        self.stackedWidget = QStackedWidget(self.icon_menu)
        self.stackedWidget.setStyleSheet("QWidget{\n"
"    background-color:rgb(255, 255, 255);}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.pag_inicio = QWidget()
        self.pag_inicio.setObjectName("pag_inicio")
        self.label_3 = QLabel(self.pag_inicio)
        self.label_3.setGeometry(QRect(80, 0, 511, 101))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel {\n"
"    color: rgb(0, 119, 182);\n"
"}\n"
"")
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_7 = QLabel(self.pag_inicio)
        self.label_7.setGeometry(QRect(180, 450, 321, 31))
        font = QFont()
        font.setFamily("Montserrat")
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QLabel(self.pag_inicio)
        self.label_8.setGeometry(QRect(30, 200, 161, 191))
        self.label_8.setText("")
        self.label_8.setPixmap(QPixmap(r"Version_mario_proyecto_final/Recursos_Interfaz/Ingreso_nuevos_pacientes.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QLabel(self.pag_inicio)
        self.label_9.setGeometry(QRect(470, 200, 161, 191))
        self.label_9.setText("")
        self.label_9.setPixmap(QPixmap(r"Version_mario_proyecto_final/Recursos_Interfaz/Seguimiento_pacientes.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QLabel(self.pag_inicio)
        self.label_10.setGeometry(QRect(260, 200, 151, 191))
        self.label_10.setText("")
        self.label_10.setPixmap(QPixmap(r"Version_mario_proyecto_final/Recursos_Interfaz/Moca.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_12 = QLabel(self.pag_inicio)
        self.label_12.setGeometry(QRect(300, 210, 91, 16))
        font = QFont()
        font.setFamily("Montserrat")
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QLabel(self.pag_inicio)
        self.label_13.setGeometry(QRect(510, 210, 91, 16))
        font = QFont()
        font.setFamily("Montserrat")
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QLabel(self.pag_inicio)
        self.label_14.setGeometry(QRect(260, 140, 181, 21))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("QLabel {\n"
"    color: rgb(0, 119, 182);\n"
"}\n"
"")
        self.label_14.setObjectName("label_14")
        self.widget_2 = QWidget(self.pag_inicio)
        self.widget_2.setGeometry(QRect(-120, 110, 921, 21))
        self.widget_2.setStyleSheet("QWidget {\n"
"    background-color: rgb(144, 224, 239);\n"
"}\n"
"")
        self.widget_2.setObjectName("widget_2")
        self.widget_3 = QWidget(self.pag_inicio)
        self.widget_3.setGeometry(QRect(0, 420, 971, 16))
        self.widget_3.setStyleSheet("QWidget {\n"
"    background-color: rgb(144, 224, 239);\n"
"}\n"
"\n"
"")
        self.widget_3.setObjectName("widget_3")
        self.label_15 = QLabel(self.pag_inicio)
        self.label_15.setGeometry(QRect(670, 480, 16, 16))
        self.label_15.setText("")
        self.label_15.setPixmap(QPixmap(r"Version_mario_proyecto_final/Recursos_Interfaz/cop2.png"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        self.label_16 = QLabel(self.pag_inicio)
        self.label_16.setGeometry(QRect(610, 480, 55, 16))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("QLabel {\n"
"    color: rgb(0, 119, 182);\n"
"}\n"
"\n"
"")
        self.label_16.setObjectName("label_16")
        self.label_11 = QLabel(self.pag_inicio)
        self.label_11.setGeometry(QRect(40, 210, 181, 16))
        font = QFont()
        font.setFamily("Montserrat")
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.stackedWidget.addWidget(self.pag_inicio)
        self.pag_ingresar = QWidget()
        self.pag_ingresar.setObjectName("pag_ingresar")
        self.label_19 = QLabel(self.pag_ingresar)
        self.label_19.setGeometry(QRect(10, 30, 661, 21))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QLabel(self.pag_ingresar)
        self.label_20.setGeometry(QRect(10, 90, 651, 21))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("QLabel {\n"
"    color: rgb(0, 119, 182);\n"
"}\n"
"")
        self.label_20.setObjectName("label_20")
        self.label_21 = QLabel(self.pag_ingresar)
        self.label_21.setGeometry(QRect(10, 120, 611, 20))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("QLabel {\n"
"    color: rgb(0, 119, 182);\n"
"}\n"
"")
        self.label_21.setObjectName("label_21")
        self.label_22 = QLabel(self.pag_ingresar)
        self.label_22.setGeometry(QRect(240, 200, 171, 171))
        self.label_22.setText("")
        self.label_22.setPixmap(QPixmap(r"Version_mario_proyecto_final/Recursos_Interfaz/Alzcare.png"))
        self.label_22.setScaledContents(True)
        self.label_22.setObjectName("label_22")
        self.stackedWidget.addWidget(self.pag_ingresar)
        self.pag_registro = QWidget()
        self.pag_registro.setObjectName("pag_registro")
        self.label_5 = QLabel(self.pag_registro)
        self.label_5.setGeometry(QRect(10, 20, 661, 41))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_4 = QLabel(self.pag_registro)
        self.label_4.setGeometry(QRect(10, 90, 711, 20))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel {\n"
"    color: rgb(0, 119, 182);\n"
"}\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_17 = QLabel(self.pag_registro)
        self.label_17.setGeometry(QRect(10, 120, 631, 20))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("QLabel {\n"
"    color: rgb(0, 119, 182);\n"
"}\n"
"")
        self.label_17.setObjectName("label_17")
        self.label_18 = QLabel(self.pag_registro)
        self.label_18.setGeometry(QRect(240, 200, 171, 171))
        self.label_18.setText("")
        self.label_18.setPixmap(QPixmap(r"Version_mario_proyecto_final/Recursos_Interfaz/Alzcare.png"))
        self.label_18.setScaledContents(True)
        self.label_18.setObjectName("label_18")
        self.stackedWidget.addWidget(self.pag_registro)
        self.pag_moka = QWidget()
        self.pag_moka.setObjectName("pag_moka")
        self.label_6 = QLabel(self.pag_moka)
        self.label_6.setGeometry(QRect(10, 20, 681, 41))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_23 = QLabel(self.pag_moka)
        self.label_23.setGeometry(QRect(10, 60, 341, 21))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QLabel(self.pag_moka)
        self.label_24.setGeometry(QRect(10, 100, 661, 21))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("QLabel {\n"
"    color: rgb(0, 119, 182);\n"
"}\n"
"\n"
"")
        self.label_24.setObjectName("label_24")
        self.label_25 = QLabel(self.pag_moka)
        self.label_25.setGeometry(QRect(10, 130, 151, 21))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("QLabel {\n"
"    color: rgb(0, 119, 182);\n"
"}\n"
"")
        self.label_25.setObjectName("label_25")
        self.label_26 = QLabel(self.pag_moka)
        self.label_26.setGeometry(QRect(240, 200, 171, 171))
        self.label_26.setText("")
        self.label_26.setPixmap(QPixmap(r"Version_mario_proyecto_final/Recursos_Interfaz/Alzcare.png"))
        self.label_26.setScaledContents(True)
        self.label_26.setObjectName("label_26")
        self.stackedWidget.addWidget(self.pag_moka)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.gridLayout.addWidget(self.icon_menu, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.Boton_menu.toggled['bool'].connect(self.icon_2.setHidden)
        self.Boton_menu.toggled['bool'].connect(self.icon_1.setVisible)
        self.boton_moca1.toggled['bool'].connect(self.boton_moca2.setChecked)
        self.boton_registro1.toggled['bool'].connect(self.boton_registro2.setChecked)
        self.boton_ingreso1.toggled['bool'].connect(self.boton_ingreso2.setChecked)
        self.boton_inicio1.toggled['bool'].connect(self.boton_inicio2.setChecked)
        self.boton_inicio2.toggled['bool'].connect(self.boton_inicio1.setChecked)
        self.boton_ingreso2.toggled['bool'].connect(self.boton_ingreso1.setChecked)
        self.boton_registro2.toggled['bool'].connect(self.boton_registro1.setChecked)
        self.boton_moca2.toggled['bool'].connect(self.boton_moca1.setChecked)
        self.pushButton_6.toggled['bool'].connect(MainWindow.close)
        self.pushButton_10.toggled['bool'].connect(MainWindow.close)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.boton_inicio2.setText(_translate("MainWindow", "Inicio"))
        self.boton_ingreso2.setText(_translate("MainWindow", "Ingresar"))
        self.boton_registro2.setText(_translate("MainWindow", "Registro"))
        self.boton_moca2.setText(_translate("MainWindow", "Moca"))
        self.pushButton_10.setText(_translate("MainWindow", "Salir"))
        self.label_3.setText(_translate("MainWindow", "\"Tu asistente personal para una vida mejor\""))
        self.label_7.setText(_translate("MainWindow", "Faciltando la vida con Alzheimer, un día a la vez"))
        self.label_12.setText(_translate("MainWindow", "Test moca"))
        self.label_13.setText(_translate("MainWindow", "Seguimiento"))
        self.label_14.setText(_translate("MainWindow", "Nuestros servicios"))
        self.label_16.setText(_translate("MainWindow", "alzcare"))
        self.label_11.setText(_translate("MainWindow", "Ingreso de pacientes"))
        self.label_19.setText(_translate("MainWindow", "Por favor , tenga en cuenta que el ingreso se realizará en una ventana nueva."))
        self.label_20.setText(_translate("MainWindow", "Importante: El paciente debe estar en compañía del cuidador durante el registro para"))
        self.label_21.setText(_translate("MainWindow", "garantizar que toda la información se complete correctamente y con seguridad."))
        self.label_5.setText(_translate("MainWindow", "Por favor , tenga en cuenta que el proceso de registro se realizará en una ventana nueva."))
        self.label_4.setText(_translate("MainWindow", "Importante: El paciente debe estar en compañía del cuidador durante el registro para"))
        self.label_17.setText(_translate("MainWindow", "garantizar que toda la información se complete correctamente y con seguridad."))
        self.label_6.setText(_translate("MainWindow", "La Evaluación Cognitiva de MoCA , fue diseñada como un instrumento de detección rápida"))
        self.label_23.setText(_translate("MainWindow", "de la disfunción cognitiva leve. "))
        self.label_24.setText(_translate("MainWindow", "Tenga en cuenta: que el test proporcionado en esta aplicación es una versión adaptada"))
        self.label_25.setText(_translate("MainWindow", "del test original. "))

class Log_in(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(904, 610)
        Form.setMaximumSize(QSize(1000, 1000))
        self.widget_2 = QWidget(Form)
        self.widget_2.setGeometry(QRect(0, 0, 461, 641))
        self.widget_2.setStyleSheet("QWidget {\n"
"    background-color: rgb(225, 255, 255);\n"
"}\n"
"")
        self.widget_2.setObjectName("widget_2")
        self.label = QLabel(self.widget_2)
        self.label.setGeometry(QRect(140, 240, 191, 191))
        self.label.setText("")
        self.label.setPixmap(QPixmap(r"Version_mario_proyecto_final/Recursos_Interfaz/Alzcare.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.widget = QWidget(Form)
        self.widget.setGeometry(QRect(460, -10, 451, 631))
        self.widget.setStyleSheet("QWidget {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #0077b6, stop:0.5 #0096c7, stop:1 #00b4d8);\n"
"}\n"
"\n"
"QLabel {\n"
"    background-color: transparent;  /* Fondo transparente para QLabel */\n"
"    color: white;  /* Color del texto del QLabel */\n"
"    font-size: 16px;  /* Tamaño de fuente del QLabel */\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: white;  /* Fondo sólido blanco para QLineEdit */\n"
"    border: 2px solid #00b4d8;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    color: black;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #0077b6; /* Color del borde al enfocar */\n"
"    outline: none;\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"    border-radius: 10px;\n"
"    background-color: rgb(0, 180, 216);\n"
"}")
        self.widget.setObjectName("widget")
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setGeometry(QRect(-10, 0, 16, 641))
        self.widget_3.setStyleSheet("QWidget {\n"
"    background-color: rgb(0, 180, 216);\n"
"}\n"
"")
        self.widget_3.setObjectName("widget_3")
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setGeometry(QRect(80, 370, 291, 31))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setGeometry(QRect(80, 220, 291, 41))
        self.lineEdit.setAccessibleDescription("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QRect(80, 300, 291, 41))
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QLabel(self.widget)
        self.label_2.setGeometry(QRect(80, 180, 61, 31))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QLabel(self.widget)
        self.label_3.setGeometry(QRect(80, 270, 101, 21))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QLabel(self.widget)
        self.label_4.setGeometry(QRect(60, 70, 341, 61))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setGeometry(QRect(110, 560, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setGeometry(QRect(270, 560, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        self.pushButton_3.clicked.connect(Form.close) # type: ignore
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_2.setText(_translate("Form", "Ingresar"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"right\">Usuario:</p><p align=\"right\"><br/></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"right\">Contraseña:</p><p align=\"right\"><br/></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p>Bienvenido a Alzcare, por favor ingrese </p><p>sus credenciales para continuar</p></body></html>"))
        self.pushButton.setText(_translate("Form", "Regresar"))
        self.pushButton_3.setText(_translate("Form", "Salir"))

class Formato_Log_in(QDialog):
    def __init__(self, parent=None):
        super(Formato_Log_in, self).__init__(parent)
        self.ui = Log_in()
        self.ui.setupUi(self)

class Pre_Registro(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(901, 612)
        self.widget = QWidget(Form)
        self.widget.setGeometry(QRect(0, 0, 471, 651))
        self.widget.setStyleSheet("QWidget {\n"
"    background-color: rgb(225, 255, 255);\n"
"}\n"
"\n"
"QLabel{\n"
"    color:white;\n"
"}")
        self.widget.setObjectName("widget")
        self.label = QLabel(self.widget)
        self.label.setGeometry(QRect(130, 230, 191, 191))
        self.label.setText("")
        self.label.setPixmap(QPixmap(r"Version_mario_proyecto_final/Recursos_Interfaz/Alzcare.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.widget_2 = QWidget(Form)
        self.widget_2.setGeometry(QRect(450, 0, 471, 621))
        self.widget_2.setStyleSheet("QWidget {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #0077b6, stop:0.5 #0096c7, stop:1 #00b4d8);\n"
"}\n"
"\n"
"QLabel {\n"
"    background-color: transparent;  /* Fondo transparente para QLabel */\n"
"    color: white;  /* Color del texto del QLabel */\n"
"    font-size: 16px;  /* Tamaño de fuente del QLabel */\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: white;  /* Fondo sólido blanco para QLineEdit */\n"
"    border: 2px solid #00b4d8;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    color: black;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #0077b6; /* Color del borde al enfocar */\n"
"    outline: none;\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"    border-radius: 10px;\n"
"    background-color: rgb(0, 180, 216);\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setGeometry(QRect(-10, 0, 16, 641))
        self.widget_3.setStyleSheet("QWidget {\n"
"    background-color: rgb(0, 180, 216);\n"
"}\n"
"")
        self.widget_3.setObjectName("widget_3")
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setGeometry(QRect(30, 40, 341, 61))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_regresar = QPushButton(self.widget_2)
        self.pushButton_regresar.setGeometry(QRect(90, 560, 93, 28))
        self.pushButton_regresar.setObjectName("pushButton_regresar")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setGeometry(QRect(30, 230, 171, 191))
        self.label_2.setText("")
        self.label_2.setPixmap(QPixmap(":/prefijoNuevo/Img_interfaz2/paciente.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setGeometry(QRect(240, 250, 171, 171))
        self.label_3.setText("")
        self.label_3.setPixmap(QPixmap(":/prefijoNuevo/Img_interfaz2/cuidador.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.pushButton_salir = QPushButton(self.widget_2)
        self.pushButton_salir.setGeometry(QRect(250, 560, 93, 28))
        self.pushButton_salir.setObjectName("pushButton_salir")
        self.pushButton_paciente = QPushButton(self.widget_2)
        self.pushButton_paciente.setGeometry(QRect(70, 230, 93, 28))
        self.pushButton_paciente.setStyleSheet("QPusButton{\n"
"    background-color: rgb(225, 255, 255);\n"
"}")
        self.pushButton_paciente.setObjectName("pushButton_paciente")
        self.pushButton_cuidador = QPushButton(self.widget_2)
        self.pushButton_cuidador.setGeometry(QRect(280, 230, 93, 28))
        self.pushButton_cuidador.setObjectName("pushButton_cuidador")

        self.retranslateUi(Form)
        self.pushButton_salir.clicked['bool'].connect(Form.close) 
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p>Bienvenido a Alzcare, por favor seleccione</p><p>el tipo de usuario a registrar</p></body></html>"))
        self.pushButton_regresar.setText(_translate("Form", "Regresar"))
        self.pushButton_salir.setText(_translate("Form", "Salir"))
        self.pushButton_paciente.setText(_translate("Form", "Paciente"))
        self.pushButton_cuidador.setText(_translate("Form", "Cuidador"))

class Formato_Pre_Registro(QDialog):
    def __init__(self, parent=None):
        super(Formato_Pre_Registro, self).__init__(parent)
        self.ui = Pre_Registro()
        self.ui.setupUi(self)

class Botonera(QMainWindow, Ui_MainWindow):
    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador
        self.setupUi(self,self.controlador)

        self.menu_login = Formato_Log_in()
        self.menu_registro = Formato_Pre_Registro()

        self.icon_2.setHidden(True)
        
        self.boton_inicio1.clicked.connect(self.boton_paginaInicio)
        self.boton_inicio2.clicked.connect(self.boton_paginaInicio)
        
        self.boton_ingreso1.clicked.connect(self.boton_paginaIngreso)
        self.boton_ingreso2.clicked.connect(self.boton_paginaIngreso)

        self.boton_registro1.clicked.connect(self.boton_paginaRegistro)
        self.boton_registro2.clicked.connect(self.boton_paginaRegistro)

        self.boton_moca1.clicked.connect(self.boton_paginaMoca)
        self.boton_moca2.clicked.connect(self.boton_paginaMoca)

        self.menu_login.ui.pushButton.clicked.connect(self.ventanas_inicio)
        self.menu_login.ui.pushButton_2.clicked.connect(self.ventana_seguimiento)

    def ventanas_inicio(self):
        self.menu_login.close()
        self.menu_registro.close()
        self.show()
        self.stackedWidget.setCurrentIndex(0)
        
    def boton_paginaInicio(self):
        self.stackedWidget.setCurrentIndex(0)
    
    def boton_paginaIngreso(self):
        self.stackedWidget.setCurrentIndex(1)
        QTimer.singleShot(4000, self.ventana_login)
    
    def ventana_login(self):
        self.close()
        self.menu_login.show()
    
    def boton_paginaRegistro(self):
        self.stackedWidget.setCurrentIndex(2)
        QTimer.singleShot(4000, self.ventana_registro)
    
    def ventana_registro(self):
        self.close()
        self.menu_registro.show()
    
    def boton_paginaMoca(self):
        self.stackedWidget.setCurrentIndex(3)

    def ventana_seguimiento(self):
        usuario = self.menu_login.ui.lineEdit.text()
        contrasena = self.menu_login.ui.lineEdit_2.text()
        if self.controlador.validar_usuario(usuario, contrasena):
            self.close()
            self.menu_seguimiento.show()
        else:
            QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos")
