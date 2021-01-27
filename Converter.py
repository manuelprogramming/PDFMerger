from Tool import Tool
from PIL import Image
import os
from HelpingFunction import *
from Settings import *


class SavingFileError:
    pass

class ConvertingError:
    pass

class Converter(Tool):
    def __init__(self, pdfmerger):
        super().__init__(pdfmerger)

        self.pdfmerger = pdfmerger
        self.current_dir = os.path.dirname(__file__)
        self.current_files = []

    def getConversionMode(self):
        return self.pdfmerger.comboBox_convert_from.currentText()

    def convert(self):
        try:
            if self._itemListIsNotEmpty():
                self._openAndConvertImages()
                self.pdfmerger.process_label.setText("File succesfully converted. Press Save for saving your file")
            else:
                self.pdfmerger.process_label.setText("No items to convert, load Items to list")
        except ConvertingError:
            self.pdfmerger.process_label.setText("Failed to Convert File")


    def _openAndConvertImages(self):
        for file in self.pdfmerger.current_files:
            img = Image.open(file)
            self.current_files.append(img.convert(self.getConversionMode()))

    def _itemListIsNotEmpty(self):
        return self.pdfmerger.item_list.count() != 0

    def saveFile(self):
        try:
            filepath = self.saveFileDialog()
            if filepath:
                self._createPathAndSaveToPath(filepath)
                self._displaySuccesSavedMessage(filepath)
        except SavingFileError:
            self._displayFailedSavedMessage()

    def _createPathAndSaveToPath(self, filepath):
        saving_format = self._getFormatToSaveTo()
        if len(self.current_files) == 1:
            file = self.current_files[0]
            file.save(filepath)
        else:
            for i, file in enumerate(self.current_files):
                rpath = createSplitFilename(filepath, i, saving_format)
                file.save(rpath)

    def _getFormatToSaveTo(self):
        return self.pdfmerger.comboBox_convert_to.currentText()

    def _displaySuccesSavedMessage(self, filepath):
        self.pdfmerger.process_label.setText(f"File saved succesfully to \n{filepath}")

    def _displayFailedSavedMessage(self):
        self.pdfmerger.process_label.setText(f"Unable to save the File")


if __name__ == '__main__':

    img = Image.open("testfolder/Aufgabe 5.jpg")
    for item in conversion:
        pdf = img.convert(item)
        print("successful ", item)
        # pdf.save("testfolder/test.pdf")
