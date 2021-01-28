import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QLabel 

displayedText = 'Hello World!'
if __name__ == '__main__':
    a = QApplication(sys.argv) 
    
    form = QWidget() 
    form.setGeometry(100,150,350,250) 
    form.setWindowTitle('Alpha - a Chrono Virtual Assistant') 
    
    label = QLabel() 
    label.setText(displayedText)
    label.move(140,100)
    label.setParent(form)
    
    form.show() 
    
    a.exec_()


