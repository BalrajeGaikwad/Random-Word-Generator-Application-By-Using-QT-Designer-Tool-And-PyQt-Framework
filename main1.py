from PyQt5 import QtWidgets, QtCore
from win_ui1 import Ui_MainWindow
from random import choice
my_words = ['hello', 'good', 'bye', 'test', 'python', 'happy', 'sad']
class mainwin(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainwin, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.no_of_clicks=0
        self.ui.pushButton.pressed.connect(self.random_word1)
        self.ui.pushButton_2.pressed.connect(self.random_word2)
        self.ui.pushButton_3.pressed.connect(self.random_word3)
        #self.ui.pushButton.pressed.connect(self.random_word1)
        
        self.show()

  #  my_words=['hello','good','bye','test','python','happy','sad']
    
    def random_word1(self):
        word=choice(my_words)
        self.ui.label_2.setText(word)
        self.no_of_clicks+=1
        self.ui.label_5.setText(f"No Of Clicks:{self.no_of_clicks}")

    def random_word2(self):
        word=choice(my_words)
        self.ui.label_3.setText(word)
        self.no_of_clicks+=1
        self.ui.label_6.setText(f"No Of Clicks:{self.no_of_clicks}")

    def random_word3(self):
        word=choice(my_words)
        self.ui.label_4.setText(word)
        self.no_of_clicks+=1
        self.ui.label_7.setText(f"No Of Clicks:{self.no_of_clicks}")



if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    obj=mainwin()
    sys.exit(app.exec_())