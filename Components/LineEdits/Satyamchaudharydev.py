from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import QAction, QIcon

from resources import rc_icons

Satyamchaudharydev_stylesheet = """
    QLineEdit {
        border: none;
        background: none;
        color: #8b8ba7;
        padding-inline: 0.5em;
        padding-block: 0.7em;
        font-size: 30px;
        border-radius: 15px;
    }

"""


class Satyamchaudharydev(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setClearButtonEnabled(True)
        self.setFrame(False)
        self.findChildren(QAction)[0].setIcon(QIcon(":/resources/icons/x.svg"))
        self.search_action = self.addAction(QIcon(":/resources/icons/search.svg"),
                                            QLineEdit.ActionPosition.LeadingPosition)
        self.setStyleSheet(Satyamchaudharydev_stylesheet)
        self.search_action_trigger = self.search_action.triggered
        self.setPlaceholderText("Type your text")

        self.search_action_trigger.connect(self.default_search_event)

    def default_search_event(self):
        print("Default Search Event triggered")
