import sys, os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QWidget, QLineEdit,
                             QRadioButton, QCommandLinkButton, QMessageBox, QInputDialog, QLabel, QHBoxLayout,
                             QVBoxLayout)
from PyQt5.QtCore import QObject, QThread, pyqtSignal, QProcess, QUrl, Qt, QPoint
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

from ui.chatBot import Ui_MainWindow
import chat


# def take_input_and_output(input_prompt_text, output_location):
#     app = QWidget.QApplication([])
#     text, ok = QWidget.QInputDialog.getText(None, 'Input Dialog', input_prompt_text)
#     if ok:
#         with open(output_location, 'w') as f:
#             f.write(text)
#     app.exec_()

# def take_input_and_output(input):
#
class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.layout = QVBoxLayout()
        self.layout.addWidget(MyBar(self))
        self.layout.addWidget(chatting(self))
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        self.setMinimumSize(800, 400)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.pressing = False


class chatting(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.whichOne = "human"
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
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
        inp = self.input_lineEdit.text()
        output = "You: "
        output += inp
        self.output_lineEdit.append(output)
        self.botOutput(inp)
        self.input_lineEdit.clear()

    def botOutput(self, inp=None):
        output = f"{self.whichOne}: "
        if self.whichOne == "doggy":
            output += "Bark! Bark!"
            self.output_lineEdit.append(output)
            self.playAudioFile('Sound/Dog Barking Sound Effects _ No Copyright Sound Effects Free To Use.mp3')

        elif self.whichOne == "cat":
            output += "Meow! Meow!"
            self.output_lineEdit.append(output)
            self.playAudioFile('Sound/Cat meow sound effect.mp3')

        elif self.whichOne == "human":
            output = chat.gettingInput(inp)
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


class MyBar(QWidget):

    def __init__(self, parent):
        super(MyBar, self).__init__()
        self.parent = parent
        print(self.parent.width())
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel("Chat Bot")
        self.setStyleSheet("background-color: rgb(47, 49, 54);")
        btn_size = 35

        self.pushButton_3 = QPushButton("x")
        self.pushButton_3.clicked.connect(self.btn_close_clicked)
        self.pushButton_3.setFixedSize(btn_size, btn_size)
        self.pushButton_3.setStyleSheet("background-color: rgb(32, 34, 37);"
                                        "color: red;")

        self.pushButton = QPushButton("-")
        self.pushButton.clicked.connect(self.btn_min_clicked)
        self.pushButton.setFixedSize(btn_size, btn_size)
        self.pushButton.setStyleSheet("background-color: rgb(32, 34, 37);"
                                      "color: white;")

        self.pushButton_2 = QPushButton("+")
        self.pushButton_2.clicked.connect(self.btn_max_clicked)
        self.pushButton_2.setFixedSize(btn_size, btn_size)
        self.pushButton_2.setStyleSheet("background-color: rgb(32, 34, 37);"
                                        "color: white;")

        self.title.setFixedHeight(35)
        self.title.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.pushButton)
        self.layout.addWidget(self.pushButton_2)
        self.layout.addWidget(self.pushButton_3)

        self.title.setStyleSheet("""
            background-color: rgb(32, 34, 37);
            color: white;
        """)
        self.setLayout(self.layout)

        self.start = QPoint(0, 0)
        self.pressing = False

    def resizeEvent(self, QResizeEvent):
        super(MyBar, self).resizeEvent(QResizeEvent)
        self.title.setFixedWidth(self.parent.width())

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end - self.start
            self.parent.setGeometry(self.mapToGlobal(self.movement).x(),
                                    self.mapToGlobal(self.movement).y(),
                                    self.parent.width(),
                                    self.parent.height())
            self.start = self.end

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False

    def btn_close_clicked(self):
        self.parent.close()

    def btn_max_clicked(self):
        self.parent.showMaximized()

    def btn_min_clicked(self):
        self.parent.showMinimized()  # self.parent.showMinimized()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
