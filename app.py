from PySide2.QtWidgets import QApplication
from controllers.MainWindow import UiFormWindow

if __name__ == "__main__":
    app = QApplication()
    window = UiFormWindow()
    window.show()

    app.exec_()