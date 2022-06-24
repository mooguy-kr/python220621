# mytest.py

import sys
from PyQt5.Qt import QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import QWidget, QLineEdit, QFormLayout


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.e1 = QLineEdit()
        self.e1.setValidator(QIntValidator())
        self.e1.setMaxLength(4)
        self.e1.setAlignment(Qt.AlignRight)

        # This control will focus using the tab key
        self.e1.setFocusPolicy(Qt.ClickFocus | Qt.TabFocus)

        e2 = QLineEdit()
        e2.setValidator(QDoubleValidator(0.99, 99.99, 2))

        # This control will not focus using the tab key
        e2.setFocusPolicy(Qt.ClickFocus | Qt.NoFocus)

        self.flo = QFormLayout()
        self.flo.addRow("integer validator", self.e1)
        self.flo.addRow("Double validator", e2)

        e3 = QLineEdit()
        e3.setInputMask('+99_9999_999999')
        self.flo.addRow("Input Mask", e3)

        # This control will not focus using the tab key
        e3.setFocusPolicy(Qt.ClickFocus | Qt.NoFocus)

        e4 = QLineEdit()
        self.flo.addRow("Text changed", e4)

        # This control will focus using the tab key (this is the default behaviour you don't need to explicitly set it)
        e4.setFocusPolicy(Qt.ClickFocus | Qt.TabFocus)

        # Default focus behaviour
        e5 = QLineEdit()
        e5.setEchoMode(QLineEdit.Password)
        self.flo.addRow("Password", e5)

        e6 = QLineEdit("Hello Python")
        e6.setReadOnly(True)
        self.flo.addRow("Read Only", e6)

        self.setLayout(self.flo)
        self.setWindowTitle("Example")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())