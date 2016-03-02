import os
import sys
import functools

from PyQt5 import QtCore
from PyQt5.QtCore import QCoreApplication, Qt, QTimer
from PyQt5.QtWidgets import (QWidget, QStackedLayout, QDesktopWidget,
                             QVBoxLayout, QShortcut, QApplication)

from PyQt5.QtGui import QKeySequence

from gui.select_menu import SelectItemMenu
from gui.data_widget import DataWidget
from gui.db_widget import DBWidget
from gui.options_widget import OptionsWidget
from gui.report_widget import ReportWidget
from gui.top_frame import TopFrame
from gui.top_system_buttons import TopSystemButtons


class MainWindow(QWidget):

    MENU_LABELS = 'data', 'report', 'base', 'options'

    def __init__(self, items):
        super().__init__()

        self.items = items

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowTitle('Hospital Helper')
        dw = QDesktopWidget()
        w = dw.geometry().size().width() * 0.75
        self.resize(w, w * 0.6)

        self.stacked_layout = QStackedLayout()
        vbox = QVBoxLayout()
        vbox.setContentsMargins(0, 0, 0, 0)
        vbox.setSpacing(0)
        self.setLayout(vbox)

        vbox.addWidget(TopSystemButtons(self), stretch=3)

        t = TopFrame(self, items)
        vbox.addWidget(t, stretch=15)
        self.waterline = self.height() - t.height()

        vbox.addSpacing(50)
        vbox.addLayout(self.stacked_layout, stretch=40)

        qr = self.frameGeometry()
        cp = dw.availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        self._create_layout()
        self.select_menu = SelectItemMenu(self, items)

        self._set_shortcuts()

        self.show()

    def _set_shortcuts(self):
        QShortcut(QKeySequence('Esc'), self).activated.connect(self.close)
        QShortcut(Qt.CTRL, self).activated.connect(self.close)

    def _create_layout(self):
        # Order matters
        self.frames = [frame(self, self.items) for frame in (DataWidget,
                                                             ReportWidget,
                                                             DBWidget,
                                                             OptionsWidget)]
        for frame in self.frames:
            self.stacked_layout.addWidget(frame)

    def set_select_menu_item_visibility(self, value, event=None):
        # Event is triggered only on 'Data' tab
        if not self.stacked_layout.currentIndex():
            self.select_menu.setVisible(value)
            self.select_menu.raise_()

    def select_item(self, index):
        self.frames[0].select_item(index)
        self.set_select_menu_item_visibility(False)

    def data_button_entered(self, event):
        # Event is triggered only on 'Data' tab
        if not self.stack_index:
            self.set_select_menu_item_visibility(True)

    def select_menu_button_clicked(self, btn):
        for i, each in enumerate(self.MENU_LABELS):
            if _(each) == btn.text():
                if self.stacked_layout.currentIndex() == i == 0:
                    self.set_select_menu_item_visibility(not self.select_menu.isVisible())
                self.stacked_layout.setCurrentIndex(i)

    def _h(self, event):
        mods = event.modifiers()
        if mods & QtCore.Qt.ControlModifier and mods & QtCore.Qt.ShiftModifier:
            print('asd')

    def keyPressEvent(self, event):
        t = QTimer()
        t.singleShot(200, functools.partial(self._h, event))
        # mods = event.modifiers()
        # if mods & QtCore.Qt.ControlModifier and mods & QtCore.Qt.ShiftModifier:
        #     return
        # if (event.modifiers() == Qt.ControlModifier and event.text() is ''):
        #     self.set_select_menu_item_visibility(True)
        # super().keyPressEvent(event)

    def keyReleaseEvent(self, event):
        if (event.text() is ''):
            self.set_select_menu_item_visibility(False)

    def close(self, event=None):
        QCoreApplication.instance().quit()

    def minimize(self, event=None):
        self.setWindowState(Qt.WindowMinimized)


def init(items):
    app = QApplication(sys.argv)
    with open(os.path.join(os.path.dirname(__file__), 'style.qss'), 'r') as f:
        app.setStyleSheet(f.read())
    mw = MainWindow(items)
    sys.exit(app.exec_())
