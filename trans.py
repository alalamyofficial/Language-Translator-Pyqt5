import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog , QMessageBox
import googletrans
from googletrans import Translator

class MainWindow(QDialog):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("trans.ui", self)


        self.setWindowTitle("Translator")
        self.setWindowIcon(QtGui.QIcon("trans1.png"))


        self.textEdit.clear()
        self.textEdit_2.clear()
        self.add_languages()


        self.pushButton.clicked.connect(self.translatetxt)
        self.pushButton_2.clicked.connect(self.clear)



    def add_languages(self):
        for i in googletrans.LANGUAGES.values():
            self.comboBox.addItem(i.capitalize())
            self.comboBox_2.addItem(i.capitalize())



    def translatetxt(self):

        try:

            text_1 = self.textEdit.toPlainText()
            lang_1 = self.comboBox.currentText()        
            lang_2 = self.comboBox_2.currentText() 


            translator = googletrans.Translator()
            translate1 = translator.translate(text_1, src=lang_1 , dest=lang_2)
            self.textEdit_2.setText(translate1.text)   

        except Exception as e:
              self.error_message(e)      


    def error_message(self,text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error")
        msg.setText(str(text))
        msg.exec_()          

    def clear(self):
        self.textEdit.clear()
        self.textEdit_2.clear()


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()