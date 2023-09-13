"""Calculator View"""
from PySide6 import QtCore, QtWidgets
from calculator_controller import CalculatorController
from calculator_model import CalculatorModel
from shared import ArithOp


class Calculator(QtWidgets.QWidget):
    """This widget is a calculator"""

    def __init__(self, model: CalculatorModel, controller: CalculatorController):
        super().__init__()

        self.digits_buttons = []
        self._model = model
        self._controller = controller

        self.plus_btn = QtWidgets.QPushButton("+")
        self.minus_btn = QtWidgets.QPushButton("-")
        self.multi_btn = QtWidgets.QPushButton("*")
        self.divide_btn = QtWidgets.QPushButton("/")
        self.equal_btn = QtWidgets.QPushButton("=")
        self.c_btn = QtWidgets.QPushButton("C")

        for i in range(0, 10):
            self.digits_buttons.append(QtWidgets.QPushButton(str(i)))

        self.display = QtWidgets.QLabel(
            "0", alignment=QtCore.Qt.AlignmentFlag.AlignRight)

        self.grid_layout = QtWidgets.QGridLayout(self)
        self.grid_layout.addWidget(self.display, 0, 0, 1, 4)

        self.grid_layout.addWidget(self.c_btn, 1, 0, 1, 3)

        self.grid_layout.addWidget(self.plus_btn, 1, 3)
        self.grid_layout.addWidget(self.minus_btn, 2, 3)
        self.grid_layout.addWidget(self.multi_btn, 3, 3)
        self.grid_layout.addWidget(self.divide_btn, 4, 3)
        self.grid_layout.addWidget(self.equal_btn, 5, 3)

        self.grid_layout.addWidget(self.digits_buttons[0], 5, 0, 1, 3)
        self.grid_layout.addWidget(self.digits_buttons[1], 4, 0)
        self.grid_layout.addWidget(self.digits_buttons[2], 4, 1)
        self.grid_layout.addWidget(self.digits_buttons[3], 4, 2)
        self.grid_layout.addWidget(self.digits_buttons[4], 3, 0)
        self.grid_layout.addWidget(self.digits_buttons[5], 3, 1)
        self.grid_layout.addWidget(self.digits_buttons[6], 3, 2)
        self.grid_layout.addWidget(self.digits_buttons[7], 2, 0)
        self.grid_layout.addWidget(self.digits_buttons[8], 2, 1)
        self.grid_layout.addWidget(self.digits_buttons[9], 2, 2)

        self.plus_btn.clicked.connect(
            self._controller.operation_clicked(ArithOp.PLUS))
        self.minus_btn.clicked.connect(
            self._controller.operation_clicked(ArithOp.MINUS))
        self.multi_btn.clicked.connect(
            self._controller.operation_clicked(ArithOp.MULTIPLY))
        self.divide_btn.clicked.connect(
            self._controller.operation_clicked(ArithOp.DIVIDE))
        self.equal_btn.clicked.connect(self._controller.equal_clicked)
        self.c_btn.clicked.connect(self._controller.c_clicked)

        for i in range(0, 10):
            self.digits_buttons[i].clicked.connect(
                self._controller.digit_click_factory(str(i)))

        self._model._display_text.connect(self.update_result)

    def update_result(self, text):
        "update calculator display"
        self.display.setText(text)
