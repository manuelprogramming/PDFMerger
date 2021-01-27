from Splitter import Splitter
from Merger import Merger

class EventHandler:
    def __init__(self, app):
        self.app = app

    def connectButtons(self):
        self.app.load_button.clicked.connect(self.openFileNamesDialog)
        self.app.action_button.clicked.connect(self.mergePDF)
        self.app.radioButton_split.clicked.connect(self.setSplitMode)
        self.app.radioButton_merge.clicked.connect(self.setMergeMode)
        self.app.save_button.clicked.connect(self.saveFileDialog)
        self.app.actionexit_2.triggered.connect(self.endProgramm)
        self.app.delete_all_files_button.clicked.connect(self.clearFiles)
        self.app.delete_selected_file_button.clicked.connect(self.clearSelectedFile)

    def endProgramm(self):
        self.app.exit()

    def clearFiles(self):
        self.app.pdf_list.clear()
        self.current_files = []
        self.app.process_label.setText("All Files have been deleted")

    def clearSelectedFile(self):
        for item in self.app.pdf_list.selectedItems():
            row = self.app.pdf_list.row(item)
            self.app.pdf_list.takeItem(row)
            self.current_files.remove(item.text())
        self.app.process_label.setText("Selected Files have been removed")

    def setSplitMode(self):
        self.app.process_label.setText("Operating in Split Mode")
        self.app.action_button.setText("Split")
        self.app.action_button.clicked.disconnect()
        self.app.action_button.clicked.connect(self.splitPDF)
        self.app.save_button.setDisabled(True)

    def setMergeMode(self):
        self.app.process_label.setText("Operating in Merge Mode")
        self.app.action_button.setText("Merge")
        self.app.action_button.clicked.disconnect()
        self.app.action_button.clicked.connect(self.mergePDF)
        self.app.save_button.setDisabled(False)

    def mergePDF(self):
        self.app.current_tool = Merger(self.app)
        self.app.current_tool.mergePDF()

    def splitPDF(self):
        self.app.current_tool = Splitter(self.app)
        self.app.current_tool.splitPDF()

    def saveFileDialog(self):
        self.app.current_tool.saveFileDialog()

    def openFileNamesDialog(self):
        self.app.current_tool.openFileNamesDialog()
