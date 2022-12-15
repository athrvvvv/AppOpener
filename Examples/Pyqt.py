import sys, AppOpener
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QTextEdit, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QRect

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # get the screen dimensions and calculate the center position
        screen_geometry = QApplication.desktop().screenGeometry()
        x = (screen_geometry.width() - self.width()) / 2
        y = (screen_geometry.height() - self.height()) / 2

        # cast the center coordinates to int and set the window dimensions
        x = int(x)
        y = int(y)
        self.setGeometry(x, y, 500, 500)
        self.setWindowTitle('AppOpener with Pyqt')

        # create text area and submit button
        self.text_area = QTextEdit(self)
        self.text_area.setFont(QFont('SansSerif', 20))
        self.submit_btn = QPushButton('Submit', self)
        self.submit_btn.clicked.connect(self.on_submit)

        # set the submit button's shortcut to the Return key
        self.submit_btn.setShortcut('Return')

        # create label for displaying text
        self.label = QLabel(self)
        self.label.setFont(QFont('SansSerif', 20))

        # use a vertical layout to arrange the text area, submit button, and label
        layout = QVBoxLayout()
        layout.addWidget(self.text_area)
        layout.addWidget(self.submit_btn)
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.show()


    def on_submit(self):
        text = self.text_area.toPlainText()
        AppOpener.run(str(text))
        self.label.setText(str("Looking for "+text.strip()))
        self.text_area.clear()
        self.text_area.setFocus()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
