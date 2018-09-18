import sys
from PyQt5.QtWidgets import (QCheckBox, QVBoxLayout, QApplication, QWidget, QLabel)


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.ch = QCheckBox("Do you want to save?")
        self.l1 = QLabel()

        self.init_ui()

    def init_ui(self):
        v_box = QVBoxLayout()
        v_box.addWidget(self.ch)
        v_box.addWidget(self.l1)

        self.setLayout(v_box)
        self.setWindowTitle("PyQt Lessons")

        self.ch.clicked.connect(lambda: self.checked(self.ch.isChecked(), self.l1))

        self.show()

    def checked(self, ch, l1):
        if ch:
            l1.setText("Yes")
        else:
            l1.setText("No")


app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
