from PySide6.QtWidgets import QWidget ,QMainWindow,QPushButton,QHBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QApplication, QWidget,QSlider,QVBoxLayout,QLabel

"""
The class that contains the main window

"""

class MainApp(QMainWindow,QWidget):
    def __init__(self,app):
        super().__init__()
        self.setWindowTitle("ROV controller ver 1.0")
        self.app=app
        menu_bar=self.menuBar()
        file_menu=menu_bar.addMenu("Menu")
        quit_action=file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)
        self.setGeometry(100, 100, 400, 300)

        self.sliderA = QSlider(Qt.Vertical)
        self.sliderB = QSlider(Qt.Vertical)
        self.sliderC = QSlider(Qt.Vertical)
        self.sliderD = QSlider(Qt.Vertical)

        self.sliderA.setMinimum(0)
        self.sliderA.setMaximum(250)
        self.sliderA.setValue(50)

        self.sliderB.setMinimum(0)
        self.sliderB.setMaximum(250)
        self.sliderB.setValue(50)

        self.sliderC.setMinimum(0)
        self.sliderC.setMaximum(250)
        self.sliderC.setValue(50)

        self.sliderD.setMinimum(0)
        self.sliderD.setMaximum(250)
        self.sliderD.setValue(50)

        self.sliderA.valueChanged.connect(self.on_sliderA_value_changed)
        self.sliderB.valueChanged.connect(self.on_sliderB_value_changed)
        self.sliderC.valueChanged.connect(self.on_sliderC_value_changed)
        self.sliderD.valueChanged.connect(self.on_sliderD_value_changed)

        layout=QVBoxLayout()

        row_0=QHBoxLayout()

        labelA = QLabel("Silnik A")
        labelB = QLabel("Silnik B")
        labelC = QLabel("Silnik C")
        labelD = QLabel("Silnik D")

        row_0.addWidget(labelA)
        row_0.addWidget(labelB)
        row_0.addWidget(labelC)
        row_0.addWidget(labelD)

        row_1=QHBoxLayout()
        row_1.addWidget(self.sliderA)
        row_1.addWidget(self.sliderB)
        row_1.addWidget(self.sliderC)
        row_1.addWidget(self.sliderD)
        
        row_2=QHBoxLayout()
        button = QPushButton("Włącz wyjście")
        button.setCheckable(True) 
        button.toggled.connect(self.onToggled)

        layout.addLayout(row_0)
        layout.addLayout(row_1)
        layout.addWidget(button)


        widget=QWidget()
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)



    def keyPressEvent(self, event):
            if event.key() == Qt.Key_J:
                print("Left key pressed")
            elif event.key() == Qt.Key_L:
                print("Right key pressed")
            elif event.key() == Qt.Key_I:
                print("Forward key pressed")
            elif event.key() == Qt.Key_K:
                print("Reverse key pressed")

            elif event.key() == Qt.Key_W:
                print("W key pressed")
            elif event.key() == Qt.Key_S:
                print("S key pressed")

    def on_sliderA_value_changed(self, value):
        print(f"Slider A value changed to {value}")
        
    def on_sliderB_value_changed(self, value):
        print(f"Slider B value changed to {value}")
    def on_sliderC_value_changed(self, value):
        print(f"Slider C value changed to {value}")
        
    def on_sliderD_value_changed(self, value):
        print(f"Slider D value changed to {value}")

    def onToggled(self, checked):
        if checked:
            print("Pressed")
        else:
            print("Released")
    def quit_app(self):
        self.app.quit()