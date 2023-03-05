from PySide6.QtWidgets import QApplication, QWidget,QMainWindow,QPushButton
from MainWindow import MainApp
import sys

app=QApplication(sys.argv)
window=MainApp(app)
window.show()

app.exec()