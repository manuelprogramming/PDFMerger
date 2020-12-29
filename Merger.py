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


    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self.pdfmerger, "Merged File", "*.pdf", "All Files (*);;PDF Files (*.pdf)", options=options)
        if fileName:
            with open(fileName, "wb") as out:
                self.pdf_writer.write(out)
                self.pdfmerger.process_label.setText(f"PDF-File successfully saved as {fileName}")


    def displaySucessfullCreationMessage(self):
        if self.pdfmerger.current_files:
            self.pdfmerger.process_label.setText("PDF File created successfully. Press Save for saving your file")