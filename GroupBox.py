import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QGroupBox, QGridLayout
from PyQt5.QtWidgets import QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QAction, qApp, QLabel


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.l1 = QLabel("Value1")
        self.b1 = QPushButton("Set Data")
        self.le = QTextEdit()
        self.le.setFixedSize(210, 30)

        self.l2 = QLabel("Value1")
        self.b2 = QPushButton("Set Data")
        self.le2 = QTextEdit()
        self.le2.setFixedSize(210, 30)

        vbox_gr = QGridLayout()
        vbox_ui = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox.addLayout(vbox_ui)
        hbox.addLayout(vbox_gr)

        infoGBox = QGroupBox("General info")
        infoGBoxLayout = QGridLayout()
        infoGBox.setLayout(infoGBoxLayout)
        infoGBox.setMinimumWidth(230)
        infoGBox.setMaximumWidth(230)

        infoGBoxLayout.addWidget(self.l1, 1, 0)
        infoGBoxLayout.addWidget(self.b1, 3, 1)
        infoGBoxLayout.addWidget(self.le, 2, 0)

        vbox_ui.addWidget(infoGBox)

        self.setLayout(hbox)
        self.setWindowTitle('PyQt5')
        self.show()


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
