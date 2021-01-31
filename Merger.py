from PyQt5.QtWidgets import QFileDialog, QApplication
from PyPDF2 import PdfFileReader, PdfFileWriter
from Tool import Tool
from HelpingFunction import *


class Merger(Tool):
    def __init__(self, pdfmerger):
        super().__init__(pdfmerger)
        self.pdfmerger = pdfmerger
        self.pdf_writer = PdfFileWriter()
        self.file_handler = pdfmerger.file_handler
        self.process_label = pdfmerger.process_label

    @tryThis
    def mergePDF(self):
        for file in self.file_handler.current_files:
            pdf_reader = PdfFileReader(file)
            for page in range(pdf_reader.getNumPages()):
                self.pdf_writer.addPage(pdf_reader.getPage(page))

        self.displaySucessfullCreationMessage()

    def saveFile(self):
        file_name = self.saveFileDialog()
        if file_name:
            self._saveFileAndShowSuccessMessage(file_name)

    def _saveFileAndShowSuccessMessage(self, file_name):
        with open(file_name, "wb") as out:
            self.pdf_writer.write(out)
            self.process_label.setText(f"PDF-File successfully saved as \n{file_name}")

    def displaySucessfullCreationMessage(self):
        if self.file_handler.current_files:
            self.process_label.setText("PDF File created successfully. Press Save for saving your file")
