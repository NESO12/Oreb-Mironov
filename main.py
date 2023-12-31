import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from random import randint
from PyQt5 import uic
from UI import Ui_MainWindow


class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flag = False
        self.btn.clicked.connect(self.draw())

    def draw(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            color = QColor(255, 255, 0)
            qp.setPen(color)
            qp.setBrush(color)
            r = randint(10, 100)
            x, y = randint(0, 500 - r), randint(0, 500 - r)
            qp.drawEllipse(x, y, r, r)

            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())
