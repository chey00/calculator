from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QWidget, QPushButton, QGridLayout, QLCDNumber


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        self.__current_value = ""

        push_button_1 = QPushButton("1")
        push_button_1.released.connect(self.handle_1)
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

        # 1) Erstellen Sie für jedes Button einen passenden Slot.
        # 2) Verbinden Sie jedes Button mit dem zugehörigen Slot.

    @pyqtSlot()
    def handle_1(self):
        self.__current_value += "1"

        self.display.display(self.__current_value)
