import sys
from PyQt5.QtWidgets import QApplication

from gui import TransparentWindow, SystemTrayIcon
from logic import Logic


break_time = 5
active_time = 10
prolong_break = 5

# with open(path.join(path.dirname(__file__), 'config.json'), 'r') as file:
#     parameters = json.loads(file.read(), object_hook=json_hook)
#     break_time = parameters['break_time']
#     active_time = parameters['active_time']
#     prolong_break = parameters['prolong_break']

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("Break Reminder")
    app.setQuitOnLastWindowClosed(False)


    window = TransparentWindow()
    system_tray_icon = SystemTrayIcon(window)

    logic = Logic(break_time, active_time, prolong_break)

    logic.display_break_ui_signal.connect(window.show)
    logic.hide_break_ui_signal.connect(window.hide)
    logic.update_timer_signal.connect(window.updateUITimer)

    logic.startActiveTimer()

    sys.exit(app.exec_())