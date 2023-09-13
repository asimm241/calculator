"""Model for calculator"""
from PySide6.QtCore import Signal, QObject
from shared import ArithOp


class CalculatorModel(QObject):
    """calculator model"""
    _display_text = Signal(str, name="result_text")
    _display_text_value = "0"

    def __init__(self):
        super(CalculatorModel, self).__init__()
        self._operand = 0
        self.operation = ArithOp.NONE
        self.append_digit = False

    def set_display(self, value):
        """set result text"""
        displayed_value = float(value)
        if displayed_value.is_integer():
            displayed_value = int(value)
        self._display_text_value = displayed_value
        self._display_text.emit(str(displayed_value))

    def get_display(self):
        "get result text"
        return self._display_text_value

    def get_operand(self):
        """get operand if not set return 0"""
        return self._operand

    def set_operand(self, value):
        """set operand"""
        self._operand = value

    def set_operation(self, operation):
        """set operation"""
        self.operation = operation

    def get_operation(self):
        """get operation"""
        return self.operation.value
