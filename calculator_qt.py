"""Qt calculator"""
import sys
from PySide6 import  QtWidgets
from enum import Enum
import calculator_view


class ArithOp(Enum):
    """Operations"""
    PLUS = "+"
    MINUS = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
    NONE = ""

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = calculator_view.Calculator()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
