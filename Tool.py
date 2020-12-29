from PyQt5.QtWidgets import QFileDialog, QErrorMessage


class Tool:
    def __init__(self, pdfmerger):
        self.pdfmerger = pdfmerger

    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        opened_files, _ = QFileDialog.getOpenFileNames(self.pdfmerger, "QFileDialog.getOpenFileNames()", "",
                                                       "All Files (*);;PDF Files (*.pdf)", options=options)
        if opened_files:
            self.saveOpenedFilesInList(opened_files)

    def saveOpenedFilesInList(self, opened_files):
        self.checkIfFilesAreValidTypeAndAppendToCurrentFiles(opened_files)
        self.pdfmerger.pdf_list.addItems(self.pdfmerger.current_files)

    def checkIfFilesAreValidTypeAndAppendToCurrentFiles(self, opened_files):
        for file in opened_files:
            if not self.fileIsValidType(file):
                self.displayFileError(file)
            else:
                self.pdfmerger.current_files.append(file)

    @staticmethod
    def fileIsValidType(file):
        if file.find(".pdf") == -1:
            return False
        else:
            return True

    def displayFileError(self, file):
        errordialog = QErrorMessage(self.pdfmerger)
        errordialog.showMessage(f"{file}\n is not a PDF File.\n"
                                f"Make sure you only load PDF Files", file)
        errordialog.setWindowTitle("File Error")
