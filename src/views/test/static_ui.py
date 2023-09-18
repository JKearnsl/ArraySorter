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

        # Header
        th_layout = QtWidgets.QHBoxLayout()
        th_layout.setContentsMargins(0, 0, 0, 0)
        th_layout.setSpacing(0)
        test_layout.addLayout(th_layout)

        test_header = widgets_factory.heading2(parent=test)
        test_header.setObjectName("test_header")
        th_layout.addWidget(test_header)
        self.test_header = test_header

        th_layout.addStretch(1)

        start_button = widgets_factory.button(parent=test)
        start_button.setObjectName("start_button")
        start_button.setMinimumWidth(100)
        self.start_button = start_button
        th_layout.addWidget(start_button)

        # Table
        table = widgets_factory.table(parent=test)
        table.setObjectName("table")
        table.setColumnCount(4)
        table.setRowCount(20)

        table.setHorizontalHeaderLabels([
            "Тип", "Время работы", "Кол-во эл.", "Случай"
        ])

        test_layout.addWidget(table)
        self.table = table

        central_layout.addLayout(test_layout)
        self.translate_ui(test)
        QtCore.QMetaObject.connectSlotsByName(test)

    def translate_ui(self, test: QtWidgets.QWidget):
        _translate = QtCore.QCoreApplication.translate
        self.start_button.setText(_translate("test", "Начать"))
