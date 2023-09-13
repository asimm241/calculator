"""Shared file: this will include all classes and function
 that different component share"""

from enum import Enum

class ArithOp(Enum):
    """Operations"""
    PLUS = "+"
    MINUS = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
    NONE = ""
