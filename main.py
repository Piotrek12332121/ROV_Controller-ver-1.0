from PySide6.QtWidgets import QApplication
from MainWindow import MainApp
import sys

if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=MainApp(app)
    window.show()

    app.exec()