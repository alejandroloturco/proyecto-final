from PyQt5.QtWidgets import QLabel, QApplication
from PyQt5.QtGui import QPixmap
import sys

def show_image():
    # Crear una aplicación Qt (necesario para cualquier programa Qt)
    app = QApplication(sys.argv)

    # Crear un QLabel
    label = QLabel()

    # Cargar la imagen en un QPixmap
    pixmap = QPixmap(r"Version_mario_proyecto final\Recursos_Interfaz\Alzcare.png")

    # Establecer el QPixmap en el QLabel
    label.setPixmap(pixmap)

    # Mostrar el QLabel
    label.show()

    # Iniciar el bucle de eventos de la aplicación
    sys.exit(app.exec_())

# Llamar a la función
show_image()