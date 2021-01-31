

class ModeSelector:
    def __init__(self, pdfmerger):
        self.current_mode = "Merge"
        self.pdfmerger = pdfmerger

    def getMode(self):
        return self.current_mode

    def _setupModeChange(self):
        self.pdfmerger.showRadioButtons()
        self.pdfmerger.hideConverterWidgets()
        self.pdfmerger.action_button.clicked.disconnect()

        self.pdfmerger.process_label.setText(f"Operating in {self.current_mode} Mode")
        self.pdfmerger.action_button.setText(self.current_mode)

    def setSplitMode(self):
        self.current_mode = "Split"
        self._setupModeChange()
        self.pdfmerger.radioButton_split.setChecked(True)
        self.pdfmerger.save_button.setDisabled(True)

    def setMergeMode(self):
        self.current_mode = "Merge"
        self._setupModeChange()
        self.pdfmerger.radioButton_merge.setChecked(True)
        self.pdfmerger.save_button.setDisabled(False)

    def setImageConvertMode(self):
        self.current_mode = "Convert"
        self._setupModeChange()
        self.pdfmerger.hideRadioButtons()
        self.pdfmerger.showConverterWidgets()
        self.pdfmerger.save_button.setDisabled(False)

