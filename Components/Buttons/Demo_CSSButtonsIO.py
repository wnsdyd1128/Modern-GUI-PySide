import sys
from PySide6.QtWidgets import *

from Components.Buttons.CSSButtonsIO import CSSButtonsIO


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        # Create an instance of the CustomQPushButton
        button = CSSButtonsIO()
        layout.addWidget(button)

        self.setLayout(layout)
        self.setWindowTitle('Custom QPushButton Example')
        self.setGeometry(300, 300, 300, 200)


# Main function to run the application
def main():
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
