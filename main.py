from PyQt5 import QtWidgets, QtCore
from win_ui import Ui_MainWindow
from random import choice
my_words = ['hello', 'good', 'bye', 'test', 'python', 'happy', 'sad']
class mainwin(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainwin, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        #self.no_of_clicks=0
        self.clicks_button1 = 0
        self.clicks_button2 = 0
        self.clicks_button3 = 0
        self.total_clicks=0
        self.ui.pushButton.pressed.connect(self.random_word1)
        self.ui.pushButton_2.pressed.connect(self.random_word2)
        self.ui.pushButton_3.pressed.connect(self.random_word3)
        self.ui.submit_1.pressed.connect(self.display_total_clicks1)
        self.ui.submit_2.pressed.connect(self.display_total_clicks2)
        self.ui.submit_3.pressed.connect(self.display_total_clicks3)
        
        self.show()

  #  my_words=['hello','good','bye','test','python','happy','sad']
    
    def random_word1(self):
        word=choice(my_words)
        self.ui.label_2.setText(word)
        self.clicks_button1+=1
        self.ui.label_5.setText(f"No Of Clicks:{self.clicks_button1}")

    def random_word2(self):
        word=choice(my_words)
        self.ui.label_3.setText(word)
        self.clicks_button2+=1
        self.ui.label_6.setText(f"No Of Clicks:{self.clicks_button2}")

    def random_word3(self):
        word=choice(my_words)
        self.ui.label_4.setText(word)
        self.clicks_button3+=1
        self.ui.label_7.setText(f"No Of Clicks:{self.clicks_button3}")

    def display_total_clicks1(self):
        self.ui.no_of_clicks_1.setText(
            f"Total Clicks:\n"
            f"Button 1: {self.clicks_button1}\n"
        )
    def display_total_clicks2(self):
        self.ui.no_of_clicks_2.setText(
            f"Total Clicks:\n"
            f"Button 2: {self.clicks_button2}\n"
        )
    def display_total_clicks3(self):
        self.ui.no_of_clicks_3.setText(
            f"Total Clicks:\n"
            f"Button 3: {self.clicks_button3}"
        )



if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    obj=mainwin()
    sys.exit(app.exec_())