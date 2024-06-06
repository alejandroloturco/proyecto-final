from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QVBoxLayout, QHBoxLayout ,QPushButton, QLabel, QStackedWidget, QLineEdit, QFormLayout, QComboBox, QStackedLayout, QMessageBox, QGraphicsView, QGraphicsScene, QGraphicsProxyWidget, QLabel, QGridLayout, QSpacerItem, QSizePolicy, QStatusBar, QFileDialog
from PyQt5.QtCore  import QTimer, Qt, QTimer, QSize, QRect, QCoreApplication, QMetaObject, QRegExp
from PyQt5.QtGui  import QPixmap, QFont, QIcon, QRegExpValidator, QIntValidator
import webbrowser
import random

class Alzcare(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(820, 590)
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
        self.label.setPixmap(QPixmap(r"Recursos_Interfaz/Alzcare.png"))
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
        icon.addPixmap(QPixmap(r"Recursos_Interfaz/ppal.2.png"), QIcon.Normal, QIcon.Off)
        icon.addPixmap(QPixmap(r"Recursos_Interfaz/ppal.png"), QIcon.Normal, QIcon.On)
        self.boton_inicio1.setIcon(icon)
        self.boton_inicio1.setIconSize(QSize(30, 30))
        self.boton_inicio1.setCheckable(True)
        self.boton_inicio1.setAutoExclusive(True)
        self.boton_inicio1.setObjectName("boton_inicio1")
        self.verticalLayout.addWidget(self.boton_inicio1)
        self.boton_ingreso1 = QPushButton(self.icon_2)
        self.boton_ingreso1.setText("")
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(r"Recursos_Interfaz/ingresar1.png"), QIcon.Normal, QIcon.Off)
        icon1.addPixmap(QPixmap(r"Recursos_Interfaz/ingresar.png"), QIcon.Normal, QIcon.On)
        self.boton_ingreso1.setIcon(icon1)
        self.boton_ingreso1.setIconSize(QSize(30, 30))
        self.boton_ingreso1.setCheckable(True)
        self.boton_ingreso1.setAutoExclusive(True)
        self.boton_ingreso1.setObjectName("boton_ingreso1")
        self.verticalLayout.addWidget(self.boton_ingreso1)
        self.boton_registro1 = QPushButton(self.icon_2)
        self.boton_registro1.setText("")
        icon2 = QIcon()
        icon2.addPixmap(QPixmap(r"Recursos_Interfaz/Registro.png"), QIcon.Normal, QIcon.Off)
        icon2.addPixmap(QPixmap(r"Recursos_Interfaz/Registro2.png"), QIcon.Normal, QIcon.On)
        self.boton_registro1.setIcon(icon2)
        self.boton_registro1.setIconSize(QSize(30, 30))
        self.boton_registro1.setCheckable(True)
        self.boton_registro1.setAutoExclusive(True)
        self.boton_registro1.setObjectName("boton_registro1")
        self.verticalLayout.addWidget(self.boton_registro1)
        self.boton_moca1 = QPushButton(self.icon_2)
        self.boton_moca1.setText("")
        icon3 = QIcon()
        icon3.addPixmap(QPixmap(r"Recursos_Interfaz/Moca2.png"), QIcon.Normal, QIcon.Off)
        icon3.addPixmap(QPixmap(r"Recursos_Interfaz/Moca1.png"), QIcon.Normal, QIcon.On)
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
        icon4.addPixmap(QPixmap(r"Recursos_Interfaz/salir2.png"), QIcon.Normal, QIcon.Off)
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
        self.label_2.setPixmap(QPixmap(r"Recursos_Interfaz/Alzcare.png"))
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
        icon5.addPixmap(QPixmap(r"Recursos_Interfaz/Menu.png"), QIcon.Normal, QIcon.Off)
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
        icon6.addPixmap(QPixmap(r"Recursos_Interfaz/ingresar.png"), QIcon.Normal, QIcon.Off)
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
        self.label_8.setPixmap(QPixmap(r"Recursos_Interfaz/Ingreso_nuevos_pacientes.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QLabel(self.pag_inicio)
        self.label_9.setGeometry(QRect(470, 200, 161, 191))
        self.label_9.setText("")
        self.label_9.setPixmap(QPixmap(r"Recursos_Interfaz/Seguimiento_pacientes.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QLabel(self.pag_inicio)
        self.label_10.setGeometry(QRect(260, 200, 151, 191))
        self.label_10.setText("")
        self.label_10.setPixmap(QPixmap(r"Recursos_Interfaz/Moca.png"))
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
        self.label_15.setPixmap(QPixmap(r"Recursos_Interfaz/cop2.png"))
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
        self.label_22.setPixmap(QPixmap(r"Recursos_Interfaz/Alzcare.png"))
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
        self.label_18.setPixmap(QPixmap(r"Recursos_Interfaz/Alzcare.png"))
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
        self.label_26.setPixmap(QPixmap(r"Recursos_Interfaz/Alzcare.png"))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Alzcare®"))
        MainWindow.setWindowIcon(QIcon(r'Recursos_Interfaz\Alzcare.png'))
        self.boton_inicio2.setText(_translate("MainWindow", "Inicio"))
        self.boton_ingreso2.setText(_translate("MainWindow", "Ingresar"))
        self.boton_registro2.setText(_translate("MainWindow", "Registro"))
        self.boton_moca2.setText(_translate("MainWindow", "Moca"))
        self.pushButton_10.setText(_translate("MainWindow", "Salir"))
        x = random.sample(range(0, 7), 7)
        if x[0] == 0:
            self.label_3.setText(_translate("MainWindow", "\"Tu asistente personal para una vida mejor\"")) 
        elif x[0] == 1:
            self.label_3.setText(_translate("MainWindow", "\"Facilitando la vida con Alzheimer, un día a la vez\""))
        elif x[0] == 2:
            self.label_3.setText(_translate("MainWindow", "\"Cuidando a los que cuidan\""))
        elif x[0] == 3:
            self.label_3.setText(_translate("MainWindow", "\"Alzcare, tu mejor opción\""))
        elif x[0] == 4:
            self.label_3.setText(_translate("MainWindow", "\"Un día a la vez, un paso a la vez\""))
        elif x[0] == 5:
            self.label_3.setText(_translate("MainWindow", "\"Nos importa tu bienestar. Te acompañamos en cada paso\""))
        elif x[0] == 6:
            self.label_3.setText(_translate("MainWindow", "\"Cuidamos de ti con dedicación y cariño diario\""))
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
        self.label_24.setText(_translate("MainWindow", "Tenga en cuenta: Se abrira una pestaña en su navegador que mostrará la versión mas actualizada"))
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
        self.label.setPixmap(QPixmap(r"Recursos_Interfaz/Alzcare.png"))
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
        self.pushButton_3.clicked.connect(Form.close)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Log in"))
        Form.setWindowIcon(QIcon(r"Recursos_Interfaz\Alzcare.png"))
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
        self.label.setPixmap(QPixmap(r"Recursos_Interfaz\Alzcare.png"))
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
"    color: white;\n"
"    background-color: rgb(0, 119, 182)\n"
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
        font.setPointSize(1)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setGeometry(QRect(30, 230, 171, 191))
        self.label_2.setText("")
        self.label_2.setPixmap(QPixmap(r"Recursos_Interfaz\paciente.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setGeometry(QRect(240, 250, 171, 171))
        self.label_3.setText("")
        self.label_3.setPixmap(QPixmap(r"Recursos_Interfaz\cuidador.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.pushButton_paciente = QPushButton(self.widget_2)
        self.pushButton_paciente.setGeometry(QRect(70, 230, 93, 28))
        self.pushButton_paciente.setStyleSheet("QPusButton{\n"
"    background-color: rgb(225, 255, 255);\n"
"}")
        self.pushButton_paciente.setObjectName("pushButton_paciente")
        self.pushButton_cuidador = QPushButton(self.widget_2)
        self.pushButton_cuidador.setGeometry(QRect(280, 230, 93, 28))
        self.pushButton_cuidador.setObjectName("pushButton_cuidador")
        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setGeometry(QRect(290, 570, 141, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_regresar = QPushButton(self.widget_2)
        self.pushButton_regresar.setGeometry(QRect(170, 570, 93, 28))
        self.pushButton_regresar.setObjectName("pushButton_regresar")
        self.pushButton_salir = QPushButton(self.widget_2)
        self.pushButton_salir.setGeometry(QRect(40, 570, 93, 28))
        self.pushButton_salir.setObjectName("pushButton_salir")

        self.retranslateUi(Form)
        self.pushButton_salir.clicked['bool'].connect(Form.close)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Selección de registro"))
        Form.setWindowIcon(QIcon(r"Recursos_Interfaz\Alzcare.png"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p>Bienvenido a Alzcare, por favor seleccione</p><p>el tipo de usuario a registrar</p></body></html>"))
        self.pushButton_paciente.setText(_translate("Form", "Paciente"))
        self.pushButton_cuidador.setText(_translate("Form", "Cuidador"))
        self.pushButton.setText(_translate("Form", "Importar información"))
        self.pushButton_regresar.setText(_translate("Form", "Regresar"))
        self.pushButton_salir.setText(_translate("Form", "Salir"))

class Formato_Pre_Registro(QDialog):
    def __init__(self, parent=None):
        super(Formato_Pre_Registro, self).__init__(parent)
        self.ui = Pre_Registro()
        self.ui.setupUi(self)

class Registro_Cuidador(object):
    def setupUi(self, Form):
        restriccion = QRegExp("[a-z A-Z]+")
        Form.setObjectName("Form")
        Form.resize(936, 700)
        self.widget = QWidget(Form)
        self.widget.setGeometry(QRect(0, 0, 941, 721))
        font = QFont()
        font.setPointSize(15)
        self.widget.setFont(font)
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
"    color: white;\n"
"    background-color: rgb(0, 119, 182)\n"
"}")
        self.widget.setObjectName("widget")
        self.label = QLabel(self.widget)
        self.label.setGeometry(QRect(300, 10, 421, 91))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_nombre = QLineEdit(self.widget)
        self.lineEdit_nombre.setGeometry(QRect(440, 170, 421, 51))
        font = QFont()
        font.setPointSize(1)
        input_validator = QRegExpValidator(restriccion)
        self.lineEdit_nombre.setFont(font)
        self.lineEdit_nombre.setObjectName("lineEdit_nombre")
        self.lineEdit_nombre.setValidator(input_validator)
        self.lineEdit_apellido = QLineEdit(self.widget)
        self.lineEdit_apellido.setGeometry(QRect(440, 230, 421, 51))
        self.lineEdit_apellido.setObjectName("lineEdit_apellido")
        self.lineEdit_apellido.setValidator(input_validator)
        self.lineEdit_usuario = QLineEdit(self.widget)
        self.lineEdit_usuario.setGeometry(QRect(440, 290, 421, 51))
        self.lineEdit_usuario.setEchoMode(QLineEdit.Normal)
        self.lineEdit_usuario.setObjectName("lineEdit_usuario")
        self.lineEdit_cedula = QLineEdit(self.widget)
        self.lineEdit_cedula.setGeometry(QRect(440, 350, 421, 51))
        self.lineEdit_cedula.setObjectName("lineEdit_cedula")
        self.lineEdit_cedula.setValidator(QIntValidator())
        self.lineEdit_cedula.setMaxLength(10)
        self.label_2 = QLabel(self.widget)
        self.label_2.setGeometry(QRect(350, 180, 81, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QLabel(self.widget)
        self.label_3.setGeometry(QRect(320, 360, 111, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QLabel(self.widget)
        self.label_4.setGeometry(QRect(340, 420, 91, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QLabel(self.widget)
        self.label_5.setGeometry(QRect(250, 480, 181, 31))
        self.label_5.setObjectName("label_5")
        self.pushButton_ = QPushButton(self.widget)
        self.pushButton_.setGeometry(QRect(440, 610, 421, 31))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        self.pushButton_.setFont(font)
        self.pushButton_.setStyleSheet("")
        self.pushButton_.setObjectName("pushButton_")
        self.label_7 = QLabel(self.widget)
        self.label_7.setGeometry(QRect(300, 80, 261, 20))
        self.label_7.setObjectName("label_7")
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setGeometry(QRect(60, 610, 93, 28))
        font = QFont()
        font.setPointSize(9)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setGeometry(QRect(200, 610, 93, 28))
        font = QFont()
        font.setPointSize(9)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_contrasena = QLineEdit(self.widget)
        self.lineEdit_contrasena.setGeometry(QRect(440, 410, 421, 51))
        self.lineEdit_contrasena.setEchoMode(QLineEdit.Password)
        self.lineEdit_contrasena.setObjectName("lineEdit_contrasena")
        self.lineEdit_celular = QLineEdit(self.widget)
        self.lineEdit_celular.setGeometry(QRect(440, 470, 421, 51))
        self.lineEdit_celular.setObjectName("lineEdit_celular")
        self.lineEdit_celular.setValidator(QIntValidator())
        self.lineEdit_celular.setMaxLength(10)
        self.label_6 = QLabel(self.widget)
        self.label_6.setGeometry(QRect(320, 240, 111, 21))
        self.label_6.setObjectName("label_6")
        self.label_8 = QLabel(self.widget)
        self.label_8.setGeometry(QRect(250, 540, 181, 31))
        self.label_8.setObjectName("label_8")
        self.lineEdit_formacion = QLineEdit(self.widget)
        self.lineEdit_formacion.setGeometry(QRect(440, 530, 421, 51))
        self.lineEdit_formacion.setObjectName("lineEdit_formacion")
        self.label_9 = QLabel(self.widget)
        self.label_9.setGeometry(QRect(320, 300, 111, 21))
        self.label_9.setObjectName("label_9")

        self.retranslateUi(Form)
        self.pushButton_3.clicked['bool'].connect(Form.close)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Registro Cuidador"))
        Form.setWindowIcon(QIcon(r"Recursos_Interfaz\Alzcare.png"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt;\">REGISTRO DEL CUIDADOR</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">Nombre: </span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"right\">Cédula: </p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">Contraseña: </span></p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p align=\"right\">Celular:</p></body></html>"))
        self.pushButton_.setText(_translate("Form", "Aceptar"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt;\">Complete los siguientes campos</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Form", "Regresar"))
        self.pushButton_3.setText(_translate("Form", "Salir"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p align=\"right\">Apellido: </p></body></html>"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p align=\"right\">Formación:</p></body></html>"))
        self.label_9.setText(_translate("Form", "<html><head/><body><p align=\"right\">Usuario:</p></body></html>"))

class Formato_Registro_Cuidador(QDialog):
    def __init__(self, parent=None):
        super(Formato_Registro_Cuidador, self).__init__(parent)
        self.ui = Registro_Cuidador()
        self.ui.setupUi(self)

class Registro_Paciente(object):
    def setupUi(self, Form):
        restriccion = QRegExp("[a-z A-Z]+")
        Form.setObjectName("Form")
        Form.resize(924, 792)
        self.widget = QWidget(Form)
        self.widget.setGeometry(QRect(-10, -10, 1221, 871))
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
"    color: white;\n"
"    background-color: rgb(0, 119, 182)\n"
"}")
        self.widget.setObjectName("widget")
        self.label = QLabel(self.widget)
        self.label.setGeometry(QRect(320, 0, 421, 91))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        input_validator = QRegExpValidator(restriccion)
        self.lineEdit_nombre = QLineEdit(self.widget)
        self.lineEdit_nombre.setGeometry(QRect(440, 120, 421, 51))
        self.lineEdit_nombre.setObjectName("lineEdit_nombre")
        self.lineEdit_nombre.setValidator(input_validator)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setGeometry(QRect(440, 730, 421, 31))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QLabel(self.widget)
        self.label_2.setGeometry(QRect(350, 130, 81, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QLabel(self.widget)
        self.label_3.setGeometry(QRect(350, 190, 81, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QLabel(self.widget)
        self.label_4.setGeometry(QRect(350, 250, 81, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QLabel(self.widget)
        self.label_5.setGeometry(QRect(360, 310, 71, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QLabel(self.widget)
        self.label_6.setGeometry(QRect(270, 370, 161, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QLabel(self.widget)
        self.label_7.setGeometry(QRect(270, 430, 161, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QLabel(self.widget)
        self.label_8.setGeometry(QRect(310, 70, 391, 20))
        self.label_8.setObjectName("label_8")
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setGeometry(QRect(40, 750, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setGeometry(QRect(180, 750, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_cedula = QLineEdit(self.widget)
        self.lineEdit_cedula.setGeometry(QRect(440, 180, 421, 51))
        self.lineEdit_cedula.setObjectName("lineEdit_cedula")
        self.lineEdit_cedula.setValidator(QIntValidator())
        self.lineEdit_cedula.setMaxLength(10)
        self.lineEdit_edad = QLineEdit(self.widget)
        self.lineEdit_edad.setGeometry(QRect(440, 240, 421, 51))
        self.lineEdit_edad.setObjectName("lineEdit_edad")
        self.lineEdit_edad.setValidator(QIntValidator())
        self.lineEdit_edad.setMaxLength(3)
        self.lineEdit_celular = QLineEdit(self.widget)
        self.lineEdit_celular.setGeometry(QRect(440, 300, 421, 51))
        self.lineEdit_celular.setObjectName("lineEdit_celular")
        self.lineEdit_celular.setValidator(QIntValidator())
        self.lineEdit_celular.setMaxLength(10)
        self.lineEdit_residencia = QLineEdit(self.widget)
        self.lineEdit_residencia.setGeometry(QRect(440, 360, 421, 51))
        self.lineEdit_residencia.setObjectName("lineEdit_residencia")
        self.lineEdit_nacimiento = QLineEdit(self.widget)
        self.lineEdit_nacimiento.setGeometry(QRect(440, 420, 421, 51))
        self.lineEdit_nacimiento.setObjectName("lineEdit_nacimiento")
        self.lineEdit_estudio = QLineEdit(self.widget)
        self.lineEdit_estudio.setGeometry(QRect(440, 480, 421, 51))
        self.lineEdit_estudio.setObjectName("lineEdit_estudio")
        self.lineEdit_dominancia = QLineEdit(self.widget)
        self.lineEdit_dominancia.setGeometry(QRect(440, 540, 421, 51))
        self.lineEdit_dominancia.setObjectName("lineEdit_dominancia")
        self.lineEdit_dominancia.setValidator(input_validator)
        self.lineEdit_tipoalz = QLineEdit(self.widget)
        self.lineEdit_tipoalz.setGeometry(QRect(440, 600, 421, 51))
        self.lineEdit_tipoalz.setObjectName("lineEdit_tipoalz")
        self.lineEdit_fasealz = QLineEdit(self.widget)
        self.lineEdit_fasealz.setGeometry(QRect(440, 660, 421, 51))
        self.lineEdit_fasealz.setObjectName("lineEdit_fasealz")
        self.label_9 = QLabel(self.widget)
        self.label_9.setGeometry(QRect(270, 500, 161, 20))
        self.label_9.setObjectName("label_9")
        self.label_10 = QLabel(self.widget)
        self.label_10.setGeometry(QRect(270, 560, 161, 20))
        self.label_10.setObjectName("label_10")
        self.label_11 = QLabel(self.widget)
        self.label_11.setGeometry(QRect(270, 620, 161, 20))
        self.label_11.setObjectName("label_11")
        self.label_12 = QLabel(self.widget)
        self.label_12.setGeometry(QRect(270, 680, 161, 20))
        self.label_12.setObjectName("label_12")

        self.retranslateUi(Form)
        self.pushButton_3.clicked.connect(Form.close)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Registro Paciente"))
        Form.setWindowIcon(QIcon(r"Recursos_Interfaz\Alzcare.png"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt;\">REGISTRO DEL PACIENTE</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Aceptar"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">Nombre:</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">Cedula:</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">Edad:</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">Celular:</span></p></body></html>"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">Lugar de residencia:</span></p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">Lugar de nacimiento:</span></p></body></html>"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt;\">Complete los siguientes campos en presencia del cuidador</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Form", "Regresar"))
        self.pushButton_3.setText(_translate("Form", "Salir"))
        self.label_9.setText(_translate("Form", "<html><head/><body><p align=\"right\">Estudio:</p></body></html>"))
        self.label_10.setText(_translate("Form", "<html><head/><body><p align=\"right\">Dominancia:</p></body></html>"))
        self.label_11.setText(_translate("Form", "<html><head/><body><p align=\"right\">Tiempo alzheimer:</p></body></html>"))
        self.label_12.setText(_translate("Form", "<html><head/><body><p align=\"right\">Fase alzheimer:</p></body></html>"))

class Formato_Registro_Paciente(QDialog):
    def __init__(self, parent=None):
        super(Formato_Registro_Paciente, self).__init__(parent)
        self.ui = Registro_Paciente()
        self.ui.setupUi(self)

class Seguimiento_Paciente(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1092, 801)
        self.widget = QWidget(Form)
        self.widget.setGeometry(QRect(-50, -20, 1281, 921))
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
        self.label = QLabel(self.widget)
        self.label.setGeometry(QRect(440, 70, 321, 61))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QLabel(self.widget)
        self.label_2.setGeometry(QRect(70, 40, 171, 21))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QLabel(self.widget)
        self.label_3.setGeometry(QRect(550, 180, 101, 21))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.widget_6 = QWidget(self.widget)
        self.widget_6.setGeometry(QRect(120, 370, 271, 311))
        self.widget_6.setStyleSheet("QWidget {\n"
"    background-color: rgb(225, 255, 255);\n"
"}\n"
"\n"
"QLabel{\n"
"    color: rgb(0, 5, 1);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid #0077b6; \n"
"    outline: none;\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"    border-radius: 10px;\n"
"    background-color: rgb(0, 119, 182);\n"
"    color:white;\n"
"}")
        self.widget_6.setObjectName("widget_6")
        self.label_4 = QLabel(self.widget_6)
        self.label_4.setGeometry(QRect(50, 40, 191, 181))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_4 = QPushButton(self.widget_6)
        self.pushButton_4.setGeometry(QRect(30, 270, 221, 28))
        font = QFont()
        font.setFamily("Montserrat")
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.widget_7 = QWidget(self.widget)
        self.widget_7.setGeometry(QRect(430, 370, 281, 311))
        self.widget_7.setStyleSheet("QWidget {\n"
"    background-color: rgb(225, 255, 255);\n"
"}\n"
"\n"
"QLabel{\n"
"    color: rgb(0, 5, 1);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid #0077b6; \n"
"    outline: none;\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"    border-radius: 10px;\n"
"    background-color: rgb(0, 119, 182);\n"
"    color:white;\n"
"}")
        self.widget_7.setObjectName("widget_7")
        self.pushButton_5 = QPushButton(self.widget_7)
        self.pushButton_5.setGeometry(QRect(30, 270, 221, 28))
        font = QFont()
        font.setFamily("Montserrat")
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_5 = QLabel(self.widget_7)
        self.label_5.setGeometry(QRect(10, 40, 321, 181))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.widget_8 = QWidget(self.widget)
        self.widget_8.setGeometry(QRect(740, 370, 311, 311))
        self.widget_8.setStyleSheet("QWidget {\n"
"    background-color: rgb(225, 255, 255);\n"
"}\n"
"\n"
"QLabel{\n"
"    color: rgb(0, 5, 1);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid #0077b6; \n"
"    outline: none;\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"    border-radius: 10px;\n"
"    background-color: rgb(0, 119, 182);\n"
"    color:white;\n"
"}")
        self.widget_8.setObjectName("widget_8")
        self.pushButton_3 = QPushButton(self.widget_8)
        self.pushButton_3.setGeometry(QRect(40, 270, 221, 28))
        font = QFont()
        font.setFamily("Montserrat")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_6 = QLabel(self.widget_8)
        self.label_6.setGeometry(QRect(20, 20, 421, 231))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QLabel(self.widget)
        self.label_7.setGeometry(QRect(190, 250, 141, 111))
        self.label_7.setText("")
        self.label_7.setPixmap(QPixmap(r"Recursos_Interfaz\seguimiento_intprincipal.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QLabel(self.widget)
        self.label_8.setGeometry(QRect(520, 260, 111, 111))
        self.label_8.setText("")
        self.label_8.setPixmap(QPixmap(r"Recursos_Interfaz\estadisticas.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QLabel(self.widget)
        self.label_9.setGeometry(QRect(840, 260, 131, 101))
        self.label_9.setText("")
        self.label_9.setPixmap(QPixmap(r"Recursos_Interfaz\exportar.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setGeometry(QRect(1030, 760, 93, 28))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border: none; /* Quitar el borde */\n"
"    background-color: transparent; /* Fondo transparente */\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.pushButton.setText("")
        icon = QIcon()
        icon.addPixmap(QPixmap(r"Recursos_Interfaz\salir2.png"), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setGeometry(QRect(1010, 50, 101, 41))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    border: none; /* Quitar el borde */\n"
"    background-color: transparent; /* Fondo transparente */\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.pushButton_2.setText("")
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(r"Recursos_Interfaz\regresar.png"), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(30, 30))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.close)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Seguimiento Paciente"))
        Form.setWindowIcon(QIcon(r"Recursos_Interfaz\Alzcare.png"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">SEGUIMIENTO DE PACIENTES</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt;\">Alzcare - company</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Servicios</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt;\">Evalúa el estado diario </span></p><p><span style=\" font-size:9pt;\">del paciente con 10 </span></p><p><span style=\" font-size:9pt;\">preguntas clave </span></p></body></html>"))
        self.pushButton_4.setText(_translate("Form", "Seguimiento"))
        self.pushButton_5.setText(_translate("Form", "Estadísticas"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt;\">Visualiza las estadísticas basadas </span></p><p><span style=\" font-size:9pt;\">en el puntaje obtenido </span></p><p><span style=\" font-size:9pt;\">del seguimiento. </span></p><p><span style=\" font-size:9pt;\">Analiza el progreso y las áreas </span></p><p><span style=\" font-size:9pt;\">que necesitan atención.</span></p></body></html>"))
        self.pushButton_3.setText(_translate("Form", "Exportar perfil"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt;\">Exporta la información completa </span></p><p><span style=\" font-size:9pt;\">del usuario y sus respuestas al </span></p><p><span style=\" font-size:9pt;\">seguimiento, manteniendo un registro </span></p><p><span style=\" font-size:9pt;\">detallado y accesible para revisiones</span></p><p><span style=\" font-size:9pt;\">futuras.</span></p></body></html>"))

class Formato_Seguimiento(QDialog):
    def __init__(self, parent=None):
        super(Formato_Seguimiento, self).__init__(parent)
        self.ui = Seguimiento_Paciente()
        self.ui.setupUi(self)

class Graficos(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(914, 651)
        Form.setStyleSheet("QWidget {\n"
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
"QPushButton {\n"
"    border: none; /* Quitar el borde */\n"
"    background-color: transparent; /* Fondo transparente */\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.label = QLabel(Form)
        self.label.setGeometry(QRect(280, 40, 331, 61))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.widget = QWidget(Form)
        self.widget.setGeometry(QRect(150, 130, 621, 451))
        self.widget.setStyleSheet("QWidget {\n"
"    background-color: rgb(225, 255, 255);\n"
"}\n"
"")
        self.widget.setObjectName("widget")
        self.label_2 = QLabel(self.widget)
        self.label_2.setGeometry(QRect(50, 30, 501, 391))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton = QPushButton(Form)
        self.pushButton.setGeometry(QRect(790, 590, 111, 31))
        self.pushButton.setText("")
        icon = QIcon()
        icon.addPixmap(QPixmap(r"Recursos_Interfaz\salir2.png"), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.close)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Grafico de progreso"))
        Form.setWindowIcon(QIcon(r"Recursos_Interfaz\Alzcare.png"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">GRÁFICOS Y ESTADÍSTICAS</span></p></body></html>"))

class Formato_Graficos(QDialog):
    def __init__(self, parent=None):
        super(Formato_Graficos, self).__init__(parent)
        self.ui = Graficos()
        self.ui.setupUi(self)

class Pregunta_1(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(967, 751)
        self.widget = QWidget(Form)
        self.widget.setGeometry(QRect(-90, -110, 1101, 881))
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
"    color: white;\n"
"    background-color: rgb(0, 119, 182)\n"
"}")
        self.widget.setObjectName("widget")
        self.label_5 = QLabel(self.widget)
        self.label_5.setGeometry(QRect(610, 330, 61, 51))
        self.label_5.setText("")
        self.label_5.setPixmap(QPixmap(r"Recursos_Interfaz\Alzcare.png"))
        self.label_5.setObjectName("label_5")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setGeometry(QRect(10, 110, 1191, 61))
        self.widget_2.setStyleSheet("QWidget{\n"
"    background-color: rgb(144, 224, 239);\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setGeometry(QRect(160, 20, 151, 21))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QLabel(self.widget_2)
        self.label.setGeometry(QRect(100, 10, 41, 41))
        self.label.setText("")
        self.label.setPixmap(QPixmap(r"Recursos_Interfaz\Alzcare.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_regresar = QPushButton(self.widget_2)
        self.pushButton_regresar.setGeometry(QRect(960, 20, 81, 31))
        self.pushButton_regresar.setText("")
        icon = QIcon()
        icon.addPixmap(QPixmap(r"Recursos_Interfaz\regresar.png"), QIcon.Normal, QIcon.Off)
        self.pushButton_regresar.setIcon(icon)
        self.pushButton_regresar.setIconSize(QSize(40, 240))
        self.pushButton_regresar.setObjectName("pushButton_regresar")
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setGeometry(QRect(240, 280, 651, 481))
        self.widget_3.setStyleSheet("QWidget{\n"
"    background-color: rgb(202, 240, 248);\n"
"}\n"
"QLabel{\n"
"    color: rgb(0, 119, 182);}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(0, 119, 182);\n"
"    color: white;\n"
"}")
        self.widget_3.setObjectName("widget_3")
        self.label_3 = QLabel(self.widget_3)
        self.label_3.setGeometry(QRect(10, 0, 351, 41))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_7 = QLabel(self.widget_3)
        self.label_7.setGeometry(QRect(230, 40, 351, 41))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton = QPushButton(self.widget_3)
        self.pushButton.setGeometry(QRect(120, 150, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_B = QPushButton(self.widget_3)
        self.pushButton_B.setGeometry(QRect(120, 210, 93, 28))
        self.pushButton_B.setObjectName("pushButton_B")
        self.pushButton_C = QPushButton(self.widget_3)
        self.pushButton_C.setGeometry(QRect(120, 270, 93, 28))
        self.pushButton_C.setObjectName("pushButton_C")
        self.pushButton_D = QPushButton(self.widget_3)
        self.pushButton_D.setGeometry(QRect(120, 330, 93, 28))
        self.pushButton_D.setObjectName("pushButton_D")
        self.label_A = QLabel(self.widget_3)
        self.label_A.setGeometry(QRect(230, 150, 55, 16))
        self.label_A.setObjectName("label_A")
        self.label_B = QLabel(self.widget_3)
        self.label_B.setGeometry(QRect(230, 210, 55, 16))
        self.label_B.setObjectName("label_B")
        self.label_C = QLabel(self.widget_3)
        self.label_C.setGeometry(QRect(230, 280, 55, 16))
        self.label_C.setObjectName("label_C")
        self.label_D = QLabel(self.widget_3)
        self.label_D.setGeometry(QRect(230, 340, 55, 16))
        self.label_D.setObjectName("label_D")
        self.label_9 = QLabel(self.widget_3)
        self.label_9.setGeometry(QRect(370, 160, 231, 201))
        self.label_9.setText("")
        self.label_9.setPixmap(QPixmap(r"Recursos_Interfaz\calendario_int1.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_6 = QLabel(self.widget)
        self.label_6.setGeometry(QRect(250, 240, 531, 31))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Pregunta 1"))
        Form.setWindowIcon(QIcon(r"Recursos_Interfaz\Alzcare.png"))
        self.label_2.setText(_translate("Form", "Alzcare - company"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p>Pregunta 1.</p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p>¿Qué día es hoy?</p></body></html>"))
        self.pushButton.setText(_translate("Form", "A"))
        self.pushButton_B.setText(_translate("Form", "B"))
        self.pushButton_C.setText(_translate("Form", "C"))
        self.pushButton_D.setText(_translate("Form", "D"))
        self.label_A.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:8pt;\">Respondio correctamente</span></p></body></html>"))
        self.label_A.adjustSize()
        self.label_B.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:8pt;\">Se equivoco en la ciudad</span></p></body></html>"))
        self.label_B.adjustSize()
        self.label_C.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:8pt;\">Se equivoco en el mes</span></p></body></html>"))
        self.label_C.adjustSize()
        self.label_D.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:8pt;\">Se equivoco en el año</span></p></body></html>"))
        self.label_D.adjustSize()
        self.label_6.setText(_translate("Form", "El cuidador deberá estar presente para realizar las siguientes preguntas:"))

class Formato_Pregunta_1(QDialog):
    def __init__(self, parent=None):
        super(Formato_Pregunta_1, self).__init__(parent)
        self.ui = Pregunta_1()
        self.ui.setupUi(self)

class Pregunta_2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(967, 751)
        self.widget = QWidget(Form)
        self.widget.setGeometry(QRect(-90, -110, 1101, 881))
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
"    color: white;\n"
"    background-color: rgb(0, 119, 182)\n"
"}")
        self.widget.setObjectName("widget")
        self.label_5 = QLabel(self.widget)
        self.label_5.setGeometry(QRect(610, 330, 61, 51))
        self.label_5.setText("")
        self.label_5.setPixmap(QPixmap(r"Recursos_Interfaz\Alzcare.png"))
        self.label_5.setObjectName("label_5")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setGeometry(QRect(10, 110, 1191, 61))
        self.widget_2.setStyleSheet("QWidget{\n"
"    background-color: rgb(144, 224, 239);\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setGeometry(QRect(160, 20, 151, 21))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QLabel(self.widget_2)
        self.label.setGeometry(QRect(100, 10, 41, 41))
        self.label.setText("")
        self.label.setPixmap(QPixmap(r"Recursos_Interfaz\Alzcare.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_regresar = QPushButton(self.widget_2)
        self.pushButton_regresar.setGeometry(QRect(960, 20, 81, 31))
        self.pushButton_regresar.setText("")
        icon = QIcon()
        icon.addPixmap(QPixmap(r"Recursos_Interfaz\regresar.png"), QIcon.Normal, QIcon.Off)
        self.pushButton_regresar.setIcon(icon)
        self.pushButton_regresar.setIconSize(QSize(40, 240))
        self.pushButton_regresar.setObjectName("pushButton_regresar")
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setGeometry(QRect(240, 280, 651, 481))
        self.widget_3.setStyleSheet("QWidget{\n"
"    background-color: rgb(202, 240, 248);\n"
"}\n"
"QLabel{\n"
"    color: rgb(0, 119, 182);}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(0, 119, 182);\n"
"    color: white;\n"
"}")
        self.widget_3.setObjectName("widget_3")
        self.label_3 = QLabel(self.widget_3)
        self.label_3.setGeometry(QRect(10, 0, 351, 41))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_7 = QLabel(self.widget_3)
        self.label_7.setGeometry(QRect(230, 40, 351, 41))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton = QPushButton(self.widget_3)
        self.pushButton.setGeometry(QRect(120, 150, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_C = QPushButton(self.widget_3)
        self.pushButton_C.setGeometry(QRect(120, 270, 93, 28))
        self.pushButton_C.setObjectName("pushButton_C")
        self.label_A = QLabel(self.widget_3)
        self.label_A.setGeometry(QRect(230, 150, 55, 16))
        self.label_A.setFont(font)
        self.label_A.setObjectName("label_A")
        self.label_C = QLabel(self.widget_3)
        self.label_C.setGeometry(QRect(230, 280, 55, 16))
        self.label_C.setFont(font)
        self.label_C.setObjectName("label_C")
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setGeometry(QRect(380, 180, 201, 141))
        self.label_4.setText("")
        self.label_4.setPixmap(QPixmap(r"Recursos_Interfaz\nombre_int2.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_6 = QLabel(self.widget)
        self.label_6.setGeometry(QRect(250, 240, 531, 31))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Pregunta 2"))
        Form.setWindowIcon(QIcon(r"Recursos_Interfaz\Alzcare.png"))
        self.label_2.setText(_translate("Form", "Alzcare - company"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p>Pregunta 2.</p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p>¿Cuál es su nombre?</p></body></html>"))
        self.pushButton.setText(_translate("Form", "A"))
        self.pushButton_C.setText(_translate("Form", "C"))
        self.label_A.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:8pt;\">Respondio correctamente</span></p></body></html>"))
        self.label_A.adjustSize()
        self.label_C.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:8pt;\">Respondio incorrectamente</span></p></body></html>"))
        self.label_C.adjustSize()
        self.label_6.setText(_translate("Form", "El cuidador deberá estar presente para realizar las siguientes preguntas:"))

class Formato_Pregunta_2(QDialog):
    def __init__(self, parent=None):
        super(Formato_Pregunta_2, self).__init__(parent)
        self.ui = Pregunta_2()
        self.ui.setupUi(self)

class Pregunta_3(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(967, 751)
        self.widget = QWidget(Form)
        self.widget.setGeometry(QRect(-90, -110, 1101, 881))
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
"    color: white;\n"
"    background-color: rgb(0, 119, 182)\n"
"}")
        self.widget.setObjectName("widget")
        self.label_5 = QLabel(self.widget)
        self.label_5.setGeometry(QRect(610, 330, 61, 51))
        self.label_5.setText("")
        self.label_5.setPixmap(QPixmap(r"Recursos_Interfaz\Alzcare.png"))
        self.label_5.setObjectName("label_5")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setGeometry(QRect(10, 110, 1191, 61))
        self.widget_2.setStyleSheet("QWidget{\n"
"    background-color: rgb(144, 224, 239);\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setGeometry(QRect(160, 20, 151, 21))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QLabel(self.widget_2)
        self.label.setGeometry(QRect(100, 10, 41, 41))
        self.label.setText("")
        self.label.setPixmap(QPixmap(r"Recursos_Interfaz\Alzcare.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_regresar = QPushButton(self.widget_2)
        self.pushButton_regresar.setGeometry(QRect(960, 20, 81, 31))
        self.pushButton_regresar.setText("")
        icon = QIcon()
        icon.addPixmap(QPixmap(r"Recursos_Interfaz\regresar.png"), QIcon.Normal, QIcon.Off)
        self.pushButton_regresar.setIcon(icon)
        self.pushButton_regresar.setIconSize(QSize(40, 240))
        self.pushButton_regresar.setObjectName("pushButton_regresar")
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setGeometry(QRect(240, 280, 651, 481))
        self.widget_3.setStyleSheet("QWidget{\n"
"    background-color: rgb(202, 240, 248);\n"
"}\n"
"QLabel{\n"
"    color: rgb(0, 119, 182);}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(0, 119, 182);\n"
"    color: white;\n"
"}")
        self.widget_3.setObjectName("widget_3")
        self.label_3 = QLabel(self.widget_3)
        self.label_3.setGeometry(QRect(10, 0, 351, 41))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_7 = QLabel(self.widget_3)
        self.label_7.setGeometry(QRect(230, 40, 351, 41))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton = QPushButton(self.widget_3)
        self.pushButton.setGeometry(QRect(120, 150, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_C = QPushButton(self.widget_3)
        self.pushButton_C.setGeometry(QRect(120, 270, 93, 28))
        self.pushButton_C.setObjectName("pushButton_C")
        self.label_A = QLabel(self.widget_3)
        self.label_A.setGeometry(QRect(230, 150, 55, 16))
        self.label_A.setFont(font)
        self.label_A.setObjectName("label_A")
        self.label_C = QLabel(self.widget_3)
        self.label_C.setGeometry(QRect(230, 280, 55, 16))
        self.label_C.setFont(font)
        self.label_C.setObjectName("label_C")
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setGeometry(QRect(390, 190, 151, 141))
        self.label_4.setText("")
        self.label_4.setPixmap(QPixmap(r"Recursos_Interfaz\edad_int3.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_6 = QLabel(self.widget)
        self.label_6.setGeometry(QRect(250, 240, 531, 31))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Pregunta 3"))
        Form.setWindowIcon(QIcon(r"Recursos_Interfaz\Alzcare.png"))
        self.label_2.setText(_translate("Form", "Alzcare - company"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p>Pregunta 3.</p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p>¿Qué edad tiene?</p></body></html>"))
        self.pushButton.setText(_translate("Form", "A"))
        self.pushButton_C.setText(_translate("Form", "C"))
        self.label_A.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:8pt;\">Respondio correctamente</span></p></body></html>"))
        self.label_A.adjustSize()
        self.label_C.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:8pt;\">Respondio incorrectamente</span></p></body></html>"))
        self.label_C.adjustSize()
        self.label_6.setText(_translate("Form", "El cuidador deberá estar presente para realizar las siguientes preguntas:"))

class Formato_Pregunta_3(QDialog):
    def __init__(self, parent=None):
        super(Formato_Pregunta_3, self).__init__(parent)
        self.ui = Pregunta_3()
        self.ui.setupUi(self)

class Pregunta_4(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(967, 751)
        self.widget = QWidget(Form)
        self.widget.setGeometry(QRect(-90, -110, 1101, 881))
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
"    color: white;\n"
"    background-color: rgb(0, 119, 182)\n"
"}")
        self.widget.setObjectName("widget")
        self.label_5 = QLabel(self.widget)
        self.label_5.setGeometry(QRect(610, 330, 61, 51))
        self.label_5.setText("")
        self.label_5.setPixmap(QPixmap(r"Recursos_Interfaz\Alzcare.png"))
        self.label_5.setObjectName("label_5")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setGeometry(QRect(10, 110, 1191, 61))
        self.widget_2.setStyleSheet("QWidget{\n"
"    background-color: rgb(144, 224, 239);\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setGeometry(QRect(160, 20, 151, 21))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QLabel(self.widget_2)
        self.label.setGeometry(QRect(100, 10, 41, 41))
        self.label.setText("")
        self.label.setPixmap(QPixmap(r"Recursos_Interfaz\Alzcare.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_regresar = QPushButton(self.widget_2)
        self.pushButton_regresar.setGeometry(QRect(960, 20, 81, 31))
        self.pushButton_regresar.setText("")
        icon = QIcon()
        icon.addPixmap(QPixmap(r"Recursos_Interfaz\regresar.png"), QIcon.Normal, QIcon.Off)
        self.pushButton_regresar.setIcon(icon)
        self.pushButton_regresar.setIconSize(QSize(40, 240))
        self.pushButton_regresar.setObjectName("pushButton_regresar")
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setGeometry(QRect(240, 280, 651, 481))
        self.widget_3.setStyleSheet("QWidget{\n"
"    background-color: rgb(202, 240, 248);\n"
"}\n"
"QLabel{\n"
"    color: rgb(0, 119, 182);}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(0, 119, 182);\n"
"    color: white;\n"
"}")
        self.widget_3.setObjectName("widget_3")
        self.label_3 = QLabel(self.widget_3)
        self.label_3.setGeometry(QRect(10, 0, 351, 41))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_7 = QLabel(self.widget_3)
        self.label_7.setGeometry(QRect(200, 50, 351, 41))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton = QPushButton(self.widget_3)
        self.pushButton.setGeometry(QRect(120, 150, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_C = QPushButton(self.widget_3)
        self.pushButton_C.setGeometry(QRect(120, 270, 93, 28))
        self.pushButton_C.setObjectName("pushButton_C")
        self.label_A = QLabel(self.widget_3)
        self.label_A.setGeometry(QRect(230, 150, 55, 16))
        self.label_A.setFont(font)
        self.label_A.setObjectName("label_A")
        self.label_C = QLabel(self.widget_3)
        self.label_C.setGeometry(QRect(230, 280, 55, 16))
        self.label_C.setFont(font)
        self.label_C.setObjectName("label_C")
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setGeometry(QRect(380, 180, 161, 151))
        self.label_4.setText("")
        self.label_4.setPixmap(QPixmap(r"Recursos_Interfaz\memoria_int4.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_6 = QLabel(self.widget)
        self.label_6.setGeometry(QRect(250, 240, 531, 31))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Preunta 4"))
        Form.setWindowIcon(QIcon(r"Recursos_Interfaz\Alzcare.png"))
        self.label_2.setText(_translate("Form", "Alzcare - company"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p>Pregunta 4.</p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p>¿Tienes problemas de memoria?</p></body></html>"))
        self.pushButton.setText(_translate("Form", "A"))
        self.pushButton_C.setText(_translate("Form", "C"))
        self.label_A.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:8pt;\">Reconoce su situacion</span></p></body></html>"))
        self.label_A.adjustSize()
        self.label_C.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:8pt;\">No reconoce su situacion</span></p></body></html>"))
        self.label_C.adjustSize()
        self.label_6.setText(_translate("Form", "El cuidador deberá estar presente para realizar las siguientes preguntas:"))

class Formato_Pregunta_4(QDialog):
    def __init__(self, parent=None):
        super(Formato_Pregunta_4, self).__init__(parent)
        self.ui = Pregunta_4()
        self.ui.setupUi(self)

class Pregunta_5(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(967, 751)
        self.widget = QWidget(Form)
        self.widget.setGeometry(QRect(-90, -110, 1101, 881))
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
"    color: white;\n"
"    background-color: rgb(0, 119, 182)\n"
"}")
        self.widget.setObjectName("widget")
        self.label_5 = QLabel(self.widget)
        self.label_5.setGeometry(QRect(610, 330, 61, 51))
        self.label_5.setText("")
        self.label_5.setPixmap(QPixmap(r"Recursos_Interfaz\Alzcare.png"))
        self.label_5.setObjectName("label_5")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setGeometry(QRect(10, 110, 1191, 61))
        self.widget_2.setStyleSheet("QWidget{\n"
"    background-color: rgb(144, 224, 239);\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setGeometry(QRect(160, 20, 151, 21))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QLabel(self.widget_2)
        self.label.setGeometry(QRect(100, 10, 41, 41))
        self.label.setText("")
        self.label.setPixmap(QPixmap(r"Recursos_Interfaz\Alzcare.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_regresar = QPushButton(self.widget_2)
        self.pushButton_regresar.setGeometry(QRect(960, 20, 81, 31))
        self.pushButton_regresar.setText("")
        icon = QIcon()
        icon.addPixmap(QPixmap(r"Recursos_Interfaz\regresar.png"), QIcon.Normal, QIcon.Off)
        self.pushButton_regresar.setIcon(icon)
        self.pushButton_regresar.setIconSize(QSize(40, 240))
        self.pushButton_regresar.setObjectName("pushButton_regresar")
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setGeometry(QRect(240, 280, 651, 481))
        self.widget_3.setStyleSheet("QWidget{\n"
"    background-color: rgb(202, 240, 248);\n"
"}\n"
"QLabel{\n"
"    color: rgb(0, 119, 182);}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(0, 119, 182);\n"
"    color: white;\n"
"}")
        self.widget_3.setObjectName("widget_3")
        self.label_3 = QLabel(self.widget_3)
        self.label_3.setGeometry(QRect(10, 0, 351, 41))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_7 = QLabel(self.widget_3)
        self.label_7.setGeometry(QRect(230, 40, 351, 41))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton = QPushButton(self.widget_3)
        self.pushButton.setGeometry(QRect(120, 150, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_C = QPushButton(self.widget_3)
        self.pushButton_C.setGeometry(QRect(120, 270, 93, 28))
        self.pushButton_C.setObjectName("pushButton_C")
        self.label_A = QLabel(self.widget_3)
        self.label_A.setGeometry(QRect(230, 150, 55, 16))
        self.label_A.setFont(font)
        self.label_A.setObjectName("label_A")
        self.label_C = QLabel(self.widget_3)
        self.label_C.setGeometry(QRect(230, 280, 55, 16))
        self.label_C.setFont(font)
        self.label_C.setObjectName("label_C")
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setGeometry(QRect(390, 170, 151, 151))
        self.label_4.setText("")
        self.label_4.setPixmap(QPixmap(r"Recursos_Interfaz\cuidador_int5.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_6 = QLabel(self.widget)
        self.label_6.setGeometry(QRect(250, 240, 531, 31))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Pregunta 5"))
        Form.setWindowIcon(QIcon(r"Recursos_Interfaz\Alzcare.png"))
        self.label_2.setText(_translate("Form", "Alzcare - company"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p>Pregunta 5.</p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p>Sabes cómo se llama tu cuidador?</p></body></html>"))
        self.pushButton.setText(_translate("Form", "A"))
        self.pushButton_C.setText(_translate("Form", "C"))
        self.label_A.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:8pt;\">Respondio correctamente</span></p></body></html>"))
        self.label_A.adjustSize()
        self.label_C.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:8pt;\">Respondio incorrectamente</span></p></body></html>"))
        self.label_C.adjustSize()
        self.label_6.setText(_translate("Form", "El cuidador deberá estar presente para realizar las siguientes preguntas:"))

class Formato_Pregunta_5(QDialog):
    def __init__(self, parent=None):
        super(Formato_Pregunta_5, self).__init__(parent)
        self.ui = Pregunta_5()
        self.ui.setupUi(self)

class Pregunta_6(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(967, 751)
        self.widget = QWidget(Form)
        self.widget.setGeometry(QRect(-90, -110, 1101, 881))
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
"    color: white;\n"
"    background-color: rgb(0, 119, 182)\n"
"}")
        self.widget.setObjectName("widget")
        self.label_5 = QLabel(self.widget)
        self.label_5.setGeometry(QRect(610, 330, 61, 51))
        self.label_5.setText("")
        self.label_5.setPixmap(QPixmap(r"Recursos_Interfaz\Alzcare.png"))
        self.label_5.setObjectName("label_5")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setGeometry(QRect(10, 110, 1191, 61))
        self.widget_2.setStyleSheet("QWidget{\n"
"    background-color: rgb(144, 224, 239);\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setGeometry(QRect(160, 20, 151, 21))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QLabel(self.widget_2)
        self.label.setGeometry(QRect(100, 10, 41, 41))
        self.label.setText("")
        self.label.setPixmap(QPixmap(r"Recursos_Interfaz\Alzcare.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_regresar = QPushButton(self.widget_2)
        self.pushButton_regresar.setGeometry(QRect(960, 20, 81, 31))
        self.pushButton_regresar.setText("")
        icon = QIcon()
        icon.addPixmap(QPixmap(r"Recursos_Interfaz\regresar.png"), QIcon.Normal, QIcon.Off)
        self.pushButton_regresar.setIcon(icon)
        self.pushButton_regresar.setIconSize(QSize(40, 240))
        self.pushButton_regresar.setObjectName("pushButton_regresar")
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setGeometry(QRect(240, 280, 651, 481))
        self.widget_3.setStyleSheet("QWidget{\n"
"    background-color: rgb(202, 240, 248);\n"
"}\n"
"QLabel{\n"
"    color: rgb(0, 119, 182);}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(0, 119, 182);\n"
"    color: white;\n"
"}")
        self.widget_3.setObjectName("widget_3")
        self.label_3 = QLabel(self.widget_3)
        self.label_3.setGeometry(QRect(10, 0, 351, 41))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_7 = QLabel(self.widget_3)
        self.label_7.setGeometry(QRect(150, 50, 351, 41))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton = QPushButton(self.widget_3)
        self.pushButton.setGeometry(QRect(120, 150, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_B = QPushButton(self.widget_3)
        self.pushButton_B.setGeometry(QRect(120, 210, 93, 28))
        self.pushButton_B.setObjectName("pushButton_B")
        self.pushButton_C = QPushButton(self.widget_3)
        self.pushButton_C.setGeometry(QRect(120, 270, 93, 28))
        self.pushButton_C.setObjectName("pushButton_C")
        self.label_A = QLabel(self.widget_3)
        self.label_A.setGeometry(QRect(230, 150, 55, 16))
        self.label_A.setFont(font)
        self.label_A.setObjectName("label_A")
        self.label_B = QLabel(self.widget_3)
        self.label_B.setGeometry(QRect(230, 210, 55, 16))
        self.label_B.setFont(font)
        self.label_B.setObjectName("label_B")
        self.label_C = QLabel(self.widget_3)
        self.label_C.setGeometry(QRect(230, 280, 55, 16))
        self.label_C.setFont(font)
        self.label_C.setObjectName("label_C")
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setGeometry(QRect(390, 180, 141, 151))
        self.label_4.setText("")
        self.label_4.setPixmap(QPixmap(r"Recursos_Interfaz\vestir_int6.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_6 = QLabel(self.widget)
        self.label_6.setGeometry(QRect(250, 240, 531, 31))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Pregunta 6"))
        Form.setWindowIcon(QIcon(r"Recursos_Interfaz\Alzcare.png"))
        self.label_2.setText(_translate("Form", "Alzcare - company"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p>Pregunta 6.</p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p>¿El paciente necesita ayuda para vestirse?</p></body></html>"))
        self.pushButton.setText(_translate("Form", "A"))
        self.pushButton_B.setText(_translate("Form", "B"))
        self.pushButton_C.setText(_translate("Form", "C"))
        self.label_A.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:8pt;\">No necesita ayuda</span></p></body></html>"))
        self.label_A.adjustSize()
        self.label_B.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:8pt;\">Necesita ayuda para los cordones</span></p></body></html>"))
        self.label_B.adjustSize()
        self.label_C.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:8pt;\">Necesita ayuda para todo</span></p></body></html>"))
        self.label_C.adjustSize()
        self.label_6.setText(_translate("Form", "El cuidador deberá estar presente para realizar las siguientes preguntas:"))

class Formato_Pregunta_6(QDialog):
    def __init__(self, parent=None):
        super(Formato_Pregunta_6, self).__init__(parent)
        self.ui = Pregunta_6()
        self.ui.setupUi(self)

class Pregunta_7(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(967, 751)
        self.widget = QWidget(Form)
        self.widget.setGeometry(QRect(-90, -110, 1101, 881))
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
"    color: white;\n"
"    background-color: rgb(0, 119, 182)\n"
"}")
        self.widget.setObjectName("widget")
        self.label_5 = QLabel(self.widget)
        self.label_5.setGeometry(QRect(610, 330, 61, 51))
        self.label_5.setText("")
        self.label_5.setPixmap(QPixmap(r"Recursos_Interfaz\Alzcare.png"))
        self.label_5.setObjectName("label_5")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setGeometry(QRect(10, 110, 1191, 61))
        self.widget_2.setStyleSheet("QWidget{\n"
"    background-color: rgb(144, 224, 239);\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setGeometry(QRect(160, 20, 151, 21))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QLabel(self.widget_2)
        self.label.setGeometry(QRect(100, 10, 41, 41))
        self.label.setText("")
        self.label.setPixmap(QPixmap(r"Recursos_Interfaz\Alzcare.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_regresar = QPushButton(self.widget_2)
        self.pushButton_regresar.setGeometry(QRect(960, 20, 81, 31))
        self.pushButton_regresar.setText("")
        icon = QIcon()
        icon.addPixmap(QPixmap(r"Recursos_Interfaz\regresar.png"), QIcon.Normal, QIcon.Off)
        self.pushButton_regresar.setIcon(icon)
        self.pushButton_regresar.setIconSize(QSize(40, 240))
        self.pushButton_regresar.setObjectName("pushButton_regresar")
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setGeometry(QRect(240, 280, 651, 481))
        self.widget_3.setStyleSheet("QWidget{\n"
"    background-color: rgb(202, 240, 248);\n"
"}\n"
"QLabel{\n"
"    color: rgb(0, 119, 182);}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(0, 119, 182);\n"
"    color: white;\n"
"}")
        self.widget_3.setObjectName("widget_3")
        self.label_3 = QLabel(self.widget_3)
        self.label_3.setGeometry(QRect(10, 0, 351, 41))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_7 = QLabel(self.widget_3)
        self.label_7.setGeometry(QRect(60, 40, 571, 61))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton = QPushButton(self.widget_3)
        self.pushButton.setGeometry(QRect(50, 150, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_B = QPushButton(self.widget_3)
        self.pushButton_B.setGeometry(QRect(50, 210, 93, 28))
        self.pushButton_B.setObjectName("pushButton_B")
        self.pushButton_C = QPushButton(self.widget_3)
        self.pushButton_C.setGeometry(QRect(50, 260, 93, 28))
        self.pushButton_C.setObjectName("pushButton_C")
        self.label_A = QLabel(self.widget_3)
        self.label_A.setGeometry(QRect(150, 160, 251, 16))
        self.label_A.setObjectName("label_A")
        self.label_B = QLabel(self.widget_3)
        self.label_B.setGeometry(QRect(150, 210, 301, 20))
        self.label_B.setObjectName("label_B")
        self.label_C = QLabel(self.widget_3)
        self.label_C.setGeometry(QRect(150, 270, 271, 16))
        self.label_C.setObjectName("label_C")
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setGeometry(QRect(270, 330, 151, 131))
        self.label_4.setText("")
        self.label_4.setPixmap(QPixmap(r"Recursos_Interfaz\foto_int7.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_6 = QLabel(self.widget)
        self.label_6.setGeometry(QRect(250, 240, 531, 31))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Pregunta 7"))
        Form.setWindowIcon(QIcon(r"Recursos_Interfaz\Alzcare.png"))
        self.label_2.setText(_translate("Form", "Alzcare - company"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p>Pregunta 7.</p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p>El cuidador deberá mostrar al paciente una fotografía de </p><p>un familiar cercano al paciente</p></body></html>"))
        self.pushButton.setText(_translate("Form", "A"))
        self.pushButton_B.setText(_translate("Form", "B"))
        self.pushButton_C.setText(_translate("Form", "C"))
        self.label_A.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:8pt;\">El paciente reconoce e identifica al familiar</span></p></body></html>"))
        self.label_A.adjustSize()
        self.label_B.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:8pt;\">El paciente reconoce el nombre, pero no al familiar</span></p></body></html>"))
        self.label_B.adjustSize()
        self.label_C.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:8pt;\">El paciente no reconoce ni identifica al familiar</span></p></body></html>"))
        self.label_C.adjustSize()
        self.label_6.setText(_translate("Form", "El cuidador deberá estar presente para realizar las siguientes preguntas:"))

class Formato_Pregunta_7(QDialog):
    def __init__(self, parent=None):
        super(Formato_Pregunta_7, self).__init__(parent)
        self.ui = Pregunta_7()
        self.ui.setupUi(self)

class Pregunta_8(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(967, 751)
        self.widget = QWidget(Form)
        self.widget.setGeometry(QRect(-90, -110, 1101, 881))
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
"    color: white;\n"
"    background-color: rgb(0, 119, 182)\n"
"}")
        self.widget.setObjectName("widget")
        self.label_5 = QLabel(self.widget)
        self.label_5.setGeometry(QRect(610, 330, 61, 51))
        self.label_5.setText("")
        self.label_5.setPixmap(QPixmap(r"Recursos_Interfaz\Alzcare.png"))
        self.label_5.setObjectName("label_5")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setGeometry(QRect(10, 110, 1191, 61))
        self.widget_2.setStyleSheet("QWidget{\n"
"    background-color: rgb(144, 224, 239);\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setGeometry(QRect(160, 20, 151, 21))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QLabel(self.widget_2)
        self.label.setGeometry(QRect(100, 10, 41, 41))
        self.label.setText("")
        self.label.setPixmap(QPixmap(r"Recursos_Interfaz\Alzcare.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_regresar = QPushButton(self.widget_2)
        self.pushButton_regresar.setGeometry(QRect(960, 20, 81, 31))
        self.pushButton_regresar.setText("")
        icon = QIcon()
        icon.addPixmap(QPixmap(r"Recursos_Interfaz\regresar.png"), QIcon.Normal, QIcon.Off)
        self.pushButton_regresar.setIcon(icon)
        self.pushButton_regresar.setIconSize(QSize(40, 240))
        self.pushButton_regresar.setObjectName("pushButton_regresar")
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setGeometry(QRect(240, 280, 651, 481))
        self.widget_3.setStyleSheet("QWidget{\n"
"    background-color: rgb(202, 240, 248);\n"
"}\n"
"QLabel{\n"
"    color: rgb(0, 119, 182);}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(0, 119, 182);\n"
"    color: white;\n"
"}")
        self.widget_3.setObjectName("widget_3")
        self.label_3 = QLabel(self.widget_3)
        self.label_3.setGeometry(QRect(10, 0, 351, 41))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_7 = QLabel(self.widget_3)
        self.label_7.setGeometry(QRect(150, 50, 371, 41))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton = QPushButton(self.widget_3)
        self.pushButton.setGeometry(QRect(120, 150, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_B = QPushButton(self.widget_3)
        self.pushButton_B.setGeometry(QRect(120, 210, 93, 28))
        self.pushButton_B.setObjectName("pushButton_B")
        self.pushButton_C = QPushButton(self.widget_3)
        self.pushButton_C.setGeometry(QRect(120, 270, 93, 28))
        self.pushButton_C.setObjectName("pushButton_C")
        self.label_A = QLabel(self.widget_3)
        self.label_A.setGeometry(QRect(220, 150, 111, 16))
        self.label_A.setObjectName("label_A")
        self.label_B = QLabel(self.widget_3)
        self.label_B.setGeometry(QRect(220, 210, 211, 16))
        self.label_B.setObjectName("label_B")
        self.label_C = QLabel(self.widget_3)
        self.label_C.setGeometry(QRect(220, 270, 181, 16))
        self.label_C.setObjectName("label_C")
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setGeometry(QRect(240, 310, 161, 161))
        self.label_4.setText("")
        self.label_4.setPixmap(QPixmap(r"Recursos_Interfaz\aseo_int8.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_6 = QLabel(self.widget)
        self.label_6.setGeometry(QRect(250, 240, 531, 31))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Pregunta 8"))
        Form.setWindowIcon(QIcon(r"Recursos_Interfaz\Alzcare.png"))
        self.label_2.setText(_translate("Form", "Alzcare - company"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p>Pregunta 8.</p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p>¿El paciente necesita ayuda para asearse?</p></body></html>"))
        self.pushButton.setText(_translate("Form", "A"))
        self.pushButton_B.setText(_translate("Form", "B"))
        self.pushButton_C.setText(_translate("Form", "C"))
        self.label_A.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:8pt;\">No necesita ayuda</span></p></body></html>"))
        self.label_B.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:8pt;\">Necesita ayuda para una extremidad</span></p></body></html>"))
        self.label_C.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:8pt;\">Necesita ayuda para dos o más</span></p></body></html>"))
        self.label_6.setText(_translate("Form", "El cuidador deberá estar presente para realizar las siguientes preguntas:"))

class Formato_Pregunta_8(QDialog):
    def __init__(self, parent=None):
        super(Formato_Pregunta_8, self).__init__(parent)
        self.ui = Pregunta_8()
        self.ui.setupUi(self)

class Pregunta_9(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(967, 751)
        self.widget = QWidget(Form)
        self.widget.setGeometry(QRect(-90, -110, 1101, 881))
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
"    color: white;\n"
"    background-color: rgb(0, 119, 182)\n"
"}")
        self.widget.setObjectName("widget")
        self.label_5 = QLabel(self.widget)
        self.label_5.setGeometry(QRect(610, 330, 61, 51))
        self.label_5.setText("")
        self.label_5.setPixmap(QPixmap(r"Recursos_Interfaz\Alzcare.png"))
        self.label_5.setObjectName("label_5")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setGeometry(QRect(10, 110, 1191, 61))
        self.widget_2.setStyleSheet("QWidget{\n"
"    background-color: rgb(144, 224, 239);\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setGeometry(QRect(160, 20, 151, 21))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QLabel(self.widget_2)
        self.label.setGeometry(QRect(100, 10, 41, 41))
        self.label.setText("")
        self.label.setPixmap(QPixmap(r"Recursos_Interfaz\Alzcare.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_regresar = QPushButton(self.widget_2)
        self.pushButton_regresar.setGeometry(QRect(960, 20, 81, 31))
        self.pushButton_regresar.setText("")
        icon = QIcon()
        icon.addPixmap(QPixmap(r"Recursos_Interfaz\regresar.png"), QIcon.Normal, QIcon.Off)
        self.pushButton_regresar.setIcon(icon)
        self.pushButton_regresar.setIconSize(QSize(40, 240))
        self.pushButton_regresar.setObjectName("pushButton_regresar")
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setGeometry(QRect(240, 280, 651, 481))
        self.widget_3.setStyleSheet("QWidget{\n"
"    background-color: rgb(202, 240, 248);\n"
"}\n"
"QLabel{\n"
"    color: rgb(0, 119, 182);}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(0, 119, 182);\n"
"    color: white;\n"
"}")
        self.widget_3.setObjectName("widget_3")
        self.label_3 = QLabel(self.widget_3)
        self.label_3.setGeometry(QRect(10, 0, 351, 41))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_7 = QLabel(self.widget_3)
        self.label_7.setGeometry(QRect(50, 40, 551, 41))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton_A = QPushButton(self.widget_3)
        self.pushButton_A.setGeometry(QRect(120, 150, 93, 28))
        font = QFont()
        font.setFamily("Montserrat")
        self.pushButton_A.setFont(font)
        self.pushButton_A.setObjectName("pushButton_A")
        self.pushButton_B = QPushButton(self.widget_3)
        self.pushButton_B.setGeometry(QRect(120, 190, 93, 28))  
        font = QFont()
        font.setFamily("Montserrat")
        self.pushButton_B.setFont(font)
        self.pushButton_B.setObjectName("pushButton_B")
        self.pushButton_C = QPushButton(self.widget_3)
        self.pushButton_C.setGeometry(QRect(120, 230, 93, 28))
        self.pushButton_C.setFont(font)
        self.pushButton_C.setFont(font)
        self.pushButton_C.setObjectName("pushButton_C")
        self.label_A = QLabel(self.widget_3)
        self.label_A.setGeometry(QRect(220, 150, 231, 21))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        self.label_A.setFont(font)
        self.label_A.setObjectName("label_A")
        self.label_B = QLabel(self.widget_3)
        self.label_B.setGeometry(QRect(220, 190, 221, 21))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        self.label_B.setFont(font)
        self.label_B.setObjectName("label_B")
        self.label_C = QLabel(self.widget_3)
        self.label_C.setGeometry(QRect(220, 230, 181, 16))
        self.label_C.setFont(font)
        self.label_C.setObjectName("label_C")
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setGeometry(QRect(230, 320, 191, 121))
        self.label_4.setText("")
        self.label_4.setPixmap(QPixmap(r"Recursos_Interfaz\cama_int9.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_6 = QLabel(self.widget)
        self.label_6.setGeometry(QRect(250, 240, 531, 31))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Pregunta 9"))
        Form.setWindowIcon(QIcon(r"Recursos_Interfaz\Alzcare.png"))
        self.label_2.setText(_translate("Form", "Alzcare - company"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p>Pregunta 9.</p><p><br/></p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p>¿El paciente necesita ayuda a la hora de levantarse de la cama?</p></body></html>"))
        self.pushButton_A.setText(_translate("Form", "A"))
        self.pushButton_B.setText(_translate("Form", "B"))
        self.pushButton_C.setText(_translate("Form", "C"))
        self.label_A.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:8pt;\">Se sienta y se levanta sin ayuda</span></p></body></html>"))
        self.label_B.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:8pt;\">Se sienta y se levanta con ayuda</span></p></body></html>"))
        self.label_C.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:8pt;\">No se levanta de la cama</span></p></body></html>"))
        self.label_6.setText(_translate("Form", "El cuidador deberá estar presente para realizar las siguientes preguntas:"))

class Formato_Pregunta_9(QDialog):
    def __init__(self, parent=None):
        super(Formato_Pregunta_9, self).__init__(parent)
        self.ui = Pregunta_9()
        self.ui.setupUi(self)

class Pregunta_10(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(967, 734)
        self.widget = QWidget(Form)
        self.widget.setGeometry(QRect(-90, -110, 1101, 881))
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
"    color: white;\n"
"    background-color: rgb(0, 119, 182)\n"
"}")
        self.widget.setObjectName("widget")
        self.label_5 = QLabel(self.widget)
        self.label_5.setGeometry(QRect(610, 330, 61, 51))
        self.label_5.setText("")
        self.label_5.setPixmap(QPixmap(r"Recursos_Interfaz\Alzcare.png"))
        self.label_5.setObjectName("label_5")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setGeometry(QRect(10, 110, 1191, 61))
        self.widget_2.setStyleSheet("QWidget{\n"
"    background-color: rgb(144, 224, 239);\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setGeometry(QRect(160, 20, 151, 21))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QLabel(self.widget_2)
        self.label.setGeometry(QRect(100, 10, 41, 41))
        self.label.setText("")
        self.label.setPixmap(QPixmap(r"Recursos_Interfaz\Alzcare.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_regresar = QPushButton(self.widget_2)
        self.pushButton_regresar.setGeometry(QRect(960, 20, 81, 31))
        self.pushButton_regresar.setText("")
        icon = QIcon()
        icon.addPixmap(QPixmap(r"Recursos_Interfaz\regresar.png"), QIcon.Normal, QIcon.Off)
        self.pushButton_regresar.setIcon(icon)
        self.pushButton_regresar.setIconSize(QSize(40, 240))
        self.pushButton_regresar.setObjectName("pushButton_regresar")
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setGeometry(QRect(240, 280, 651, 481))
        self.widget_3.setStyleSheet("QWidget{\n"
"    background-color: rgb(202, 240, 248);\n"
"}\n"
"QLabel{\n"
"    color: rgb(0, 119, 182);}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(0, 119, 182);\n"
"    color: white;\n"
"}")
        self.widget_3.setObjectName("widget_3")
        self.label_3 = QLabel(self.widget_3)
        self.label_3.setGeometry(QRect(10, 0, 351, 41))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_7 = QLabel(self.widget_3)
        self.label_7.setGeometry(QRect(160, 40, 421, 41))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton = QPushButton(self.widget_3)
        self.pushButton.setGeometry(QRect(120, 150, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_B = QPushButton(self.widget_3)
        self.pushButton_B.setGeometry(QRect(120, 210, 93, 28))
        self.pushButton_B.setObjectName("pushButton_B")
        self.pushButton_C = QPushButton(self.widget_3)
        self.pushButton_C.setGeometry(QRect(120, 270, 93, 28))
        self.pushButton_C.setObjectName("pushButton_C")
        self.pushButton_D = QPushButton(self.widget_3)
        self.pushButton_D.setGeometry(QRect(120, 330, 93, 28))
        self.pushButton_D.setObjectName("pushButton_D")
        self.label_A = QLabel(self.widget_3)
        self.label_A.setGeometry(QRect(220, 150, 261, 16))
        self.label_A.setObjectName("label_A")
        self.label_B = QLabel(self.widget_3)
        self.label_B.setGeometry(QRect(220, 210, 141, 21))
        self.label_B.setObjectName("label_B")
        self.label_C = QLabel(self.widget_3)
        self.label_C.setGeometry(QRect(220, 270, 141, 21))
        self.label_C.setObjectName("label_C")
        self.label_D = QLabel(self.widget_3)
        self.label_D.setGeometry(QRect(220, 330, 221, 20))
        self.label_D.setFont(font)
        self.label_D.setObjectName("label_D")
        self.label_6 = QLabel(self.widget)
        self.label_6.setGeometry(QRect(250, 240, 531, 31))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Pregunta 10"))
        Form.setWindowIcon(QIcon(r"Recursos_Interfaz\Alzcare.png"))
        self.label_2.setText(_translate("Form", "Alzcare - company"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p>Pregunta 10.</p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p>¿El paciente necesita ayuda en sus esfínteres?</p></body></html>"))
        self.pushButton.setText(_translate("Form", "A"))
        self.pushButton_B.setText(_translate("Form", "B"))
        self.pushButton_C.setText(_translate("Form", "C"))
        self.pushButton_D.setText(_translate("Form", "D"))
        self.label_A.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:8pt;\">Control completo de ambos esfínteres</span></p></body></html>"))
        self.label_B.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:8pt;\">Incontinencia ocasional</span></p></body></html>"))
        self.label_C.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:8pt;\">Necesita supervisión</span></p></body></html>"))
        self.label_D.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:8pt;\">Una sonda vesical o es incontinente</span></p></body></html>"))
        self.label_6.setText(_translate("Form", "El cuidador deberá estar presente para realizar las siguientes preguntas:"))

class Formato_Pregunta_10(QDialog):
    def __init__(self, parent=None):
        super(Formato_Pregunta_10, self).__init__(parent)
        self.ui = Pregunta_10()
        self.ui.setupUi(self)

class Botonera(QMainWindow, Alzcare):
    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador
        self.usuario = ""
        self.respuestas = []
        self.setupUi(self)

        self.menu_login = Formato_Log_in()
        self.menu_seguimiento = Formato_Seguimiento()
        self.menu_graficos = Formato_Graficos()
        self.pregunta_1 = Formato_Pregunta_1()
        self.pregunta_2 = Formato_Pregunta_2()
        self.pregunta_3 = Formato_Pregunta_3()
        self.pregunta_4 = Formato_Pregunta_4()
        self.pregunta_5 = Formato_Pregunta_5()
        self.pregunta_6 = Formato_Pregunta_6()
        self.pregunta_7 = Formato_Pregunta_7()
        self.pregunta_8 = Formato_Pregunta_8()
        self.pregunta_9 = Formato_Pregunta_9()
        self.pregunta_10 = Formato_Pregunta_10()
        self.menu_pre_registro = Formato_Pre_Registro()
        self.menu_registro_cuidador = Formato_Registro_Cuidador()
        self.menu_registro_paciente = Formato_Registro_Paciente()

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

        self.menu_seguimiento.ui.pushButton_2.clicked.connect(self.cerrar_sesion)
        self.menu_seguimiento.ui.pushButton_3.clicked.connect(self.exportar_perfil)
        self.menu_seguimiento.ui.pushButton_4.clicked.connect(self.ciclo_preguntas)
        self.menu_seguimiento.ui.pushButton_5.clicked.connect(self.ventana_graficos)

        self.pregunta_1.ui.pushButton.clicked.connect(self.respuesta_pregunta_1)
        self.pregunta_1.ui.pushButton_B.clicked.connect(self.respuesta_pregunta_1)
        self.pregunta_1.ui.pushButton_C.clicked.connect(self.respuesta_pregunta_1)
        self.pregunta_1.ui.pushButton_D.clicked.connect(self.respuesta_pregunta_1)
        self.pregunta_1.ui.pushButton_regresar.clicked.connect(self.ventana_seguimiento)

        self.pregunta_2.ui.pushButton.clicked.connect(self.respuesta_pregunta_2)
        self.pregunta_2.ui.pushButton_C.clicked.connect(self.respuesta_pregunta_2)
        self.pregunta_2.ui.pushButton_regresar.clicked.connect(self.ventana_seguimiento)

        self.pregunta_3.ui.pushButton.clicked.connect(self.respuesta_pregunta_3)
        self.pregunta_3.ui.pushButton_C.clicked.connect(self.respuesta_pregunta_3)
        self.pregunta_3.ui.pushButton_regresar.clicked.connect(self.ventana_seguimiento)
    
        self.pregunta_4.ui.pushButton.clicked.connect(self.respuesta_pregunta_4)
        self.pregunta_4.ui.pushButton_C.clicked.connect(self.respuesta_pregunta_4)
        self.pregunta_4.ui.pushButton_regresar.clicked.connect(self.ventana_seguimiento)

        self.pregunta_5.ui.pushButton.clicked.connect(self.respuesta_pregunta_5)
        self.pregunta_5.ui.pushButton_C.clicked.connect(self.respuesta_pregunta_5)
        self.pregunta_5.ui.pushButton_regresar.clicked.connect(self.ventana_seguimiento)

        self.pregunta_6.ui.pushButton.clicked.connect(self.respuesta_pregunta_6)
        self.pregunta_6.ui.pushButton_B.clicked.connect(self.respuesta_pregunta_6)
        self.pregunta_6.ui.pushButton_C.clicked.connect(self.respuesta_pregunta_6)
        self.pregunta_6.ui.pushButton_regresar.clicked.connect(self.ventana_seguimiento)

        self.pregunta_7.ui.pushButton.clicked.connect(self.respuesta_pregunta_7)
        self.pregunta_7.ui.pushButton_B.clicked.connect(self.respuesta_pregunta_7)
        self.pregunta_7.ui.pushButton_C.clicked.connect(self.respuesta_pregunta_7)
        self.pregunta_7.ui.pushButton_regresar.clicked.connect(self.ventana_seguimiento)

        self.pregunta_8.ui.pushButton.clicked.connect(self.respuesta_pregunta_8)
        self.pregunta_8.ui.pushButton_B.clicked.connect(self.respuesta_pregunta_8)
        self.pregunta_8.ui.pushButton_C.clicked.connect(self.respuesta_pregunta_8)
        self.pregunta_8.ui.pushButton_regresar.clicked.connect(self.ventana_seguimiento)

        self.pregunta_9.ui.pushButton_A.clicked.connect(self.respuesta_pregunta_9)
        self.pregunta_9.ui.pushButton_B.clicked.connect(self.respuesta_pregunta_9)
        self.pregunta_9.ui.pushButton_C.clicked.connect(self.respuesta_pregunta_9)
        self.pregunta_9.ui.pushButton_regresar.clicked.connect(self.ventana_seguimiento)

        self.pregunta_10.ui.pushButton.clicked.connect(self.respuesta_pregunta_10)
        self.pregunta_10.ui.pushButton_B.clicked.connect(self.respuesta_pregunta_10)
        self.pregunta_10.ui.pushButton_C.clicked.connect(self.respuesta_pregunta_10)
        self.pregunta_10.ui.pushButton_D.clicked.connect(self.respuesta_pregunta_10)
        self.pregunta_10.ui.pushButton_regresar.clicked.connect(self.ventana_seguimiento)

        self.menu_pre_registro.ui.pushButton_paciente.clicked.connect(self.ventana_registro_paciente)
        self.menu_pre_registro.ui.pushButton_cuidador.clicked.connect(self.ventana_registro_cuidador)
        self.menu_pre_registro.ui.pushButton_salir.clicked.connect(self.close)
        self.menu_pre_registro.ui.pushButton_regresar.clicked.connect(self.ventanas_inicio)
        self.menu_pre_registro.ui.pushButton.clicked.connect(self.importacion_perfil)

        self.menu_registro_cuidador.ui.pushButton_.clicked.connect(self.registrar_cuidador)
        self.menu_registro_cuidador.ui.pushButton_2.clicked.connect(self.ventana_pre_registro)

        self.menu_registro_paciente.ui.pushButton.clicked.connect(self.registrar_paciente)
        self.menu_registro_paciente.ui.pushButton_2.clicked.connect(self.ventana_pre_registro)

    def ventanas_inicio(self):
        self.menu_login.close()
        self.menu_pre_registro.close()
        self.menu_registro_cuidador.close()
        self.menu_registro_paciente.close()
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

    def ventana_seguimiento(self):
        usuario = self.menu_login.ui.lineEdit.text()
        contrasena = self.menu_login.ui.lineEdit_2.text()
        if self.controlador.validar_usuario(usuario, contrasena):
            QMessageBox.information(self, "Ingreso", "Ingreso exitoso")
            self.menu_login.close()
            self.usuario = usuario
            self.menu_seguimiento.show()
        else:
            QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos")

    def cerrar_sesion(self):
        self.menu_seguimiento.close()
        self.usuario = ""
        self.ventanas_inicio()
    
    def ventana_graficos(self):
        self.menu_seguimiento.close()
        pixmap,punto = self.controlador.grafico(self.usuario)
        if punto >= 21:
            QMessageBox.information(self, "Resultado", "Vas muy bien :D")
        elif punto >= 16:
            QMessageBox.information(self, "Resultado", "Puedes mejorar :|")
        elif punto >= 11:
            QMessageBox.information(self, "Resultado", "Debes mejorar :(")
        else:
            QMessageBox.information(self, "Resultado", "Debes mejorar mucho :C")
        self.menu_graficos.ui.label_2.setPixmap(pixmap)
        self.menu_graficos.ui.label_2.setScaledContents(True)
        self.menu_graficos.show()

    def ciclo_preguntas(self):
        self.menu_seguimiento.close()
        self.pregunta_1.show()

    def respuesta_pregunta_1(self):
        respuesta = str(self.sender().text())
        self.respuestas.append(respuesta)
        self.controlador.puntos(respuesta)
        self.pregunta_1.close()
        self.pregunta_2.show()
    
    def respuesta_pregunta_2(self):
        respuesta = str(self.sender().text())
        if respuesta == "C":
            respuesta = "D"
        self.respuestas.append(respuesta)
        self.controlador.puntos(respuesta)
        self.pregunta_2.close()
        self.pregunta_3.show()
    
    def respuesta_pregunta_3(self):
        respuesta = str(self.sender().text())
        if respuesta == "C":
            respuesta = "D"
        self.respuestas.append(respuesta)
        self.controlador.puntos(respuesta)
        self.pregunta_3.close()
        self.pregunta_4.show()
    
    def respuesta_pregunta_4(self):
        respuesta = str(self.sender().text())
        if respuesta == "C":
            respuesta = "D"
        self.respuestas.append(respuesta)
        self.controlador.puntos(respuesta)
        self.pregunta_4.close()
        self.pregunta_5.show()
    
    def respuesta_pregunta_5(self):
        respuesta = str(self.sender().text())
        if respuesta == "C":
            respuesta = "D"
        self.respuestas.append(respuesta)
        self.controlador.puntos(respuesta)
        self.pregunta_5.close()
        self.pregunta_6.show()

    def respuesta_pregunta_6(self):
        respuesta = str(self.sender().text())
        if respuesta == "C":
            respuesta = "D"
        self.respuestas.append(respuesta)
        self.controlador.puntos(respuesta)
        self.pregunta_6.close()
        self.pregunta_7.show()
    
    def respuesta_pregunta_7(self):
        respuesta = str(self.sender().text())
        if respuesta == "C":
            respuesta = "D"
        elif respuesta == "B":
            respuesta = "C"
        self.respuestas.append(respuesta)
        self.controlador.puntos(respuesta)
        self.pregunta_7.close()
        self.pregunta_8.show()
    
    def respuesta_pregunta_8(self):
        respuesta = str(self.sender().text())
        if respuesta == "C":
            respuesta = "D"
        self.respuestas.append(respuesta)    
        self.controlador.puntos(respuesta)
        self.pregunta_8.close()
        self.pregunta_9.show()

    def respuesta_pregunta_9(self):
        respuesta = str(self.sender().text())
        if respuesta == "C":
            respuesta = "D"
        self.respuestas.append(respuesta)
        self.controlador.puntos(respuesta)
        self.pregunta_9.close()
        self.pregunta_10.show()

    def respuesta_pregunta_10(self):
        respuesta = str(self.sender().text())
        self.respuestas.append(respuesta)
        self.controlador.puntos(respuesta)
        if self.controlador.registro_seguimiento(self.usuario, self.respuestas):
            QMessageBox.information(self, "Registro", "Seguimiento registrado con éxito")
            self.pregunta_10.close()
            self.menu_seguimiento.show()
            self.respuestas = []
        else:
            QMessageBox.warning(self, "Error", "No se pudo registrar el seguimiento")
            self.pregunta_10.close()
            self.menu_seguimiento.show()
            self.respuestas = []

    def boton_paginaRegistro(self):
        self.stackedWidget.setCurrentIndex(2)
        QTimer.singleShot(4000, self.ventana_pre_registro)
    
    def ventana_pre_registro(self):
        self.close()
        self.menu_registro_cuidador.close()
        self.menu_registro_paciente.close()
        self.menu_pre_registro.show()

    def ventana_registro_paciente(self):
        self.menu_pre_registro.close()
        self.menu_registro_paciente.show()
    
    def ventana_registro_cuidador(self):
        self.menu_pre_registro.close()
        self.menu_registro_cuidador.show()
    
    def registrar_paciente(self):
        nombre = self.menu_registro_paciente.ui.lineEdit_nombre.text()
        edad = int(self.menu_registro_paciente.ui.lineEdit_edad.text())
        telefono = int(self.menu_registro_paciente.ui.lineEdit_celular.text())
        cedula = int(self.menu_registro_paciente.ui.lineEdit_cedula.text())
        lugar_residencia = self.menu_registro_paciente.ui.lineEdit_residencia.text()
        lugar_nacimiento = self.menu_registro_paciente.ui.lineEdit_nacimiento.text()
        fase_alzheimer = self.menu_registro_paciente.ui.lineEdit_fasealz.text()
        estudio = self.menu_registro_paciente.ui.lineEdit_estudio.text()
        dominancia = self.menu_registro_paciente.ui.lineEdit_dominancia.text()
        tiempo_alzheimer = self.menu_registro_paciente.ui.lineEdit_tipoalz.text()
        if not(nombre and edad and telefono and cedula and lugar_residencia and lugar_nacimiento and fase_alzheimer and estudio and dominancia and tiempo_alzheimer):
            QMessageBox.warning(self, "Error", "Por favor llene todos los campos")
        else:
            if self.controlador.registro_paciente(nombre, nombre, edad, telefono, cedula, lugar_residencia, lugar_nacimiento, fase_alzheimer, estudio, dominancia, tiempo_alzheimer):
                QMessageBox.information(self, "Registro", "Paciente registrado con éxito")
                self.menu_registro_paciente.ui.lineEdit_nombre.clear()
                self.menu_registro_paciente.ui.lineEdit_edad.clear()
                self.menu_registro_paciente.ui.lineEdit_celular.clear()
                self.menu_registro_paciente.ui.lineEdit_cedula.clear()
                self.menu_registro_paciente.ui.lineEdit_residencia.clear()
                self.menu_registro_paciente.ui.lineEdit_nacimiento.clear()
                self.menu_registro_paciente.ui.lineEdit_fasealz.clear()
                self.menu_registro_paciente.ui.lineEdit_estudio.clear()
                self.menu_registro_paciente.ui.lineEdit_dominancia.clear()
                self.menu_registro_paciente.ui.lineEdit_tipoalz.clear()
                self.menu_registro_paciente.close()
                self.menu_pre_registro.show()
            else:
                QMessageBox.warning(self, "Error", "No se pudo registrar al paciente")
    
    def registrar_cuidador(self):
        nombre = self.menu_registro_cuidador.ui.lineEdit_nombre.text()
        apellido = self.menu_registro_cuidador.ui.lineEdit_apellido.text()
        cedula = int(self.menu_registro_cuidador.ui.lineEdit_cedula.text())
        contrasena = self.menu_registro_cuidador.ui.lineEdit_contrasena.text()
        telefono = int(self.menu_registro_cuidador.ui.lineEdit_celular.text())
        formacion = self.menu_registro_cuidador.ui.lineEdit_formacion.text()
        usuario = self.menu_registro_cuidador.ui.lineEdit_usuario.text()
        if not(nombre and apellido and cedula and contrasena and telefono and formacion and usuario):
            QMessageBox.warning(self, "Error", "Por favor llene todos los campos")
        else:
            if self.controlador.registro_cuidador(nombre, apellido, telefono, cedula, formacion, usuario, contrasena):
                QMessageBox.information(self, "Registro", "Cuidador registrado con éxito")
                self.menu_registro_cuidador.ui.lineEdit_nombre.clear()
                self.menu_registro_cuidador.ui.lineEdit_apellido.clear()
                self.menu_registro_cuidador.ui.lineEdit_cedula.clear()
                self.menu_registro_cuidador.ui.lineEdit_contrasena.clear()
                self.menu_registro_cuidador.ui.lineEdit_celular.clear()
                self.menu_registro_cuidador.ui.lineEdit_formacion.clear()
                self.menu_registro_cuidador.ui.lineEdit_usuario.clear()
                self.menu_registro_cuidador.close()
                self.menu_pre_registro.show()
            else:
                QMessageBox.warning(self, "Error", "No se pudo registrar al cuidador")
  
    def boton_paginaMoca(self):
        self.stackedWidget.setCurrentIndex(3)
        QTimer.singleShot(4000, (lambda: webbrowser.open("https://mocacognition.com/paper/")))

    def importacion_perfil(self):
        direccion, _ = QFileDialog.getOpenFileName(self, "Seleccione el archivo", "", "JSON Files (*.json)")
        if direccion:
            if self.controlador.importar_datos(direccion):
                QMessageBox.information(self, "Importación", "Datos importados con éxito")
            else:
                QMessageBox.warning(self, "Error", "No se pudo importar los datos")
    
    def exportar_perfil(self, usuario):
        if self.controlador.exportar_perfil(usuario):
            QMessageBox.information(self, "Exportación", "Datos exportados con éxito")
        else:
            QMessageBox.warning(self, "Error", "No se pudo exportar los datos")