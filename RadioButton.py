import sys
from PyQt5.QtWidgets import (QPushButton, QVBoxLayout, QApplication, QWidget, QLabel, QRadioButton)


def checked(ch, l1):
    if ch:
        l1.setText("Dogs")
    else:
        l1.setText("Cats")


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.l1 = QLabel("Which Animal Do You Like")
        self.dogs = QRadioButton("Dogs")
        self.cats = QRadioButton("Cats")
        self.btn = QPushButton("Select")

        self.init_ui()

    def init_ui(self):
        v_box = QVBoxLayout()
        v_box.addWidget(self.l1)
        v_box.addWidget(self.dogs)
        v_box.addWidget(self.cats)
        v_box.addWidget(self.btn)

        self.setLayout(v_box)
        self.setWindowTitle("PyQt Lessons")

        self.btn.clicked.connect(lambda: checked(self.dogs.isChecked(), self.l1))

        self.show()


app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
