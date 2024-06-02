from interfaz_moderna import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class Mymenu(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.icon_2.setHidden(True)
        
        self.boton_inicio1.clicked.connect(self.boton_paginaInicio)
        self.boton_inicio2.clicked.connect(self.boton_paginaInicio)
        
        self.boton_ingreso1.clicked.connect(self.boton_paginaIngreso)
        self.boton_ingreso2.clicked.connect(self.boton_paginaIngreso)

        self.boton_registro1.clicked.connect(self.boton_paginaRegistro)
        self.boton_registro2.clicked.connect(self.boton_paginaRegistro)

        self.boton_moca1.clicked.connect(self.boton_paginaMoca)
        self.boton_moca2.clicked.connect(self.boton_paginaMoca)


    def boton_paginaInicio(self):
        self.stackedWidget.setCurrentIndex(0)
    
    def boton_paginaIngreso(self):
        self.stackedWidget.setCurrentIndex(1)
    
    def boton_paginaRegistro(self):
        self.stackedWidget.setCurrentIndex(2)
    
    def boton_paginaMoca(self):
        self.stackedWidget.setCurrentIndex(3)
    
