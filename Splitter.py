from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog,QApplication
from PDFMergerUI import Ui_PDFMergerUI
from PyPDF2 import PdfFileReader, PdfFileWriter
from Tool import Tool
import os


class Splitter(Tool):
    def __init__(self, pdfmerger):
        super().__init__(pdfmerger)
        self.pdfmerger = pdfmerger

    def splitPDF(self):
        fileName = self.splitSaveFileDialog()
        if fileName:
            for file in self.pdfmerger.current_files:
                pdf_reader = PdfFileReader(file)
                self.createSplittedPDFs(pdf_reader, fileName)
        self.displaySuccesfullSplitedMessage()


    def createSplittedPDFs(self, pdf_reader, fileName):
        for i in range(pdf_reader.numPages):
            pdf_writer = PdfFileWriter()
            pdf_writer.addPage(pdf_reader.getPage(i))
            output_line = self.createSplitFilename(fileName, i)
            with open(output_line, "wb") as outputStream:
                pdf_writer.write(outputStream)


    def splitSaveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self.pdfmerger, "Save Splitted Files To?", "*.pdf", "All Files (*);;PDF Files (*.pdf)", options=options)
        return fileName

    @staticmethod
    def createSplitFilename(fileName, i):
        index = fileName.find('.pdf')
        output_line = fileName[:index] + str(i) + fileName[index:]
        return output_line

    def displaySuccesfullSplitedMessage(self):
        if self.pdfmerger.current_files:
            self.pdfmerger.process_label.setText("PDF-File successfully splited and saved to the selected Folder")