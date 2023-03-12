from PySide6.QtWidgets import QWidget ,QMainWindow,QPushButton,QHBoxLayout,QFrame,QComboBox,QWidget,QSlider,QVBoxLayout,QLabel
from PySide6.QtCore import  Qt
import serial.tools.list_ports
import time 

"""
The class that contains the main app

"""

class MainApp(QMainWindow,QWidget):
    def __init__(self,app):
        super().__init__()
        self.setWindowTitle("ROV controller ver 1.0")
        self.app=app
        self.is_serial_active=False # is True when Serial connection is estabished

        menu_bar=self.menuBar()
        file_menu=menu_bar.addMenu("Menu")

        quit_action=file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)

        self.setGeometry(100, 100, 400, 300)

        # Setting up sliders 

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


        ### USB Port menu box , lists all available ports 

        self.portComboBox = QComboBox(self)
        self.portComboBox.setGeometry(50, 50, 200, 30)
        ports = serial.tools.list_ports.comports()
        for port in ports:
            self.portComboBox.addItem(port.device)
        
        # Row 0
        row_0=QHBoxLayout()
        labelPort = QLabel("Port:")
        row_0.addWidget(labelPort)
        row_0.addWidget(self.portComboBox)

        button = QPushButton("Connect!")
        button.clicked.connect(self.connect_pressed)
        row_0.addWidget(button)

        # Separating line 
        line = QFrame()
        line.setFrameShape(QFrame.HLine) 
        line.setFrameShadow(QFrame.Sunken)

        # Row 1
        row_1=QHBoxLayout()
        labelA = QLabel("Engine A")
        labelB = QLabel("Engine B")
        labelC = QLabel("Engine C")
        labelD = QLabel("Engine D")
        row_1.addWidget(labelA)
        row_1.addWidget(labelB)
        row_1.addWidget(labelC)
        row_1.addWidget(labelD)

        # Row 2
        row_2=QHBoxLayout()
        row_2.addWidget(self.sliderA)
        row_2.addWidget(self.sliderB)
        row_2.addWidget(self.sliderC)
        row_2.addWidget(self.sliderD)
        
        ### generates overall main shape of the app
        main_layout=QVBoxLayout()
        main_layout.addLayout(row_0)
        main_layout.addWidget(line)
        main_layout.addLayout(row_1)
        main_layout.addLayout(row_2)

        widget=QWidget()
        widget.setLayout(main_layout)
        
        self.setCentralWidget(widget)


    ### checks if any key was pressed, if so sends commands via chosen USB Port 

    def keyPressEvent(self, event):
            if event.key() == Qt.Key_J:        ### TURN RIGHT 
                print("Left key pressed")
                if self.is_serial_active:
                    # turn left engine on 
                    self.send_via_USB('A',self.sliderA.value())
                    # turn right engine off
                    time.sleep(0.001)
                    self.send_via_USB('B',int(0))

            elif event.key() == Qt.Key_L:      ### TURN LEFT
                print("Right key pressed")
                if self.is_serial_active:
                    ##turn right engine on 
                    self.send_via_USB('B',self.sliderB.value())
                    ##turn left engine off
                    time.sleep(0.001)
                    self.send_via_USB('A',int(0))


            elif event.key() == Qt.Key_I:      ### GO FORWARD
                print("Forward key pressed")
                if self.is_serial_active:
                    ##turn left engine on 
                    self.send_via_USB('A',self.sliderA.value())
                    ##turn right engine on 
                    time.sleep(0.001)
                    self.send_via_USB('B',self.sliderB.value())


            elif event.key() == Qt.Key_K:      ### STOP
                print("Reverse key pressed")
                if self.is_serial_active:
                    ##turn left engine off 
                    self.send_via_USB('A',0)
                    ##turn right engine off 
                    time.sleep(0.001)
                    self.send_via_USB('B',0)
                

            elif event.key() == Qt.Key_W:      ### GO UP
                print("W key pressed")
                if self.is_serial_active:
                     ##turn left engine off 
                    self.send_via_USB('C',self.sliderC.value())
                    ##turn right engine off 
                    time.sleep(0.001)
                    self.send_via_USB('D',self.sliderD.value())

            
            elif event.key() == Qt.Key_S:      ### STOP
                print("S key pressed")
                if self.is_serial_active:
                     ##turn left engine off 
                    self.send_via_USB('C',0)
                    ##turn right engine off 
                    time.sleep(0.001)
                    self.send_via_USB('D',0)


    def send_via_USB(self,engine: chr,value : int):      ### method for sending signals via USB - needs engine name and speed value 

        assert value >=0, f"Value {value} needs to be between 0 and 250"
        assert value <=250, f"Value {value} needs to be between 0 and 250"
        

        message=engine
        message=message.encode(encoding='ascii')         
        val=value
        data_bytes=val.to_bytes(1,byteorder='little') 

        self.ser.write(message)   
        self.ser.write(data_bytes)

    def connect_pressed(self):    ### establishing connection via USB port (and then via RS485 module)
        index=self.portComboBox.currentIndex()
        value = self.portComboBox.itemText(index)
        print(value)
        print(type(value))
        self.ser=serial.Serial(value, 115200)
        self.is_serial_active=True

    def quit_app(self):
        self.app.quit()


    