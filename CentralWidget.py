from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QWidget, QPushButton, QGridLayout, QLCDNumber


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        self.__last_value = None
        self.__current_value = None
        self.__operator = None

        self.handle_clear()

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

        push_button_1.released.connect(self.handle_digit)
        push_button_2.released.connect(self.handle_digit)
        push_button_3.released.connect(self.handle_digit)
        push_button_4.released.connect(self.handle_digit)
        push_button_5.released.connect(self.handle_digit)
        push_button_6.released.connect(self.handle_digit)
        push_button_7.released.connect(self.handle_digit)
        push_button_8.released.connect(self.handle_digit)
        push_button_9.released.connect(self.handle_digit)
        push_button_0.released.connect(self.handle_digit)
        push_button_dot.released.connect(self.handle_digit)

        push_button_sign = QPushButton("(-)")

        push_button_sign.released.connect(self.handle_sign)

        push_button_equal = QPushButton("=")
        push_button_clear = QPushButton("clear")

        push_button_equal.released.connect(self.handle_equal)
        push_button_clear.released.connect(self.handle_clear)

        push_button_add = QPushButton("+")
        push_button_sub = QPushButton("-")
        push_button_mul = QPushButton("*")
        push_button_div = QPushButton("/")

        push_button_add.released.connect(self.handle_operator)
        push_button_sub.released.connect(self.handle_operator)
        push_button_mul.released.connect(self.handle_operator)
        push_button_div.released.connect(self.handle_operator)

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
        grid_layout.addWidget(push_button_sign, 5, 3)
        grid_layout.addWidget(push_button_div, 5, 4)

        grid_layout.addWidget(push_button_clear, 6, 1, 1, 2)
        grid_layout.addWidget(push_button_equal, 6, 3, 1, 2)

        self.setLayout(grid_layout)

    @pyqtSlot()
    def handle_digit(self):
        self.__current_value += self.sender().text()

        self.display.display(self.__current_value)

    @pyqtSlot()
    def handle_sign(self):
        try:
            if self.__current_value[0] != "-":
                self.__current_value = "-" + self.__current_value
        except IndexError:
            self.display.display("error")
        else:
            self.display.display(self.__current_value)

    @pyqtSlot()
    def handle_operator(self):
        self.__operator = self.sender().text()

        self.__last_value = self.__current_value
        self.__current_value = ""

        self.display.display(self.__current_value)

    @pyqtSlot()
    def handle_equal(self):
        left_value = float(self.__current_value)
        right_value = float(self.__last_value)

        result = left_value
        if self.__operator == "/":
            result = right_value / left_value
        elif self.__operator == "*":
            result = right_value * left_value
        elif self.__operator == "+":
            result = right_value + left_value
        elif self.__operator == "-":
            result = right_value - left_value
        else:
            print("No operator set")

        self.__current_value = str(result)

        self.display.display(self.__current_value)

    @pyqtSlot()
    def handle_clear(self):
        self.__current_value = "123"
        self.__last_value = ""
        self.__operator = ""

        self.display.display("---")
