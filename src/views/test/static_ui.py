from PyQt6 import QtCore, QtWidgets
from src.views.widgets import WidgetsFactory


class UiTest:
    def setup_ui(self, test: QtWidgets.QWidget, theme_class, widgets_factory: WidgetsFactory):
        test.setObjectName("test")
        test_layout = QtWidgets.QVBoxLayout(test)
        test_layout.setContentsMargins(0, 0, 0, 0)
        test_layout.setSpacing(0)

        customize_sheet = QtWidgets.QWidget(test)
        customize_sheet.setObjectName("customize_sheet")
        customize_sheet.setStyleSheet("""
            QWidget#customize_sheet {
                background-color: $BG3;
            }
        """.replace(
            "$BG3", theme_class.third_background)
        )
        test_layout.addWidget(customize_sheet)

        central_layout = QtWidgets.QVBoxLayout(customize_sheet)
        central_layout.setContentsMargins(20, 20, 20, 20)
        central_layout.setSpacing(10)
        central_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)

        test_layout = QtWidgets.QVBoxLayout()
        test_layout.setContentsMargins(0, 0, 0, 0)
        test_layout.setSpacing(10)

        test_header = widgets_factory.heading2(parent=test)
        test_header.setObjectName("test_header")
        test_layout.addWidget(test_header)
        self.test_header = test_header

        # Input


        self.translate_ui(test)
        QtCore.QMetaObject.connectSlotsByName(test)

    def translate_ui(self, test: QtWidgets.QWidget):
        _translate = QtCore.QCoreApplication.translate
