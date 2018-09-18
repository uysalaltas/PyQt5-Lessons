import sys
import cv2
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap, QFont
from PyQt5.QtWidgets import *


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.timer = QTimer(self)
        self.capture = cv2.VideoCapture(0)

        self.image = None

        self.imgLabel = QLabel()
        self.imgLabel.setFixedHeight(480)
        self.imgLabel.setFixedWidth(640)

        v_box = QVBoxLayout()
        v_box.addWidget(self.imgLabel)

        self.setLayout(v_box)
        self.setWindowTitle('PyQt5')

        self.start_webcam()

        self.show()

    def start_webcam(self):
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

        self.timer.timeout.connect(self.update_frame)
        self.timer.start(5)

    def update_frame(self):
        ret, self.image = self.capture.read()
        self.image = cv2.flip(self.image, 1)

        self.display_image(self.image, 1)

    def display_image(self, img, window):
        qformat = QImage.Format_Indexed8
        if len(img.shape) == 3:
            if img.shape[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888

        outImage = QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)
        outImage = outImage.rgbSwapped()

        if window == 1:
            self.imgLabel.setPixmap(QPixmap.fromImage(outImage))
            self.imgLabel.setScaledContents(True)


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
