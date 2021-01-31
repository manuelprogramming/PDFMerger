from PyQt5 import QtWidgets, QtCore, QtGui
from PDFMergerUI import Ui_PDFMergerUI
from Splitter import Splitter
from Merger import Merger
from Converter import Converter
from EventHandler import EventHandler
from ModeSelector import ModeSelector
from FileHandler import FileHandler
import os
from Settings import *
from HelpingFunction import *




class PDFMerger(QtWidgets.QMainWindow, Ui_PDFMergerUI):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setupUi(self)
        self.show()

        self.current_dir = os.path.dirname(__file__)
        self.mode_selector = ModeSelector(self)
        self.file_handler = FileHandler(self.process_label, self.item_list)
        self.event_handler = EventHandler(self)
        self.current_tool = Merger(self)

        self.setupProgramm()

    def setupProgramm(self):
        self.event_handler.connectButtons()
        self.setupConverterWidgets()
        self._setFixedWindowSize()
        self._setupStyling()
        self._setupIcon()


    def _setFixedWindowSize(self):
        self.setFixedSize(self.size())

    def hideRadioButtons(self):
        self.radioButton_merge.hide()
        self.radioButton_split.hide()

    def showRadioButtons(self):
        self.radioButton_merge.show()
        self.radioButton_split.show()

    def setupConverterWidgets(self):
        self._createConvertModeWidgets()
        self._addConvertWidgetsToModeLayout()
        self._addItemsToComboBoxes()
        self.hideConverterWidgets()

    def hideConverterWidgets(self):
        [widget.hide() for widget in self.convertWidgets]

    def showConverterWidgets(self):
        [widget.show() for widget in self.convertWidgets]

    def _createConvertModeWidgets(self):
        self.label_convert_as = QtWidgets.QLabel("Conversion Mode:")
        self.comboBox_convert_to = QtWidgets.QComboBox()
        self.label_convert_to = QtWidgets.QLabel("saving files to")
        self.comboBox_conversion_type = QtWidgets.QComboBox()
        self.label_file = QtWidgets.QLabel("File")

        self.convertWidgets = [self.label_convert_as, self.comboBox_conversion_type, self.label_convert_to,
                               self.comboBox_convert_to, self.label_file]

        self.comboBox_conversion_type.currentText()

    def _addConvertWidgetsToModeLayout(self):
        [self.horizontalLayout_mode.addWidget(widget) for widget in self.convertWidgets]

    def _addItemsToComboBoxes(self):
        self.comboBox_convert_to.addItem(".pdf")
        self._addItemsFromSupportedFormats()

    def _addItemsFromSupportedFormats(self):
        for item in supportedImageFormats:
            for img_format in supportedImageFormats[item]:
                self.comboBox_convert_to.addItem(img_format)

        for item in conversion:
            self.comboBox_conversion_type.addItem(item)

    @TryFileLoading
    def _setupStyling(self):
        style_sheet_path = os.path.join(self.current_dir, "UIs/QDarkOrangeTheme.css")
        self.setStyleSheet(open(style_sheet_path).read())
        self.process_label.setText("Operating in Merge Mode")

    @TryFileLoading
    def _setupIcon(self):
        window_icon_path = os.path.join(self.current_dir, "UIs/Icon_PDF.png")
        icon = QtGui.QIcon(QtGui.QPixmap(window_icon_path))
        self.setWindowIcon(icon)

    # Delete Files
    def clearFiles(self):
        self.file_handler.clearFiles()

    def clearSelectedFile(self):
        self.file_handler.clearSelectedFile()

    # Mode Selector

    def setSplitMode(self):
        self.mode_selector.setSplitMode()
        self.current_tool = Splitter(self)

    def setMergeMode(self):
        self.mode_selector.setMergeMode()
        self.current_tool = Merger(self)

    def setImageConvertMode(self):
        self.mode_selector.setImageConvertMode()
        self.current_tool = Converter(self)
