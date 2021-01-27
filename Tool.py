from PyQt5.QtWidgets import QFileDialog, QErrorMessage
from Settings import *
import os


class Tool:
    def __init__(self, pdfmerger):
        self.pdfmerger = pdfmerger
        self.mode_dict = modes[self.pdfmerger.current_mode]


    def openFileNamesDialog(self):
        filestring = self._createOpenFileString()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        opened_files, _ = QFileDialog.getOpenFileNames(self.pdfmerger,"Open File", "*.*", filestring, options=options)
        if opened_files:
            self.saveOpenedFilesInList(opened_files)

    def _createOpenFileString(self):
        if self.pdfmerger.current_mode == "Convert":
            type_string = "All Files (*);"
            for key in self.mode_dict.keys():
                type_string = type_string + f";;{key} Files "
                for type in self.mode_dict[key]:
                    type_string = type_string + f"(*{type})"
            return type_string
        else:
            return pdf_file_type_string

    def _createSaveFileString(self):
        if self.pdfmerger.current_mode == "Convert":
            current_format = self.pdfmerger.comboBox_convert_to.currentText()
            files_type_string = f"All Files (*);;{current_format} Files (*{current_format})"
            files_name_string = f"*{current_format}"
            return files_name_string, files_type_string
        else:
            return pdf_file_name_string, pdf_file_type_string


    def saveFileDialog(self):
        namestring, typestring = self._createSaveFileString()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self.pdfmerger, "Save File", namestring,
                                                  typestring, options=options)
        return fileName

    def saveOpenedFilesInList(self, opened_files):
        self.checkIfFilesAreValidTypeAndAppendToCurrentFiles(opened_files)
        self.pdfmerger.item_list.addItems(self.pdfmerger.current_files)

    def checkIfFilesAreValidTypeAndAppendToCurrentFiles(self, opened_files):
        self.getValidTypes()
        for file in opened_files:
            if not self.fileIsValidType(file):
                self.displayFileError(file)
            else:
                self.pdfmerger.current_files.append(file)

    def _setModeDict(self):
        self.mode_dict = modes[self.pdfmerger.current_mode]

    def getValidTypes(self):
        self.valid_types = []
        for key in self.mode_dict:
            [self.valid_types.append(x) for x in self.mode_dict[key]]


    def fileIsValidType(self, file):
        is_valid = any([file.find(sub) > 0 for sub in self.valid_types])
        print(any([file.find(sub) > 0 for sub in self.valid_types]))
        return is_valid

    def displayFileError(self, file):
        errordialog = QErrorMessage(self.pdfmerger)
        file = os.path.basename(file)
        errordialog.showMessage(f"{file}\n has not a valid format.\n"
                                f"For {self.pdfmerger.current_mode} Mode supported formats are {self.valid_types} Files "
                                , file)
        errordialog.setWindowTitle("File Error")


if __name__ == '__main__':
    tool = Tool()
    tool.mode_dict = modes["Split"]
    tool.getValidTypes()
    print(tool.valid_types)
    dastring= "C:/Users/profm/PycharmProjects/PDFMerger/EventHandler.py"
    print("isvalid:", tool.fileIsValidType(dastring))
    # print(dastring.find(".py"))
