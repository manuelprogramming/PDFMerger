import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PDFMergerUI import Ui_PDFMergerUI
from PDFMerger import PDFMerger

if __name__ == "__main__":
    app = QApplication(sys.argv)
    merger = PDFMerger(app)
    sys.exit(app.exec())