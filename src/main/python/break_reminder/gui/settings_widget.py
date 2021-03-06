from PyQt5.QtWidgets import (
    QLabel, QApplication,
    QWidget, QGridLayout, QSpinBox, QPushButton, QFrame
)
from PyQt5.QtCore import Qt, pyqtSignal


class SettingsQWidget(QWidget):

    config_data_signal = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowFlags(
            self.windowFlags() |
            Qt.WindowStaysOnTopHint
        )

        layout = QGridLayout()

        ##### Title #####
        title = QLabel('Break reminder settings', self)
        layout.addWidget(title, 0, 0, 2, 0, Qt.AlignCenter)
        #################

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        layout.addWidget(line, 2, 0, 2, 2)

        ##### Break time spinbox #####
        title_break = QLabel('Break time: ', self)
        layout.addWidget(title_break, 4, 0)

        break_hours_label = QLabel('Hours: ', self)
        layout.addWidget(break_hours_label, 5, 0, Qt.AlignCenter)
        self.break_hours_spinbox = QSpinBox(self)
        self.break_hours_spinbox.setRange(0, 23)
        layout.addWidget(self.break_hours_spinbox, 5, 1)

        break_minutes_label = QLabel('Minutes: ', self)
        layout.addWidget(break_minutes_label, 6, 0, Qt.AlignCenter)
        self.break_minutes_spinbox = QSpinBox(self)
        self.break_minutes_spinbox.setRange(0, 59)
        layout.addWidget(self.break_minutes_spinbox, 6, 1)
        ##############################

        ##### Active time spinbox #####
        title_active = QLabel('Active time:', self)
        layout.addWidget(title_active, 7, 0)

        active_hours_label = QLabel('Hours: ', self)
        layout.addWidget(active_hours_label, 8, 0, Qt.AlignCenter)
        self.active_hours_spinbox = QSpinBox(self)
        self.active_hours_spinbox.setRange(0, 23)
        layout.addWidget(self.active_hours_spinbox, 8, 1)

        active_minutes_label = QLabel('Minutes: ', self)
        layout.addWidget(active_minutes_label, 9, 0, Qt.AlignCenter)
        self.active_minutes_spinbox = QSpinBox(self)
        self.active_minutes_spinbox.setRange(0, 59)
        layout.addWidget(self.active_minutes_spinbox, 9, 1)
        ###############################

        ##### Notification interval #####
        title_interval = QLabel('Notifications interval:', self)
        layout.addWidget(title_interval, 10, 0, 1, 2)

        notification_minutes = QLabel('Minutes: ', self)
        layout.addWidget(notification_minutes, 11, 0, Qt.AlignCenter)
        self.notification_minutes_spinbox = QSpinBox(self)
        self.notification_minutes_spinbox.setRange(0, 59)
        self.notification_minutes_spinbox.setToolTip(
            '0 disables notifications')
        layout.addWidget(self.notification_minutes_spinbox, 11, 1)
        #################################

        ok_btn = QPushButton('Ok', self)
        ok_btn.clicked.connect(self.save_changes)

        layout.addWidget(ok_btn, 12, 0, 1, 2, Qt.AlignCenter)
        self.setLayout(layout)

        self.setStyleSheet('background-color: grey;')

        # window should be small widget close to systray icon
        x = QApplication.desktop().size().width() / 1.5
        y = 150
        width = 200
        height = 350
        self.setFixedSize(width, height)
        self.setGeometry(x, y, width, height)

    def save_changes(self):
        seconds_total_break = self.break_hours_spinbox.value() * 3600 +\
            self.break_minutes_spinbox.value() * 60

        seconds_total_active = self.active_hours_spinbox.value() * 3600 +\
            self.active_minutes_spinbox.value() * 60

        notification_interval = self.notification_minutes_spinbox.value() * 60
        send_notification = 1 if notification_interval else 0

        self.config_data_signal.emit({
            'break_time': seconds_total_break,
            'active_time': seconds_total_active,
            'notification_interval': [
                send_notification,
                notification_interval
            ]
        })

        self.hide()
