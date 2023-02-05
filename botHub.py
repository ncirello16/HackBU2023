import sys, os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QWidget, QLineEdit,
                             QRadioButton, QCommandLinkButton, QMessageBox, QInputDialog, QLabel, QHBoxLayout,
                             QVBoxLayout)
from PyQt5.QtCore import QObject, QThread, pyqtSignal, QProcess, QUrl, Qt, QPoint
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

from ui.chatBot import Ui_MainWindow
import chat
import find
import diningAccountBot
from multiprocessing.pool import ThreadPool

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
        self.ps = False

    def doggy(self):
        self.dog_switch_3.setEnabled(False)
        self.cat_swItch.setEnabled(True)
        self.human_switch.setEnabled(True)
        self.dic_switch.setEnabled(True)
        self.meal_switch.setEnabled(True)
        self.input_lineEdit.setPlaceholderText("Please Say HI to Dog")
        self.whichOne = "doggy"
        self.input_lineEdit.setEchoMode(QLineEdit.Normal)
        self.ps = False
        self.output_lineEdit.clear()

    def cat(self):
        self.cat_swItch.setEnabled(False)
        self.dog_switch_3.setEnabled(True)
        self.human_switch.setEnabled(True)
        self.dic_switch.setEnabled(True)
        self.meal_switch.setEnabled(True)
        self.input_lineEdit.setPlaceholderText("Please Say HI to Cat")
        self.input_lineEdit.setEchoMode(QLineEdit.Normal)
        self.whichOne = "cat"
        self.ps = False
        self.output_lineEdit.clear()

    def human(self):
        self.human_switch.setEnabled(False)
        self.dog_switch_3.setEnabled(True)
        self.cat_swItch.setEnabled(True)
        self.dic_switch.setEnabled(True)
        self.meal_switch.setEnabled(True)
        self.input_lineEdit.setPlaceholderText("Please ask Something to James")
        self.input_lineEdit.setEchoMode(QLineEdit.Normal)
        self.whichOne = "human"
        self.ps = False
        self.output_lineEdit.clear()

    def dic(self):
        self.dic_switch.setEnabled(False)
        self.dog_switch_3.setEnabled(True)
        self.cat_swItch.setEnabled(True)
        self.human_switch.setEnabled(True)
        self.meal_switch.setEnabled(True)
        self.whichOne = "Dic"
        self.input_lineEdit.setPlaceholderText("Please type one word. DicBot will define it")
        self.input_lineEdit.setEchoMode(QLineEdit.Normal)
        self.output_lineEdit.clear()
        self.ps = False

    def meal(self):
        self.meal_switch.setEnabled(False)
        self.dog_switch_3.setEnabled(True)
        self.cat_swItch.setEnabled(True)
        self.human_switch.setEnabled(True)
        self.dic_switch.setEnabled(True)
        self.whichOne = "meal"
        self.input_lineEdit.setEchoMode(QLineEdit.Normal)
        self.output_lineEdit.clear()

        if(self.ps == False):
            self.input_lineEdit.setPlaceholderText("Please Type ID:")
            self.output_lineEdit.append("Please Type ID:")
    def take_input_and_output(self):
        if self.whichOne != "meal":
            inp = self.input_lineEdit.text()
            output = "You: "
            output += inp
            self.output_lineEdit.append(output)
            self.botOutput(inp)
            self.input_lineEdit.clear()
        else:
            inp = self.input_lineEdit.text()
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

        elif self.whichOne == "Dic":
            output = find.Diction(inp)
            self.output_lineEdit.append(output)

        elif self.whichOne == "meal":
            if(self.ps == False):
                self.id = inp
                self.output_lineEdit.append("Please Type Password:")
                self.input_lineEdit.setPlaceholderText("Please Type Password:")
                self.input_lineEdit.setEchoMode(QLineEdit.Password)
                self.ps = True

            else:
                pool = ThreadPool(processes=3)


                pool.apply_async(self.work, (self.id,inp))
                self.output_lineEdit.append("Getting an output...\nPlease Wait\n-------------------------")




    def work(self,id,ps):
        try:

            pool = ThreadPool(processes=3)
            moneyLeft=diningAccountBot.parseBingWebpage(id,ps)
            # moneyLeft = diningAccountBot.parseBingWebpage(self.id,ps)
            ps = ""
            self.id = ""
            self.ps = False
            output = diningAccountBot.getMoneyPerDay(moneyLeft)
            self.input_lineEdit.setEchoMode(QLineEdit.Normal)
            output = f'You have {output[0]} money left on your account...\n' \
                     f'You can spend "{output[1]}" a day\n-------------------------\nPlease Type ID:'
            print(f'You have {output[0]} money left on your account...')
            print(f'You can spend "{output[1]}" a day\n-------------------------\nPlease Type ID:')
            self.input_lineEdit.setPlaceholderText("Please Type ID:")
            self.output_lineEdit.append(output)
        except:
            self.output_lineEdit.append("Something went to wrong...\n-------------------------\nPlease Type ID:")
            self.input_lineEdit.setPlaceholderText("Please Type ID:")
            self.ps = False
            self.input_lineEdit.setEchoMode(QLineEdit.Normal)

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
        self.dog_switch_3.clicked.connect(self.doggy)
        self.cat_swItch.clicked.connect(self.cat)
        self.human_switch.clicked.connect(self.human)
        self.dic_switch.clicked.connect(self.dic)
        self.meal_switch.clicked.connect(self.meal)
        self.input_lineEdit.returnPressed.connect(self.take_input_and_output)
        self.input_lineEdit.setPlaceholderText("Please ask Something to James")



class MyBar(QWidget):

    def __init__(self, parent):
        super(MyBar, self).__init__()
        self.parent = parent
        print(self.parent.width())
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel("Bot Hub")
        self.setStyleSheet("background-color: rgb(47, 49, 54);")
        btn_size = 35
        self.goback = False
        self.max = False

        self.pushButton_3 = QPushButton("x")
        self.pushButton_3.clicked.connect(self.btn_close_clicked)
        self.pushButton_3.setFixedSize(btn_size, btn_size)
        self.pushButton_3.setStyleSheet("background-color: rgb(32, 34, 37);"
                                        "color: red;")

        self.pushButton = QPushButton("_")
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
        if(self.goback == False):
            self.total = [self.parent.height(),self.parent.width()]
            self.goback = True
            self.parent.showMaximized()
        else:
            self.btn_back_clicked()

    def btn_back_clicked(self):
        self.parent.setFixedHeight(self.total[0])
        self.parent.setFixedWidth(self.total[1])
        self.goback = False


    def btn_min_clicked(self):
        self.parent.showMinimized()  # self.parent.showMinimized()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
