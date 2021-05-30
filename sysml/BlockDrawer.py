from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QBrush
import sys

from sysml.Block import Block


class BlockDrawer(QWidget):

    def __init__(self):
        super().__init__()
        self.init_container()

    def init_container(self):
        self.setGeometry(500, 200, 800, 800)
        self.setWindowTitle('test')
        self.show()
        block = Block(block_x=20, block_y=20, block_w=200, block_h=100, name='simple')

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_form(qp)
        qp.end()

    def draw_form(self, qp):
        qp.drawRect(self.block.block_x, self.block_y, self.block_w, self.block_h)
        qp.drawText(self.block_w / 2, self.block_y * 2, self.block.header)
        qp.drawText(self.block_w / 3, self.block_y * 3, self.block.name)

        print(self.block_w / 2)


def main():
    app = QApplication(sys.argv)
    ex = BlockDrawer()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
