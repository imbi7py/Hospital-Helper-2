from PyQt5.QtWidgets import QFrame, QStackedLayout

from gui.attributes_frame import AttributesFrame


class DataWidget(QFrame):

    def __init__(self, main_window, items):

        super().__init__(main_window)

        stacked_layout = QStackedLayout()
        main_window.communication.item_selected.connect(stacked_layout.setCurrentIndex)
        self.setLayout(stacked_layout)

        self.showEvent = self._get_show_event(main_window)

        for item in items:
            frame = AttributesFrame(main_window=main_window, item=item)
            stacked_layout.addWidget(frame)

    def _get_show_event(self, main_window):

        def show_event(event):
            main_window.communication.action_button_toggle.emit(False, None, None)

        return show_event
