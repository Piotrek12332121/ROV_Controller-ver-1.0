from PySide6.QtWidgets import QWidget ,QMainWindow,QPushButton,QHBoxLayout,QFrame,QComboBox
from PySide6.QtWidgets import QApplication, QWidget,QSlider,QVBoxLayout,QLabel
from PySide6.QtCore import QObject, Qt
import serial.tools.list_ports
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
        file_menu=menu_bar.addMenu("Set commands")  # TODO apply
        self.setGeometry(100, 100, 400, 300)

        # Setting up sliders and connecting them with functions

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

        ### USB Port menu box 

        self.portComboBox = QComboBox(self)
        self.portComboBox.setGeometry(50, 50, 200, 30)

        ports = serial.tools.list_ports.comports()
        for port in ports:
            self.portComboBox.addItem(port.device)

        print(self.portComboBox.currentIndex())

        layout=QVBoxLayout()

        row_0=QHBoxLayout()

        labelA = QLabel("Engine A")
        labelB = QLabel("Engine B")
        labelC = QLabel("Engine C")
        labelD = QLabel("Engine D")

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
        labelPort = QLabel("Port:")
        row_2.addWidget(labelPort)
        row_2.addWidget(self.portComboBox)

        button = QPushButton("Connect!")
        button.setCheckable(True) 
        button.toggled.connect(self.onToggled)
        row_2.addWidget(button)

        line = QFrame()
        line.setFrameShape(QFrame.HLine) 
        line.setFrameShadow(QFrame.Sunken)




        ### generates overall main shape of the app
        layout.addLayout(row_2)
        layout.addWidget(line)
        layout.addLayout(row_0)
        layout.addLayout(row_1)
   

        

        widget=QWidget()
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)


    ### checks if any key was pressed, if so sends commands via chosen USB Port 
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


    