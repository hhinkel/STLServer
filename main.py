import datetime
import sys
import time

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mo-Tell Liar's Contest Timer")

        start_button = QPushButton("Start")
        start_button.setCheckable(True)
        start_button.clicked.connect(self.the_button_was_clicked)

        self. setCentralWidget(start_button)

    def the_button_was_clicked(self):
        print("Clicked")
        countdown(1)


app = QApplication(sys.argv)

window = MainWindow()
window.show()


def countdown(minutes=5):
    total_seconds = minutes * 60
    while total_seconds > 0:
        timer = datetime.timedelta(seconds=total_seconds)
        print(timer)
        time.sleep(1)
        total_seconds -= 1
    while True:
        timer = datetime.timedelta(seconds=total_seconds)
        print(timer)
        time.sleep(1)
        total_seconds += 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.exec()
