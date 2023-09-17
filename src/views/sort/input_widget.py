from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QValidator, QRegularExpressionValidator

from src.views.widgets import LineEdit
from src.views.widgets.textarea import TextArea


# class ArrayValidator(QValidator):
#     def __init__(self, parent):
#         super().__init__(parent)
#
#     def validate(self, string: str | None, pos: int) -> tuple['QValidator.State', str, int]:
#         _ = string.replace(" ", "").split(",")
#         response_str = ", ".join(_)
#
#         print(_)
#         for substr in _:
#             if (not substr.isdigit() or ",," in string.replace(" ", "")) and substr != "":
#                 return QValidator.State.Invalid, response_str, pos
#
#         return QValidator.State.Acceptable, response_str, pos
#

class ArrayValidator(QValidator):
    def __init__(self, parent):
        super().__init__(parent)

    def validate(self, string: str | None, pos: int) -> tuple['QValidator.State', str, int]:
        _ = string.replace(" ", "")[1:-1].split(",")
        print(_)
        for substr in _:
            if substr.startswith("-"):
                substr = substr[1:]

            if not substr.isdigit() and substr != '':
                return QValidator.State.Invalid, string, pos

        return QValidator.State.Acceptable, string, pos


def dynamic_array_mask(array_size: int, max_length: int = 12) -> str:
    return "\\{" + f"{'X' * max_length}\\, " * (array_size - 1) + f"{'X' * max_length}" + "\\}"


class InputArray(LineEdit):

    def __init__(self, selection_color, primary_text_color, hover_color, third_background_color):
        super().__init__(selection_color, primary_text_color, hover_color, third_background_color)
        self.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDate)
        self.setInputMask(dynamic_array_mask(10))
        self.setValidator(ArrayValidator(self))

    def array(self) -> list[int]:
        return [int(x) for x in self.text().replace(" ", "")[1:-1].split(",") if x != ""]

    def set_array(self, array: list[int]):
        self.setText(f"{{{', '.join([str(x) for x in array])}}}")

    def update_mask(self, length: int, max_length: int = 12):
        self.setInputMask(dynamic_array_mask(length))

