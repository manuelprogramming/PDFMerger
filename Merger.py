from PyQt5.QtWidgets import QFileDialog,QApplication
from PyPDF2 import PdfFileReader, PdfFileWriter
from Tool import Tool

class Merger(Tool):
    def __init__(self,pdfmerger):
        super().__init__(pdfmerger)
        self.pdfmerger = pdfmerger
        self.pdf_writer = PdfFileWriter()

    def mergePDF(self):
        for file in self.pdfmerger.current_files:
            pdf_reader = PdfFileReader(file)
            for page in range(pdf_reader.getNumPages()):
                self.pdf_writer.addPage(pdf_reader.getPage(page))

        self.displaySucessfullCreationMessage()


    def saveFile(self):
        file_name = self.saveFileDialog()
        if file_name:
            with open(file_name, "wb") as out:
                self.pdf_writer.write(out)
                self.pdfmerger.process_label.setText(f"PDF-File successfully saved as \n{file_name}")


    def displaySucessfullCreationMessage(self):
        if self.pdfmerger.current_files:
            self.pdfmerger.process_label.setText("PDF File created successfully. Press Save for saving your file")