from PyQt5 import QtWidgets, QtCore
from PDFMergerUI import Ui_PDFMergerUI
from Splitter import Splitter
from Merger import Merger


class PDFMerger(QtWidgets.QMainWindow, Ui_PDFMergerUI):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setupUi(self)
        self.show()

        self.current_tool = Merger(self)

        self.current_files = []
        self.setupProgramm()

    def setupProgramm(self):
        self.connectButtons()
        self.setFixedWindowSize()
        self.process_label.setText("Operating in Merge Mode")
        self.app.setStyle("Fusion")

    def setFixedWindowSize(self):
        self.setFixedSize(self.size())

    def connectButtons(self):
        self.load_button.clicked.connect(self.openFileNamesDialog)
        self.action_button.clicked.connect(self.mergePDF)
        self.radioButton_split.clicked.connect(self.setSplitMode)
        self.radioButton_merge.clicked.connect(self.setMergeMode)
        self.save_button.clicked.connect(self.saveFileDialog)
        self.actionexit_2.triggered.connect(self.endProgramm)
        self.delete_all_files_button.clicked.connect(self.clearFiles)
        self.delete_selected_file_button.clicked.connect(self.clearSelectedFile)

    def endProgramm(self):
        self.app.exit()

    def clearFiles(self):
        self.pdf_list.clear()
        self.current_files = []
        self.process_label.setText("All Files have been deleted")

    def clearSelectedFile(self):
        for item in self.pdf_list.selectedItems():
            row = self.pdf_list.row(item)
            self.pdf_list.takeItem(row)
            self.current_files.remove(item.text())
        self.process_label.setText("Selected Files have been removed")


    def setSplitMode(self):
        self.process_label.setText("Operating in Split Mode")
        self.action_button.setText("Split")
        self.action_button.clicked.disconnect()
        self.action_button.clicked.connect(self.splitPDF)
        self.save_button.setDisabled(True)

    def setMergeMode(self):
        self.process_label.setText("Operating in Merge Mode")
        self.action_button.setText("Merge")
        self.action_button.clicked.disconnect()
        self.action_button.clicked.connect(self.mergePDF)
        self.save_button.setDisabled(False)

    def mergePDF(self):
        self.current_tool = Merger(self)
        self.current_tool.mergePDF()

    def splitPDF(self):
        self.current_tool = Splitter(self)
        self.current_tool.splitPDF()

    def saveFileDialog(self):
        self.current_tool.saveFileDialog()

    def openFileNamesDialog(self):
        self.current_tool.openFileNamesDialog()
