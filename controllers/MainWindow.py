from PySide2.QtWidgets import QWidget
from views.Ui_MainWindow import Ui_Form
from PySide2.QtCore import Qt

class UiFormWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.temperaturaLabel.setTextFormat(Qt.RichText)
        textoActual = self.temperaturaLabel.text()
        valor = 50
        self.temperaturaLabel.setText("<html><head/><body><p align=\"right\"><span style=\" font-size:48pt;\">" + str(valor) + "</span></p></body></html>")

