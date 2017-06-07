#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''start_ui'''
import sys

from PySide import QtGui, QtCore


from ui import Ui_Form

class QtThread(QtCore.QThread):
    '''QtThread'''
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def stop(self):
        '''stop'''
    def start(self):
        '''start'''

def say_hello():
    '''say_hello'''
    print("Hello")

def main():
    '''main'''
    qt_applpdddd = QtGui.QApplication(sys.argv)
    q_form = QtGui.QWidget()
    q_ui = Ui_Form()
    q_ui.setupUi(q_form)
    #q_ui.startButton.clicked.connect(say_hello)# pylint: disable=no-member
    q_form.setWindowIcon(QtGui.QIcon("main.ico"))
    q_form.show()
    sys.exit(qt_applpdddd.exec_())

if __name__ == "__main__":
    main()
