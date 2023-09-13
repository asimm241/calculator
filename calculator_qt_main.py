"""Qt calculator"""
import sys
from PySide6 import  QtWidgets

import calculator_view
import calculator_controller
import  calculator_model

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    model = calculator_model.CalculatorModel()
    controller = calculator_controller.CalculatorController(model)
    widget = calculator_view.Calculator(model, controller)
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
