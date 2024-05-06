from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QWidget, QPushButton, QGridLayout, QLCDNumber


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        self.__current_value = ""

        push_button_1 = QPushButton("1")
        push_button_2 = QPushButton("2")
        push_button_3 = QPushButton("3")
        push_button_4 = QPushButton("4")
        push_button_5 = QPushButton("5")
        push_button_6 = QPushButton("6")
        push_button_7 = QPushButton("7")
        push_button_8 = QPushButton("8")
        push_button_9 = QPushButton("9")
        push_button_0 = QPushButton("0")
        push_button_dot = QPushButton(".")

        push_button_1.released.connect(self.handle_1)
        push_button_2.released.connect(self.handle_2)
        push_button_3.released.connect(self.handle_3)
        push_button_4.released.connect(self.handle_4)
        push_button_5.released.connect(self.handle_5)
        push_button_6.released.connect(self.handle_6)
        push_button_7.released.connect(self.handle_7)
        push_button_8.released.connect(self.handle_8)
        push_button_9.released.connect(self.handle_9)
        push_button_0.released.connect(self.handle_0)
        push_button_dot.released.connect(self.handle_dot)

        push_button_equal = QPushButton("=")

        push_button_add = QPushButton("+")
        push_button_sub = QPushButton("-")
        push_button_mul = QPushButton("*")
        push_button_div = QPushButton("/")

        self.display = QLCDNumber()

        grid_layout = QGridLayout()

        grid_layout.addWidget(self.display, 1, 1, 1, 4)

        grid_layout.addWidget(push_button_7, 2, 1)
        grid_layout.addWidget(push_button_8, 2, 2)
        grid_layout.addWidget(push_button_9, 2, 3)
        grid_layout.addWidget(push_button_add, 2, 4)

        grid_layout.addWidget(push_button_4, 3, 1)
        grid_layout.addWidget(push_button_5, 3, 2)
        grid_layout.addWidget(push_button_6, 3, 3)
        grid_layout.addWidget(push_button_sub, 3, 4)

        grid_layout.addWidget(push_button_1, 4, 1)
        grid_layout.addWidget(push_button_2, 4, 2)
        grid_layout.addWidget(push_button_3, 4, 3)
        grid_layout.addWidget(push_button_mul, 4, 4)

        grid_layout.addWidget(push_button_0, 5, 1)
        grid_layout.addWidget(push_button_dot, 5, 2)
        grid_layout.addWidget(push_button_equal, 5, 3)
        grid_layout.addWidget(push_button_div, 5, 4)

        self.setLayout(grid_layout)

    @pyqtSlot()
    def handle_1(self):
        self.__current_value += "1"

        self.display.display(self.__current_value)

    @pyqtSlot()
    def handle_2(self):
        self.__current_value += "2"

        self.display.display(self.__current_value)

    @pyqtSlot()
    def handle_3(self):
        self.__current_value += "3"

        self.display.display(self.__current_value)

    @pyqtSlot()
    def handle_4(self):
        self.__current_value += "4"

        self.display.display(self.__current_value)

    @pyqtSlot()
    def handle_5(self):
        self.__current_value += "5"

        self.display.display(self.__current_value)

    @pyqtSlot()
    def handle_6(self):
        self.__current_value += "6"

        self.display.display(self.__current_value)

    @pyqtSlot()
    def handle_7(self):
        self.__current_value += "7"

        self.display.display(self.__current_value)

    @pyqtSlot()
    def handle_8(self):
        self.__current_value += "8"

        self.display.display(self.__current_value)

    @pyqtSlot()
    def handle_9(self):
        self.__current_value += "9"

        self.display.display(self.__current_value)

    @pyqtSlot()
    def handle_0(self):
        self.__current_value += "0"

        self.display.display(self.__current_value)

    @pyqtSlot()
    def handle_dot(self):
        self.__current_value += "."

        self.display.display(self.__current_value)
