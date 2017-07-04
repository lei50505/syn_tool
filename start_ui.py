#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''start_ui'''

import os
import sys
import time

from ui.ui import Ui_Form

from PySide.QtGui import QApplication, QWidget, QFileDialog
from PySide.QtCore import QThread, Signal, Slot


def singleton(cls, *args, **kw):
    '''doc'''
    instance = {}
    def _singleton():
        if cls not in instance:
            instance[cls] = cls(*args, **kw)
        return instance[cls]
    return _singleton

ABORT = "abort"

@singleton
class Data():
    '''doc'''
    def __init__(self):
        self.data = {}
    def set(self, key, val):
        '''doc'''
        self.data[key] = val
    def get(self, key):
        '''doc'''
        return self.data[key]

@singleton
class Error():
    '''doc'''
    def __init__(self):
        self.errors = []
    def add(self, val):
        '''doc'''
        self.errors.append(val)
    def get(self):
        '''doc'''
        return self.errors

class StartThread(QThread):
    '''doc'''
    #pylint:disable=no-member
    end_signal = Signal()
    proc_signal = Signal(int)
    log_signal = Signal(str)
    def __init__(self):
        super(StartThread, self).__init__(None)
    def run(self):
        '''doc'''

        data = Data()
        data.set(ABORT, False)

        self.log_signal.emit("doing")
        for icon in range(1, 11):

            time.sleep(1)
            self.proc_signal.emit(icon * 10)

            if data.get(ABORT):

                self.log_signal.emit("abort")
                self.end_signal.emit()
                return

        self.log_signal.emit("done")
        self.end_signal.emit()


class SynTool(QWidget, Ui_Form):
    '''doc'''
    def __init__(self):
        super(SynTool, self).__init__()
        self.setupUi(self)
        #pylint:disable=no-member
        # start_button
        self.start_button.clicked.connect(self.start_button_clicked_slot)
        self.start_thread = StartThread()
        self.start_thread.end_signal.connect(self.start_thread_end_slot)
        self.start_thread.proc_signal.connect(self.start_thread_proc_slot)
        self.start_thread.log_signal.connect(self.start_thread_log_slot)
        self.proc_box.setMinimum(0)
        self.proc_box.setMaximum(100)
        self.proc_box.setValue(0)

        # source_button
        self.source_button.clicked.connect(self.source_button_clicked_slot)

        # target_button
        self.target_button.clicked.connect(self.target_button_clicked_slot)

        # abort_button
        self.abort_button.clicked.connect(self.abort_button_clicked_slot)

        # delete_button
        self.delete_button.clicked.connect(self.delete_button_clicked_slot)


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
    @Slot(str)
    def start_thread_log_slot(self, value):
        '''doc'''
        self.log_box.append(value)

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
        data = Data()

        self.abort_button.setDisabled(True)
        data.set(ABORT, True)

    @Slot()
    def delete_button_clicked_slot(self):
        '''doc'''
        self.delete_button.setDisabled(True)

        self.delete_button.setDisabled(False)

def main():
    '''main'''
    app = QApplication(sys.argv)
    syn_tool = SynTool()
    syn_tool.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
