#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''start_ui'''

import os
import sys
import time

from ui.ui import Ui_Form

from PySide.QtGui import QApplication, QWidget, QFileDialog
from PySide.QtCore import QThread, Signal, Slot

ABORT = False

class StartThread(QThread):
    '''doc'''

    end_signal = Signal()
    proc_signal = Signal(int)
    def __init__(self):
        super(StartThread, self).__init__(None)
    def run(self):
        '''doc'''
        global ABORT # pylint:disable=global-statement
        ABORT = False
        print("doing")
        for icon in range(1, 11):

            time.sleep(1)
            self.proc_signal.emit(icon * 10) #pylint:disable=no-member

            if ABORT:
                print("abort")
                self.end_signal.emit() #pylint:disable=no-member
                return

        print("done")
        self.end_signal.emit() #pylint:disable=no-member


class SynTool(QWidget, Ui_Form):
    '''doc'''
    def __init__(self):
        super(SynTool, self).__init__()
        self.setupUi(self)

        # start_button
        self.start_button.clicked.connect(self.start_button_clicked_slot) #pylint:disable=no-member

        self.start_thread = StartThread()
        self.start_thread.end_signal.connect(self.start_thread_end_slot) #pylint:disable=no-member
        self.start_thread.proc_signal.connect(self.start_thread_proc_slot) #pylint:disable=no-member

        self.proc_box.setMinimum(0)
        self.proc_box.setMaximum(100)
        self.proc_box.setValue(0)

        # source_button
        self.source_button.clicked.connect(self.source_button_clicked_slot) #pylint:disable=no-member

        # target_button
        self.target_button.clicked.connect(self.target_button_clicked_slot) #pylint:disable=no-member

        # target_button
        self.abort_button.clicked.connect(self.abort_button_clicked_slot) #pylint:disable=no-member

    @Slot()
    def start_button_clicked_slot(self):
        '''doc'''
        self.source_box.setDisabled(True)
        self.source_button.setDisabled(True)
        self.target_box.setDisabled(True)
        self.target_button.setDisabled(True)
        self.select_box.setDisabled(True)
        self.save_button.setDisabled(True)
        self.delete_button.setDisabled(True)
        self.start_all_button.setDisabled(True)
        self.start_button.setDisabled(True)
        self.abort_button.setDisabled(False)
        self.start_thread.start()

    @Slot()
    def start_thread_end_slot(self):
        '''doc'''
        self.source_box.setDisabled(False)
        self.source_button.setDisabled(False)
        self.target_box.setDisabled(False)
        self.target_button.setDisabled(False)
        self.select_box.setDisabled(False)
        self.save_button.setDisabled(False)
        self.delete_button.setDisabled(False)
        self.start_all_button.setDisabled(False)
        self.start_button.setDisabled(False)
        self.abort_button.setDisabled(True)

    @Slot(int)
    def start_thread_proc_slot(self, value):
        '''doc'''
        self.proc_box.setValue(value)

    @Slot()
    def source_button_clicked_slot(self):
        '''doc'''
        self.source_button.setDisabled(True)
        select_dir = QFileDialog.getExistingDirectory()
        if os.path.isdir(select_dir):
            self.source_box.setText(select_dir)
        self.source_button.setDisabled(False)

    @Slot()
    def target_button_clicked_slot(self):
        '''doc'''
        self.target_button.setDisabled(True)
        select_dir = QFileDialog.getExistingDirectory()
        if os.path.isdir(select_dir):
            self.target_box.setText(select_dir)
        self.target_button.setDisabled(False)

    @Slot()
    def abort_button_clicked_slot(self):
        '''doc'''
        global ABORT # pylint:disable=global-statement
        self.abort_button.setDisabled(True)
        ABORT = True

def main():
    '''main'''
    app = QApplication(sys.argv)
    syn_tool = SynTool()
    syn_tool.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
