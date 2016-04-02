# import functools
import os

from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QPushButton


class ActionButton(QPushButton):

    ICONS = {each.split('.')[0]: 'gui/static/icons/{}'.format(each)
             for each in os.listdir(os.path.join(os.path.dirname(__file__), 'static', 'icons'))}

    def __init__(self, main_window):
        super().__init__(main_window)

        self.main_window = main_window
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        self.setGraphicsEffect(shadow)

        self.move(1300, 210)
        self.clicked.connect(self._clicked)

    def _clicked(self, event):

        print('abc')
        # self.set_icon('star')

    def define_click(self, function):
        self._clicked.connect(function)

    def set_icon(self, icon):
        self.setStyleSheet('qproperty-icon: url({})'.format(self.ICONS[icon]))