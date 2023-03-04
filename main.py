from PySide6.QtWidgets import QApplication, QWidget,QMainWindow,QPushButton
from MainWindow import MainApp
import sys

app=QApplication(sys.argv)
window=MainApp()
window.show()
app.exec()