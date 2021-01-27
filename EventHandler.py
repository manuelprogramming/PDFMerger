from Splitter import Splitter
from Merger import Merger
from Converter import Converter


class EventHandler:
    def __init__(self, pdfmerger):
        self.pdfmerger = pdfmerger

    def connectButtons(self):
        self._connectMenuBar()
        self._connectButtons()
        self._connectRadioButtons()

    def _connectMenuBar(self):
        self.pdfmerger.actionexit_2.triggered.connect(self.endProgramm)
        self.pdfmerger.actionMerge.triggered.connect(self.setMergeMode)
        self.pdfmerger.actionSplit.triggered.connect(self.setSplitMode)
        self.pdfmerger.actionImage.triggered.connect(self.setImageConvertMode)



    def _connectRadioButtons(self):
        self.pdfmerger.radioButton_split.clicked.connect(self.setSplitMode)
        self.pdfmerger.radioButton_merge.clicked.connect(self.setMergeMode)

    def _connectButtons(self):
        self.pdfmerger.load_button.clicked.connect(self.openFileNamesDialog)
        self.pdfmerger.action_button.clicked.connect(self.mergePDF)
        self.pdfmerger.save_button.clicked.connect(self.saveFileDialog)
        self.pdfmerger.delete_all_files_button.clicked.connect(self.clearFiles)
        self.pdfmerger.delete_selected_file_button.clicked.connect(self.clearSelectedFile)

    def endProgramm(self):
        self.pdfmerger.exit()

    def clearFiles(self):
        self.pdfmerger.clearFiles()

    def clearSelectedFile(self):
        self.pdfmerger.clearSelectedFile()

    def setSplitMode(self):
        self.pdfmerger.setSplitMode()
        self.pdfmerger.action_button.clicked.connect(self.splitPDF)

    def setMergeMode(self):
        self.pdfmerger.setMergeMode()
        self.pdfmerger.action_button.clicked.connect(self.mergePDF)

    def setImageConvertMode(self):
        self.pdfmerger.setImageConvertMode()
        self.pdfmerger.action_button.clicked.connect(self.convert)

    def mergePDF(self):
        self.pdfmerger.current_tool.mergePDF()

    def splitPDF(self):
        self.pdfmerger.current_tool.splitPDF()

    def convert(self):
        self.pdfmerger.current_tool.convert()

    def saveFileDialog(self):
        self.pdfmerger.current_tool.saveFile()

    def openFileNamesDialog(self):
        self.pdfmerger.current_tool.openFileNamesDialog()
