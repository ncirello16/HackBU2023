import sys, os
from PyQt5.QtWidgets import (QApplication,QMainWindow, QPushButton,QWidget, QLineEdit,
                             QRadioButton,QCommandLinkButton, QMessageBox, QInputDialog)
from PyQt5.QtCore import QObject, QThread, pyqtSignal, QProcess, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

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
        self.whichOne = "human"
        self.setupUi(self)
        self.player = QMediaPlayer()
        self.init()

    def doggy(self):
        self.dog_switch.setEnabled(False)
        self.cat_swItch.setEnabled(True)
        self.human_switch.setEnabled(True)
        self.whichOne = "doggy"
    def cat(self):
        self.cat_swItch.setEnabled(False)
        self.dog_switch.setEnabled(True)
        self.human_switch.setEnabled(True)
        self.whichOne = "cat"
    def human(self):
        self.human_switch.setEnabled(False)
        self.dog_switch.setEnabled(True)
        self.cat_swItch.setEnabled(True)
        self.whichOne = "human"

    def take_input_and_output(self):
        output = "You: "
        output += self.input_lineEdit.text()

        self.output_lineEdit.append(output)
        self.input_lineEdit.clear()
        self.botOutput()

    def botOutput(self):
        output = f"{self.whichOne}: "
        if self.whichOne == "doggy":
            output += "Bark! Bark!"
            self.output_lineEdit.append(output)
            self.playAudioFile('Dog Barking Sound Effects _ No Copyright Sound Effects Free To Use.mp3')

        elif self.whichOne == "cat":
            output += "Meow! Meow!"
            self.output_lineEdit.append(output)
            self.playAudioFile('Cat meow sound effect.mp3')

        elif self.whichOne == "human":
            output += "something something"
            self.output_lineEdit.append(output)

    def playAudioFile(self, file):

        full_file_path = os.path.join(os.getcwd(),
                                      file)
        url = QUrl.fromLocalFile(full_file_path)
        content = QMediaContent(url)

        self.player.setMedia(content)
        self.player.play()

    def init(self):
        self.human_switch.setEnabled(False)

        self.send.clicked.connect(self.take_input_and_output)
        self.dog_switch.clicked.connect(self.doggy)
        self.cat_swItch.clicked.connect(self.cat)
        self.human_switch.clicked.connect(self.human)
        self.input_lineEdit.returnPressed.connect(self.take_input_and_output)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
