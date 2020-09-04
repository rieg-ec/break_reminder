from PyQt5.QtWidgets import (
    QWidget, QPushButton, QLabel,
    QApplication, QVBoxLayout
    )
from PyQt5.QtCore import Qt

import time

class TransparentWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        ### TIMER LABEL ###
        self.timer_label = QLabel('', self)
        self.timer_label.setStyleSheet('font-size: 50px;')
        self.timer_label.setAlignment(Qt.AlignCenter)
        ###################

        ### INSTRUCTIONS LABELS ###
        instructions_label = QLabel('Press "Esc" to skip break or '
                                    +'"F1" to add 5 minutes', self)
        instructions_label.setStyleSheet('font-size: 30px;')

        ###########################

        layout.insertStretch(0, stretch=3)
        layout.addWidget(self.timer_label)
        layout.insertStretch(2, stretch=1)
        layout.addWidget(instructions_label)
        layout.insertStretch(4, stretch=4)

        layout.setAlignment(Qt.AlignCenter)
        self.setLayout(layout)

        '''
        WindowStaysOnTopHint for always on top,
        WindowTransparentForInput makes QWidget frameless,
        FramelessWindowHint makes transparent for input
        '''
        self.setWindowFlags(
            self.windowFlags() |
            Qt.WindowStaysOnTopHint |
            Qt.WindowTransparentForInput |
            Qt.FramelessWindowHint |
            Qt.Tool
        )

        # adjust transparency (opacity):
        self.setWindowOpacity(0.5)
        # full screen:
        self.resize(QApplication.desktop().size())
        # self.setWindowState(Qt.WindowFullScreen)
        self.setStyleSheet(
            'background-color: black;'
           +'color: white;')

    def show(self, time):
        self.update_UI_timer(time)
        print(time)
        super().show()


    def update_UI_timer(self, seconds_left):
        ''' called to update cronometer ui '''
        seconds_left_clock_mode = time.strftime(
            '%H:%M:%S', time.gmtime(seconds_left))
        self.timer_label.setText(seconds_left_clock_mode)
