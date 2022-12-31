Here, we will explore the several real life applications using module.

## 1. Command Line Interface 😘

* <font size=4>Approach </font>: Here, program runs in infinite loop taking input from user and running it in via `OPEN` function.

* <font size=4>Dependencies :</font>
```
pip install AppOpener
```

``` python
from AppOpener import open, close

def main():
    print()
    print("1. Open <any_name> TO OPEN APPLICATIONS")
    print("2. Close <any_name> TO CLOSE APPLICATIONS")
    print()
    open("help")
    print("TRY OPEN <KEY>")
    print()
    while True:
        inp = input("ENTER APPLICATION TO OPEN / CLOSE: ").lower()
        if "close " in inp:
            app_name = inp.replace("close ","").strip()
            close(app_name, close_closest=True, output=False) # App will be close be it matches little bit too (Without printing context (like CLOSING <app_name>))
        if "open " in inp:
            app_name = inp.replace("open ","")
            open(app_name, open_closest=True) # App will be open be it matches little bit too

if __name__ == '__main__':
    main()
```

## 2. Command Line Interface (Autocomplete) 😍

* <font size=4>Approach </font>: Here, program runs in infinite loop but after entering some of part of appname and pressing `TAB` it tries to autocomplete it.

* <font size=4>Dependencies :</font>
```
pip install AppOpener, pyreadline3
```

``` python
from AppOpener import give_appnames, open
import readline

class MyCompleter(object):
    def __init__(self, options):
        self.options = sorted(options)
    def complete(self, text, state):
        if state == 0:
            if text:
                self.matches = [s for s in self.options if s and s.startswith(text)]
            else:
                self.matches = self.options[:]
        try:
            return self.matches[state]
        except IndexError:
            return None

tags = give_appnames() # FETCH ALL APPNAMES AS DICTIONARY

completer = MyCompleter(tags)

readline.set_completer(completer.complete)
readline.parse_and_bind('tab: complete')

print("PRESS 'TAB' to autocomplete")

while True:
    inp = input("ENTER APPNAME TO OPEN: ")
    open(inp)
```

## 3. PyQt5 Application 😎

* <font size=4>Approach </font>: PyQt5 application, which uses AppOpener to run entered application name.

* <font size=4>Dependencies :</font>
```
pip install AppOpener, PyQt5
```

``` python
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
        AppOpener.open(str(text))
        self.label.setText(str("Looking for "+text.strip()))
        self.text_area.clear()
        self.text_area.setFocus()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
```

## 4. Tkinter Application 😋

* <font size=4>Approach </font>: Tkinter application, which uses AppOpener to run entered application name.

* <font size=4>Dependencies :</font>
```
pip install AppOpener, tk
```

``` python
import tkinter as tk
import AppOpener

# Create the root window
root = tk.Tk()
root.title("AppOpener with Tkinter")

# Set the size and position of the window using the geometry() method
root.geometry("500x500+{}+{}".format(int(root.winfo_screenwidth()/2 - 350), int(root.winfo_screenheight()/2 - 350)))

# Create the text area
text_area = tk.Text(root, height=10, width=30, font=("Helvetica", 20))
text_area.pack()

# Create the button
button = tk.Button(root, text="Submit", font=("Helvetica", 20))
button.pack()

# Create the label
label = tk.Label(root, text="", font=("Helvetica", 20))
label.pack()
text_area.focus()
# Define the function to be called when the button is clicked
def submit(event):
  # Get the text entered in the text area
  text = text_area.get("1.0", "end")
  AppOpener.open(str(text))
  # Set the text of the label to the entered text
  label.config(text=str("Looking for "+text))
  # Clear the text area
  text_area.delete("1.0", "end")

# Bind the submit function to the button's click event
button.bind("<Button-1>", submit)

# Bind the "Return" key to the button's click event
root.bind("<Return>", submit)

# Start the main event loop
root.mainloop()
```