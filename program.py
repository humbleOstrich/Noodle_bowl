import sys
import random

from PyQt5.QtGui import QColor, QPen, QBrush, QPainter
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 600, 600, 600)
        self.setWindowTitle('Супрематизм')
        self.btn = QPushButton(self)
        self.btn.move(0, 0)
        self.btn.resize(100, 20)
        self.btn.setText("Нарисовать круг")
        self.x = 0
        self.y = 0
        self.btn.clicked.connect(self.update)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.drawCircle(painter)
        painter.end()

    def drawCircle(self, painter):
        color_1 = random.randint(1, 255)
        color_2 = random.randint(1, 255)
        color_3 = random.randint(1, 255)
        pen = QPen(QColor(color_1, color_2, color_3))
        brush = QBrush(QColor(color_1, color_2, color_3))
        painter.setPen(pen)
        painter.setBrush(brush)
        rad = random.randint(10, 300)
        self.x = random.randint(10, 1000)
        self.y = random.randint(10, 1000)
        painter.drawEllipse(self.x - rad, self.y - rad, rad * 2, rad * 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
