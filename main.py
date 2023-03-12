from PySide6.QtWidgets import QApplication
from MainWindow import MainApp
import sys
"""
App for controling an underwater ROV, sends data via USB port.
The data is structured as follows:
first byte : the engine name ( one of :'A','B','C','D')
second byte: the speed value (an int between 0 and 250)
"""
if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=MainApp(app)
    window.show()

    app.exec()