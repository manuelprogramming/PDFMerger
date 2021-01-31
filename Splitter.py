from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog, QApplication
from PDFMergerUI import Ui_PDFMergerUI
from PyPDF2 import PdfFileReader, PdfFileWriter
from Tool import Tool
import os
from HelpingFunction import *


class Splitter(Tool):
    def __init__(self, pdfmerger):
        super().__init__(pdfmerger)
        self.pdfmerger = pdfmerger
        self.file_handler = pdfmerger.file_handler

    @tryThis
    def splitPDF(self):
        fileName = self.splitSaveFileDialog()
        if fileName:
            for file in self.file_handler.current_files:
                self.createSplittedPDFs(file, fileName)
        self.displaySuccesfullSplitedMessage()

    def createSplittedPDFs(self, file, fileName):
        pdf_reader = PdfFileReader(file)
        for i in range(pdf_reader.numPages):
            pdf_writer = self._createWriterAndAddPage(pdf_reader, i)
            fileName = createSplitFilename(fileName, i, ".pdf")
            self._saveToFile(fileName, pdf_writer)

    @staticmethod
    def _createWriterAndAddPage(pdf_reader, i):
        pdf_writer = PdfFileWriter()
        return pdf_writer.addPage(pdf_reader.getPage(i))

    @staticmethod
    def _saveToFile(fileName, pdf_writer):
        with open(fileName, "wb") as outputStream:
            pdf_writer.write(outputStream)

    def splitSaveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self.pdfmerger, "Save Splitted Files To?", "*.pdf",
                                                  "All Files (*);;PDF Files (*.pdf)", options=options)
        return fileName

    def displaySuccesfullSplitedMessage(self):
        if self.file_handler.current_files:
            self.pdfmerger.process_label.setText("PDF-File successfully splited and saved to the selected Folder")
