from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from Menu import Mymenu

app = QApplication(sys.argv)

window = Mymenu()

window.show()
app.exec()