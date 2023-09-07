from PyQt6 import QtCore, QtWidgets

from src.views.widgets import WidgetsFactory


class UiMergeSort:
    def setup_ui(self, merge_sort: QtWidgets.QWidget, theme_class, widgets_factory: WidgetsFactory):
        merge_sort.setObjectName("merge_sort")
        merge_sort_layout = QtWidgets.QVBoxLayout(merge_sort)
        merge_sort_layout.setContentsMargins(0, 0, 0, 0)
        merge_sort_layout.setSpacing(0)

        customize_sheet = QtWidgets.QWidget(merge_sort)
        customize_sheet.setObjectName("customize_sheet")
        customize_sheet.setStyleSheet("""
            QWidget#customize_sheet {
                background-color: $BG3;
            }
        """.replace(
            "$BG3", theme_class.third_background)
        )
        merge_sort_layout.addWidget(customize_sheet)

        central_layout = QtWidgets.QVBoxLayout(customize_sheet)
        central_layout.setContentsMargins(20, 20, 20, 20)
        central_layout.setSpacing(10)
        central_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)

        # Change Theme
        # ch_theme_layout = QtWidgets.QVBoxLayout()
        # ch_theme_layout.setContentsMargins(0, 0, 0, 0)
        # ch_theme_layout.setSpacing(10)
        #
        # ch_theme_header = widgets_factory.heading3(parent=merge_sort)
        # ch_theme_header.setObjectName("ch_theme_header")
        # ch_theme_layout.addWidget(ch_theme_header)
        # self.ch_theme_header = ch_theme_header
        #
        # ch_color_theme_widget = widgets_factory.combo_box(parent=merge_sort)
        # ch_color_theme_widget.setObjectName("ch_color_theme_widget")
        # ch_theme_layout.addWidget(ch_color_theme_widget)
        # self.ch_color_theme_widget = ch_color_theme_widget
        #
        # central_layout.addLayout(ch_theme_layout)

        self.translate_ui(merge_sort)
        QtCore.QMetaObject.connectSlotsByName(merge_sort)

    def translate_ui(self, merge_sort: QtWidgets.QWidget):
        _translate = QtCore.QCoreApplication.translate
