import sys
from PyQt5.QtWidgets import (QLineEdit, QSlider, QPushButton, QVBoxLayout, QApplication, QWidget, QLabel)
from PyQt5.QtCore import Qt


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.le = QLineEdit()
        self.l1 = QLabel()
        self.s1 = QSlider(Qt.Horizontal)
        self.s1.setMinimum(0)
        self.s1.setMaximum(100)
        self.s1.setValue(25)
        self.s1.setTickInterval(10)
        self.s1.setTickPosition(QSlider.TicksBelow)
        self.init_ui()

    def init_ui(self):
        v_box = QVBoxLayout()
        v_box.addWidget(self.le)
        v_box.addWidget(self.l1)
        v_box.addWidget(self.s1)

        self.s1.valueChanged.connect(self.s_change)

        self.setLayout(v_box)
        self.setWindowTitle("PyQt Lessons")
        self.setGeometry(300, 300, 300, 300)

        self.show()

    def s_change(self):
        value = str(self.s1.value())
        self.l1.setText(value)
        self.le.setText(value)


app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
