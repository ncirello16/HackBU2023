import sys
from PyQt5.QtWidgets import (QApplication,QMainWindow, QPushButton,QWidget, QLineEdit,
                             QRadioButton,QCommandLinkButton, QMessageBox, QInputDialog)
from PyQt5.QtCore import QObject, QThread, pyqtSignal, QProcess

from ui.chatBot import Ui_MainWindow

# def take_input_and_output(input_prompt_text, output_location):
#     app = QWidget.QApplication([])
#     text, ok = QWidget.QInputDialog.getText(None, 'Input Dialog', input_prompt_text)
#     if ok:
#         with open(output_location, 'w') as f:
#             f.write(text)
#     app.exec_()

# def take_input_and_output(input):
#

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.init()

    def take_input_and_output(self):
        output = "You: "
        output += self.input_lineEdit.text()

        self.output_lineEdit.append(output)
        self.input_lineEdit.clear()
    def init(self):
        self.send.clicked.connect(self.take_input_and_output)
        self.input_lineEdit.returnPressed.connect(self.take_input_and_output)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
