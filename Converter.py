from Tool import Tool
from PIL import Image
import os
from HelpingFunction import *
from Settings import *


class SavingFileError:
    pass


class ConversionError:
    pass


class Converter(Tool):
    def __init__(self, pdfmerger):
        super().__init__(pdfmerger)

        self.pdfmerger = pdfmerger
        self.current_dir = os.path.dirname(__file__)
        self.file_handler = pdfmerger.file_handler
        self.created_files = []
        self.process_label = pdfmerger.process_label

    def getConversionMode(self):
        return self.pdfmerger.comboBox_conversion_type.currentText()

    @tryThis
    def convert(self):
        if self._itemListIsNotEmpty():
            self._openAndConvertImages()
            self.process_label.setText("File succesfully converted. Press Save for saving your file")
        else:
            self.process_label.setText("No items to convert, load Items to list")

    def _openAndConvertImages(self):
        for file in self.file_handler.current_files:
            r_img = Image.open(file)
            r_img = r_img.convert(self.getConversionMode())
            self.created_files.append(r_img)

    def _itemListIsNotEmpty(self):
        return self.pdfmerger.item_list.count() != 0

    @tryThis
    def saveFile(self):
        filepath = self.saveFileDialog()
        if filepath:
            self._createPathAndSaveToPath(filepath)
            self._displaySuccesSavedMessage(filepath)

    def _createPathAndSaveToPath(self, filepath):
        if self._oneCreatedFile():
            self._saveToPath(filepath)
        else:
            self._saveToNumberedPath(filepath)

    def _saveToPath(self, filepath):
        file = self.created_files[0]
        file.save(filepath)

    def _saveToNumberedPath(self, filepath):
        saving_format = self._getFormatToSaveTo()
        for i, file in enumerate(self.created_files):
            rpath = createSplitFilename(filepath, i, saving_format)
            file.save(rpath)

    def _oneCreatedFile(self):
        return len(self.created_files) == 1

    def _getFormatToSaveTo(self):
        return self.pdfmerger.comboBox_convert_to.currentText()

    def _displaySuccesSavedMessage(self, filepath):
        self.process_label.setText(f"File saved succesfully to \n{filepath}")

    def _displayFailedSavedMessage(self):
        self.process_label.setText(f"Unable to save the File")


if __name__ == '__main__':

    img = Image.open("testfolder/Aufgabe 5.jpg")
    for item in conversion:
        pdf = img.convert(item)
        print("successful ", item)
        # pdf.save("testfolder/test.pdf")
