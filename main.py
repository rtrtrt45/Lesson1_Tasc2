import sys
import random
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow



class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw(self, qp):
        x = random.randrange(0, 400)
        y = random.randrange(0, 400)
        w_h = random.randrange(10, 100)
        qp.setPen(QPen(QColor(255, 247, 0), 6))
        qp.drawEllipse(x, y, w_h, w_h)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
