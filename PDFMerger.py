from PyQt5 import QtWidgets, QtCore, QtGui
from PDFMergerUI import Ui_PDFMergerUI
from Splitter import Splitter
from Merger import Merger
from Converter import Converter
from EventHandler import EventHandler
import os
from Settings import *



class PDFMerger(QtWidgets.QMainWindow, Ui_PDFMergerUI):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setupUi(self)
        self.show()

        self.current_dir = os.path.dirname(__file__)
        self.current_mode = "Merge"
        self.event_handler = EventHandler(self)
        self.current_tool = Merger(self)
        self.current_files = []
        self.setupProgramm()

    def setupProgramm(self):
        self.event_handler.connectButtons()
        self.setupConverterWidgets()
        self._setFixedWindowSize()
        self._setupStyling()
        self._setupIcon()


    def _setFixedWindowSize(self):
        self.setFixedSize(self.size())

    def _hideRadioButtons(self):
        self.radioButton_merge.hide()
        self.radioButton_split.hide()

    def _showRadioButtons(self):
        self.radioButton_merge.show()
        self.radioButton_split.show()

    def setupConverterWidgets(self):
        self._createConvertModeWidgets()
        self._addConvertWidgetsToModeLayout()
        self._addItemsToComboBoxes()
        self._hideConverterWidgets()

    def _hideConverterWidgets(self):
        [widget.hide() for widget in self.convertWidgets]

    def _showConverterWidgets(self):
        [widget.show() for widget in self.convertWidgets]

    def _createConvertModeWidgets(self):
        self.label_convert_as = QtWidgets.QLabel("Conversion Mode:")
        self.comboBox_convert_to = QtWidgets.QComboBox()
        self.label_convert_to = QtWidgets.QLabel("saving files to")
        self.comboBox_convert_from = QtWidgets.QComboBox()
        self.label_file = QtWidgets.QLabel("File")

        self.convertWidgets = [self.label_convert_as, self.comboBox_convert_from, self.label_convert_to,
                               self.comboBox_convert_to, self.label_file]

        self.comboBox_convert_from.currentText()


    def _addConvertWidgetsToModeLayout(self):
        [self.horizontalLayout_mode.addWidget(widget) for widget in self.convertWidgets]

    def _addItemsToComboBoxes(self):
        self.comboBox_convert_to.addItem(".pdf")
        self._addItemsFromSupportedFormats()



    def _addItemsFromSupportedFormats(self):
        for item in supportedImageFormats:
            for format in supportedImageFormats[item]:
                self.comboBox_convert_to.addItem(format)

        for item in conversion:
            self.comboBox_convert_from.addItem(item)

    def _setupStyling(self):
        style_sheet_path = os.path.join(self.current_dir, "UIs/QDarkOrangeTheme.css")
        self.setStyleSheet(open(style_sheet_path).read())
        self.process_label.setText("Operating in Merge Mode")

    def _setupIcon(self):
        window_icon_path = os.path.join(self.current_dir, "UIs/Icon_PDF.png")
        icon = QtGui.QIcon(QtGui.QPixmap(window_icon_path))
        self.setWindowIcon(icon)

    # Delete Files
    def clearFiles(self):
        self.item_list.clear()
        self.current_files = []
        self.process_label.setText("All Files have been deleted")

    def clearSelectedFile(self):
        for item in self.item_list.selectedItems():
            self._takeItemFromList(item)
        self.process_label.setText("Selected Files have been removed")

    def _takeItemFromList(self, item):
        row = self.item_list.row(item)
        self.item_list.takeItem(row)
        self.current_files.remove(item.text())

    # Mode Setter

    def _setupModeChange(self):
        self._showRadioButtons()
        self._hideConverterWidgets()
        self.action_button.clicked.disconnect()

        self.process_label.setText(f"Operating in {self.current_mode} Mode")
        self.action_button.setText(self.current_mode)

    def setSplitMode(self):
        self.current_mode = "Split"
        self._setupModeChange()
        self.radioButton_split.setChecked(True)
        self.save_button.setDisabled(True)

        self.current_tool = Splitter(self)

    def setMergeMode(self):
        self._setupModeChange()
        self.radioButton_merge.setChecked(True)
        self.save_button.setDisabled(False)

        self.current_tool = Merger(self)

    def setImageConvertMode(self):
        self.current_mode = "Convert"
        self._setupModeChange()
        self._hideRadioButtons()
        self._showConverterWidgets()
        self.save_button.setDisabled(False)

        self.current_tool = Converter(self)
