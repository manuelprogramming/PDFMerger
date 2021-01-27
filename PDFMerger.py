from PyQt5 import QtWidgets, QtCore
from PDFMergerUI import Ui_PDFMergerUI
from Splitter import Splitter
from Merger import Merger
from EventHandler import EventHandler


class PDFMerger(QtWidgets.QMainWindow, Ui_PDFMergerUI):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setupUi(self)
        self.show()

        self.event_handler = EventHandler(self)
        self.current_tool = Merger(self)

        self.current_files = []
        self.setupProgramm()

    def setupProgramm(self):
        self.event_handler.connectButtons()
        self.setFixedWindowSize()
        self.setStyleSheet(open("QDarkOrangeTheme.css").read())
        self.process_label.setText("Operating in Merge Mode")
        self.app.setStyle("Fusion")

    def setFixedWindowSize(self):
        self.setFixedSize(self.size())


