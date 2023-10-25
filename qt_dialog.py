# pylint: disable=astroid-error

import sys

from PySide6.QtWidgets import (
    QApplication, 
    QDialog, 
    QLineEdit, 
    QPushButton,
    QVBoxLayout,
    QMessageBox,
)

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # super().__init__()
        self.setWindowTitle("Qt Example - Form")

        # Create widgets
        self.edit = QLineEdit("Name ...")
        self.button = QPushButton("Show Greetings")

        layout = QVBoxLayout(self)
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

        self.button.clicked.connect(self.greetings)
    #:

    def greetings(self):
        msg_box = QMessageBox()
        msg_box.setText(self.edit.text())
        msg_box.setIcon(QMessageBox.Information)
        msg_box.exec()
    #:
#:

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())
