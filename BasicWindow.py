import sys
from PyQt5 import QtWidgets, QtGui


# Creating window, label, pixel image and button

def window():
    # ----- Create widgets as w -----------------
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()

    # ----- Create label l1 and put some text ---
    l1 = QtWidgets.QLabel(w)
    l1.setText('Open SOURCE')
    l1.move(10, 100)

    # ----- Create label and put jpg on it ------
    l2 = QtWidgets.QLabel(w)
    l2.setPixmap(QtGui.QPixmap('open1.jpg'))
    l2.move(0, 0)

    # ----- Create button -----------------------
    b1 = QtWidgets.QPushButton(w)
    b1.setText('Push Here')
    b1.move(10, 120)

    # ----- Set window parameter ----------------
    w.setWindowTitle('PyQt5 Lessons')
    w.setGeometry(100, 100, 300, 300)
    w.show()
    sys.exit(app.exec_())


window()
