import sys

from PySide6.QtWidgets import QVBoxLayout, QApplication, QMainWindow, QFrame
from Components.LineEdits.Satyamchaudharydev import Satyamchaudharydev


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        # Create an instance of the CustomQPushButton
        frame = QFrame(self)
        frame.setGeometry(290, 180, 300, 300)
        layout = QVBoxLayout(frame)
        button = Satyamchaudharydev(frame)
        layout.addWidget(button)

        self.setWindowTitle('Custom QPushButton Example')
        self.setGeometry(300, 300, 800, 600)


# Main function to run the application
def main():
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
