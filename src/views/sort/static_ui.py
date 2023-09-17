from PyQt6 import QtCore, QtWidgets, QtGui

from src.views.sort.input_widget import InputArray
from src.views.widgets import WidgetsFactory


class UiSort:
    def setup_ui(self, sort: QtWidgets.QWidget, theme_class, widgets_factory: WidgetsFactory):
        sort.setObjectName("sort")
        sort_layout = QtWidgets.QVBoxLayout(sort)
        sort_layout.setContentsMargins(0, 0, 0, 0)
        sort_layout.setSpacing(0)

        customize_sheet = QtWidgets.QWidget(sort)
        customize_sheet.setObjectName("customize_sheet")
        customize_sheet.setStyleSheet("""
            QWidget#customize_sheet {
                background-color: $BG3;
            }
        """.replace(
            "$BG3", theme_class.third_background)
        )
        sort_layout.addWidget(customize_sheet)

        central_layout = QtWidgets.QVBoxLayout(customize_sheet)
        central_layout.setContentsMargins(20, 20, 20, 20)
        central_layout.setSpacing(10)
        central_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)

        sort_layout = QtWidgets.QVBoxLayout()
        sort_layout.setContentsMargins(0, 0, 0, 0)
        sort_layout.setSpacing(10)

        sort_header = widgets_factory.heading2(parent=sort)
        sort_header.setObjectName("sort_header")
        sort_layout.addWidget(sort_header)
        self.sort_header = sort_header

        # Input

        input_header = widgets_factory.heading3(parent=sort)
        input_header.setObjectName("input_header")
        sort_layout.addWidget(input_header)
        self.input_header = input_header

        input_layout = QtWidgets.QVBoxLayout()
        input_layout.setContentsMargins(0, 0, 0, 0)
        input_layout.setSpacing(10)
        sort_layout.addLayout(input_layout)

        line_widget = InputArray(
            selection_color=theme_class.selection,
            primary_text_color=theme_class.text_primary,
            hover_color=theme_class.hover,
            third_background_color=theme_class.third_background
        )
        line_widget.setObjectName("line_widget")
        line_widget.setMaximumHeight(100)
        input_layout.addWidget(line_widget)

        self.line_widget = line_widget

        # ---> Tools
        tools_layout = QtWidgets.QHBoxLayout()
        tools_layout.setContentsMargins(0, 0, 0, 0)
        tools_layout.setSpacing(10)
        tools_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        tools_layout.addStretch(1)
        input_layout.addLayout(tools_layout)

        length_per_item = widgets_factory.line_edit()
        length_per_item.setObjectName("length_per_item")
        length_per_item.setMaximumWidth(130)
        length_per_item.setToolTip("Длина элемента списка")
        length_per_item.setValidator(
            QtGui.QIntValidator(1, 100000000, parent=length_per_item)
        )
        length_per_item.set_required(True)
        self.length_per_item = length_per_item

        tools_layout.addWidget(length_per_item)

        length_line_widget = widgets_factory.line_edit()
        length_line_widget.setObjectName("length_line_widget")
        length_line_widget.setMaximumWidth(80)
        length_line_widget.setToolTip("Длина списка")
        length_line_widget.setValidator(
            QtGui.QIntValidator(1, 1000000000, parent=length_line_widget)
        )
        length_line_widget.set_required(True)

        tools_layout.addWidget(length_line_widget)
        self.length_line_widget = length_line_widget

        generate_button = widgets_factory.button(parent=sort)
        generate_button.setObjectName("generate_button")
        tools_layout.addWidget(generate_button)
        self.generate_button = generate_button

        # Output

        output_header = widgets_factory.heading3(parent=sort)
        output_header.setObjectName("output_header")
        sort_layout.addWidget(output_header)
        self.output_header = output_header

        output_widget = widgets_factory.textarea()
        output_widget.setObjectName("output_widget")
        output_widget.setReadOnly(True)
        output_widget.setPlaceholderText("Отсортированный список")
        sort_layout.addWidget(output_widget)

        central_layout.addLayout(sort_layout)
        self.translate_ui(sort)
        QtCore.QMetaObject.connectSlotsByName(sort)

    def translate_ui(self, sort: QtWidgets.QWidget):
        _translate = QtCore.QCoreApplication.translate
        self.sort_header.setText(
            _translate("sort_header", "Сортировка Обменом")
        )
        self.input_header.setText(
            _translate("input_header", "Ввод")
        )
        self.output_header.setText(
            _translate("output_header", "Вывод")
        )
        self.line_widget.setPlaceholderText(
            _translate("line_widget", "Введите список")
        )
        self.generate_button.setText(
            _translate("generate_button", "Сгенерировать")
        )
        self.length_per_item.setPlaceholderText(
            _translate("length_per_item", "Длина элемента")
        )
        self.length_line_widget.setPlaceholderText(
            _translate("length_line_widget", "Длина")
        )
