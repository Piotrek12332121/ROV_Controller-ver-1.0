from PySide6.QtWidgets import QWidget ,QMainWindow,QPushButton,QHBoxLayout

"""
The class that contains the main window

"""
class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ROV controller ver 1.0")
        
        button1=QPushButton("click me!1")
        button2=QPushButton("click me!2")

        button1.clicked.connect(self.button_clicked1)
        button2.clicked.connect(self.button_clicked2)

        MainApp_layout=QHBoxLayout()
        MainApp_layout.addWidget(button1)
        MainApp_layout.addWidget(button2)


        self.setLayout(MainApp_layout)



    def button_clicked1(self):
        print("button1 was clicked")

    def button_clicked2(self):
        print("button2 was clicked")