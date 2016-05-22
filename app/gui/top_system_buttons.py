from PyQt5.QtWidgets import (QFrame, QPushButton, QHBoxLayout,
                             QGraphicsDropShadowEffect, QLabel)


class TopSystemButtons(QFrame):
    """
    Frame contains close and minimize buttons
    """

    def __init__(self, main_window):
        super().__init__()

        self.move_offset = None
        self.mouseMoveEvent = self._get_move_function(main_window)

        main_window.communication.user_selected.connect(self.set_title)

        b = QHBoxLayout()
        b.addStretch()
        b.setSpacing(0)
        b.setContentsMargins(0, 0, 0, 0)

        exit_button = QPushButton('x')
        exit_button.clicked.connect(main_window.close)

        minimize_button = QPushButton('_')
        minimize_button.clicked.connect(main_window.minimize)

        self.title = QLabel('')
        b.addWidget(self.title)
        b.addSpacing(10)
        b.addWidget(minimize_button)
        b.addSpacing(1)
        b.addWidget(exit_button)
        self.setLayout(b)

    def _get_move_function(self, main_window):

        def _f(event):
            if not self.move_offset:
                return

            x = event.globalX()
            y = event.globalY()
            x_w = self.move_offset.x()
            y_w = self.move_offset.y()
            main_window.move(x - x_w, y - y_w)

        return _f

    def set_title(self, user):
        self.title.setText('{} {}. {}.'.format(user.surname, user.name[0], user.patronymic[0]))

    def mousePressEvent(self, event):
        self.move_offset = event.pos()

    def mouseReleaseEvent(self, event):
        """
        This prevents window from moving when buttons pressed
        """
        self.move_offset = None
