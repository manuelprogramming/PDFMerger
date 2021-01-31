from HelpingFunction import *


class FileHandler:
    def __init__(self, process_label, item_list):
        self.process_label = process_label
        self.item_list = item_list
        self.current_files = []

    @tryThis
    def clearFiles(self):
        self.item_list.clear()
        self.current_files = []
        self.process_label.setText("All Files have been deleted")

    @tryThis
    def clearSelectedFile(self):
        for item in self.item_list.selectedItems():
            self._takeItemFromList(item)
        self.process_label.setText("Selected Files have been removed")

    def _takeItemFromList(self, item):
        row = self.item_list.row(item)
        self.item_list.takeItem(row)
        self.current_files.remove(item.text())


