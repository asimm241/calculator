from enum import Enum
from PySide6 import QtCore, QtWidgets
from calculator_controller import CalculatorController
from calculator_model import CalculatorModel


class ArithOp(Enum):
    """Operations"""
    PLUS = "+"
    MINUS = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
    NONE = ""


class Calculator(QtWidgets.QWidget):
    """This widget is a calculator"""

    def __init__(self):
        super().__init__()

        # self.result = 0
        # self.operation = ArithOp.NONE
        # self.append_digit = False
        self.digits_buttons = []
        self._model = CalculatorModel()
        self._controller = CalculatorController(self._model)

        self.plus_btn = QtWidgets.QPushButton("+")
        self.minus_btn = QtWidgets.QPushButton("-")
        self.multi_btn = QtWidgets.QPushButton("*")
        self.divide_btn = QtWidgets.QPushButton("/")
        self.equal_btn = QtWidgets.QPushButton("=")
        self.c_btn = QtWidgets.QPushButton("C")

        for i in range(0, 10):
            self.digits_buttons.append(QtWidgets.QPushButton(str(i)))

        # self.zero_btn = QtWidgets.QPushButton("0")
        # self.one_btn = QtWidgets.QPushButton("1")
        # self.two_btn = QtWidgets.QPushButton("2")
        # self.three_btn = QtWidgets.QPushButton("3")
        # self.four_btn = QtWidgets.QPushButton("4")
        # self.five_btn = QtWidgets.QPushButton("5")
        # self.six_btn = QtWidgets.QPushButton("6")
        # self.seven_btn = QtWidgets.QPushButton("7")
        # self.eight_btn = QtWidgets.QPushButton("8")
        # self.nine_btn = QtWidgets.QPushButton("9")

        self.display = QtWidgets.QLabel(
            "0", alignment=QtCore.Qt.AlignmentFlag.AlignRight)

        # self.layout = QtWidgets.QVBoxLayout(self)

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

        # self.zero_btn.clicked.connect(self.digit_click_factory("0"))
        # self.one_btn.clicked.connect(self.digit_click_factory("1"))
        # self.two_btn.clicked.connect(self.digit_click_factory("2"))
        # self.three_btn.clicked.connect(self.digit_click_factory("3"))
        # self.four_btn.clicked.connect(self.digit_click_factory("4"))
        # self.five_btn.clicked.connect(self.digit_click_factory("5"))
        # self.six_btn.clicked.connect(self.digit_click_factory("6"))
        # self.seven_btn.clicked.connect(self.digit_click_factory("7"))
        # self.eight_btn.clicked.connect(self.digit_click_factory("8"))
        # self.nine_btn.clicked.connect(self.digit_click_factory("9"))

    # def equal_clicked(self):
    #     """equal button clicked on calculator"""
    #     if self.operation == ArithOp.PLUS:
    #         self.result = self.result + float(self.result_txt.text())
    #     elif self.operation == ArithOp.MINUS:
    #         self.result = self.result - float(self.result_txt.text())
    #     elif self.operation == ArithOp.MULTIPLY:
    #         self.result = self.result * float(self.result_txt.text())
    #     elif self.operation == ArithOp.DIVIDE:
    #         self.result = self.result / float(self.result_txt.text())
    #     if self.result.is_integer():
    #         self.result_txt.setText(str(int(self.result)))
    #     else:
    #         self.result_txt.setText(str(self.result))
    #     self.operation = ArithOp.NONE
    #     self.append_digit = False

    # def c_clicked(self):
        # """c button clicked on calculator"""
        # self.result = 0
        # self.result_txt.setText(f"{self.result}")
        # self.append_digit = False

    # def operation_clicked(self, arith_op):
    #     """an arithmetic operation button clicked"""
    #     def handle_operation():
    #         self.operation = arith_op
    #         self.result = float(self.result_txt.text())
    #         self.append_digit = False
    #     return handle_operation

    def update_result(self, text):
        "update calculator display"
        self.display.setText(text)

    # def digit_click_factory(self, digit):
    #     """digit button clicked on calculator"""
    #     def digit_clicked():
    #         final_digits = digit
    #         if self.append_digit:
    #             operand = self.result_txt.text()
    #             operand = operand + digit
    #             final_digits = int(operand)
    #         self.result_txt.setText(f"{final_digits}")
    #         self.append_digit = True
    #     return digit_clicked
