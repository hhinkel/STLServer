import datetime
import sys
import time

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mo-Tell Liar's Contest Timer")
        self.total_seconds = 60
        self.timer = datetime.timedelta()

        self.layout = QVBoxLayout()

        self.label = QLabel()

        start_button = QPushButton("Start")
        start_button.setCheckable(True)
        start_button.clicked.connect(self.the_button_was_clicked)
        self.layout.addWidget(start_button)
        # layout.addWidget(self.label)
        # self.label.setText("Test 2")
        container = QWidget()
        container.setLayout(self.layout)

        self.setCentralWidget(container)

    def the_button_was_clicked(self):
        self.layout.addWidget(self.label)
        self.label.setText("Test 2")
        print("Clicked")
        self.countdown(1)

    def countdown(self, minutes = 5):
        self.total_seconds = minutes * 60
        while self.total_seconds > 0:
            self.timer = datetime.timedelta(seconds=self.total_seconds)
            self.label.setText(str(self.timer))
            print(self.timer)
            time.sleep(1)
            self.total_seconds -= 1
        while True:
            self.timer = datetime.timedelta(seconds=self.total_seconds)
            self.label.setText(str(self.timer))
            print(self.timer)
            time.sleep(1)
            self.total_seconds += 1


app = QApplication(sys.argv)

window = MainWindow()
window.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.exec()
