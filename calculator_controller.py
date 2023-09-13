"""calculate controller file"""
from shared import ArithOp
from calculator_model import CalculatorModel


class CalculatorController:
    """Controller for calculator"""

    def __init__(self, model: CalculatorModel):
        self.model = model

    def equal_clicked(self):
        """equal button clicked on calculator"""
        result = 0
        prev_operand = self.model.get_operand()
        new_operand = float(self.model.get_display())
        operation = self.model.get_operation()
        if operation == ArithOp.PLUS:
            result = prev_operand + new_operand
        elif operation == ArithOp.MINUS:
            result = prev_operand - new_operand
        elif operation == ArithOp.MULTIPLY:
            result = prev_operand * new_operand
        elif operation == ArithOp.DIVIDE:
            result = prev_operand / new_operand

        self.model.set_display(result)
        self.model.operation = ArithOp.NONE
        self.model.append_digit = False

    def c_clicked(self):
        """c button clicked on calculator"""
        self.model.set_operand(0)
        self.model.set_display("0")
        self.model.append_digit = False

    def operation_clicked(self, arith_op):
        """an arithmetic operation button clicked"""
        def handle_operation():
            self.model.set_operation(arith_op)
            self.model.set_operand(float(self.model.get_display()))
            self.model.append_digit = False
        return handle_operation

    def digit_click_factory(self, digit):
        """digit button clicked on calculator"""
        def digit_clicked():
            final_digits = digit
            if self.model.append_digit:
                operand = self.model.get_display()
                operand = str(operand) + digit
                final_digits = int(operand)
            self.model.set_display(f"{final_digits}")
            self.model.append_digit = True
        return digit_clicked
