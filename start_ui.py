#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''start_ui'''



import sys
import time

from ui.ui import Ui_Form

from PySide.QtGui import QDialog, QApplication, QWidget, QIcon
from PySide.QtCore import QThread, Signal, Slot



class StartThread(QThread):
    '''doc'''

    signal = Signal(list)
    def __init__(self):
        QThread.__init__(self)

    def run(self):
        '''stop'''
        time.sleep(2)

    def start(self):
        '''start'''

class SynTool(QDialog, Ui_Form):
    '''doc'''
    def __init__(self, parent=None):
        super(SynTool, self).__init__(parent)
        self.setupUi(self)
        self.start_button.connect(self.start)
        self.start_thread = None

    def start(self):
        '''doc'''
        self.start_button.setDisabled(True)
        self.start_thread = StartThread()

    @Slot(str)
    def signal(self):
        '''doc'''




def say_hello():
    '''say_hello'''
    start_thread = StartThread()
    start_thread.start()
    time.sleep(2)

def main():
    '''main'''
    qt_applpdddd = QApplication(sys.argv)
    q_form = QWidget()
    q_ui = Ui_Form()
    q_ui.setupUi(q_form)
    q_ui.start_button.clicked.connect(say_hello)# pylint: disable=no-member
    q_form.setWindowIcon(QIcon("main.ico"))
    q_form.show()
    sys.exit(qt_applpdddd.exec_())

if __name__ == "__main__":
    main()
