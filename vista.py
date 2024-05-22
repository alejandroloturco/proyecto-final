import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QStackedWidget, QLineEdit, QFormLayout
from PyQt5.QtCore import QTimer

class InitialWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Aviso de Seguridad')
        self.setGeometry(100, 100, 1280, 720)
        self.setStyleSheet("background-color: green;")
        
        layout = QVBoxLayout()
        label = QLabel('''!ADIVOS DE SALUD Y SEGURIDAD\nPara el ingreso de info se debe de tener al cuidador en la sala''')
        label.setStyleSheet("color: white; font-size: 18px;")
        layout.addWidget(label)
        self.setLayout(layout)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ventana de Inicio')
        self.setGeometry(100, 100, 1280, 720)
        self.setStyleSheet("background-color: gray;")
        
        layout = QVBoxLayout()
        self.login_button = QPushButton('Log IN')
        self.register_button = QPushButton('Registro')
        self.moka_button = QPushButton('MOKA')
        self.exit_button = QPushButton('Salir')
        
        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)
        layout.addWidget(self.moka_button)
        layout.addWidget(self.exit_button)
        
        self.setLayout(layout)

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')
        self.setGeometry(100, 100, 1280, 720)
        self.setStyleSheet("background-color: blue;")
        
        layout = QVBoxLayout()
        form_layout = QFormLayout()
        
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        
        form_layout.addRow('Usuario:', self.username_input)
        form_layout.addRow('Contraseña:', self.password_input)
        
        self.login_button = QPushButton('Entrar')
        self.exit_button = QPushButton('Salir')
        
        layout.addLayout(form_layout)
        layout.addWidget(self.login_button)
        layout.addWidget(self.exit_button)
        
        self.setLayout(layout)

class RegistroWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Registro')
        self.setGeometry(100, 100, 1280, 720)
        self.setStyleSheet("background-color: pink;")
        
        layout = QVBoxLayout()
        form_layout = QFormLayout()
        
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.name_input = QLineEdit()
        self.cc_input = QLineEdit()
        self.phone_input = QLineEdit()
        
        form_layout.addRow('Usuario:', self.username_input)
        form_layout.addRow('Contraseña:', self.password_input)
        form_layout.addRow('Nombre:', self.name_input)
        form_layout.addRow('CC:', self.cc_input)
        form_layout.addRow('Teléfono:', self.phone_input)
        
        self.register_button = QPushButton('Registrar')
        
        layout.addLayout(form_layout)
        layout.addWidget(self.register_button)
        
        self.setLayout(layout)

class MOKAWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('MOKA')
        self.setGeometry(100, 100, 1280, 720)
        self.setStyleSheet("background-color: red;")
        
        layout = QVBoxLayout()
        self.label = QLabel('Opcional: NO SE GUARDA')
        self.label.setStyleSheet("color: white; font-size: 18px;")
        layout.addWidget(self.label)
        self.setLayout(layout)

class MainApp(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('AlzCare')
        self.setGeometry(100, 100, 1280, 720)
        
        self.initial_window = InitialWindow()
        self.main_window = MainWindow()
        self.login_window = LoginWindow()
        self.registro_window = RegistroWindow()
        self.moka_window = MOKAWindow()
        
        self.addWidget(self.initial_window)
        self.addWidget(self.main_window)
        self.addWidget(self.login_window)
        self.addWidget(self.registro_window)
        self.addWidget(self.moka_window)
        
        QTimer.singleShot(3000, self.show_main_window)
        
        self.main_window.login_button.clicked.connect(self.show_login_window)
        self.main_window.register_button.clicked.connect(self.show_registro_window)
        self.main_window.moka_button.clicked.connect(self.show_moka_window)
        self.main_window.exit_button.clicked.connect(self.close)
        
        self.login_window.login_button.clicked.connect(self.show_main_window)
        self.login_window.exit_button.clicked.connect(self.close)
        
    def show_main_window(self):
        self.setCurrentWidget(self.main_window)
        
    def show_login_window(self):
        self.setCurrentWidget(self.login_window)
        
    def show_registro_window(self):
        self.setCurrentWidget(self.registro_window)
        
    def show_moka_window(self):
        self.setCurrentWidget(self.moka_window)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())
