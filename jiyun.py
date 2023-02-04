from PyQt5 import QtWidgets, QtGui

def take_input_and_output(input_prompt_text, output_location):
    app = QtWidgets.QApplication([])
    text, ok = QtWidgets.QInputDialog.getText(None, 'Input Dialog', input_prompt_text)
    if ok:
        with open(output_location, 'w') as f:
            f.write(text)
    app.exec_()

