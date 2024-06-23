from PySide6.QtCore import QEasingCurve, QPropertyAnimation, QPoint
from PySide6.QtWidgets import QPushButton, QGraphicsDropShadowEffect
from PySide6.QtGui import QColor

CSSButtonsIO_stylesheet = """
QPushButton#CSSButtonsIO {
  padding: 1.3em 3em;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 2.5px;
  font-weight: 500;
  color: #000;
  background-color: #fff;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  outline: none;
}

QPushButton#CSSButtonsIO:hover {
  background-color: #23c483;
  
  color: #fff;
}
"""


class CSSButtonsIO(QPushButton):
    def __init__(self):
        super().__init__()
        self.setObjectName("CSSButtonsIO")
        self.setStyleSheet(CSSButtonsIO_stylesheet)
        self.setText("BUTTON")
        self.animation_up = QPropertyAnimation(self, b"pos")
        self.animation_down = QPropertyAnimation(self, b"pos")
        self.original_position = None
        self.is_hovered = False
        self.hover_offset = QPoint(0, -7)
        self.setup_shadow_effect()

    def setup_animations(self):
        self.animation_up.setDuration(200)
        self.animation_up.setStartValue(self.pos())
        self.animation_up.setEndValue(self.pos() + self.hover_offset)
        self.animation_up.setEasingCurve(QEasingCurve.InOutCubic)

        # Animation to move the button back to original position
        self.animation_down.setDuration(200)
        self.animation_down.setStartValue(self.pos() + self.hover_offset)
        self.animation_down.setEndValue(self.pos())

    def setup_shadow_effect(self):
        # box-shadow: 0px 15px 20px rgba(46, 229, 157, 0.4);
        shadow = QGraphicsDropShadowEffect(self)
        if self.is_hovered:
            shadow.setXOffset(0)
            shadow.setYOffset(8)
            shadow.setBlurRadius(15)
            shadow.setColor(QColor(0, 0, 0, 25))  # 10% opacity (25/255)
        else:
            shadow.setXOffset(0)
            shadow.setYOffset(15)
            shadow.setBlurRadius(20)
            shadow.setColor(QColor(0, 0, 0, 100))  # 40% opacity (25/255)
        self.setGraphicsEffect(shadow)

    def enterEvent(self, event):
        self.is_hovered = True
        if self.original_position is None:
            self.original_position = self.pos()
            self.setup_animations()

        self.animation_down.stop()  # Stop the down animation if it's running
        self.animation_up.setStartValue(self.pos())  # Update start position dynamically
        self.animation_up.setEndValue(self.pos() + self.hover_offset)
        self.animation_up.start()
        self.setup_shadow_effect()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.is_hovered = False
        self.animation_up.stop()  # Stop the up animation if it's running
        self.animation_down.setStartValue(self.pos())  # Update start position dynamically
        self.animation_down.setEndValue(self.original_position)
        self.animation_down.start()
        self.setup_shadow_effect()
        super().leaveEvent(event)

    def showEvent(self, event):
        super().showEvent(event)
        if self.original_position is None:
            self.original_position = self.pos()
            self.setup_animations()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if self.original_position is not None:
            self.original_position = self.pos()
            self.setup_animations()
            if self.is_hovered:
                self.animation_up.stop()
                self.animation_up.setStartValue(self.pos())
                self.animation_up.setEndValue(self.original_position + self.hover_offset)
                self.animation_up.start()
            else:
                self.animation_down.stop()
                self.animation_down.setStartValue(self.pos())
                self.animation_down.setEndValue(self.original_position)
                self.animation_down.start()
        self.setup_shadow_effect()