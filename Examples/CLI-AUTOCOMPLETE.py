from AppOpener import open, close, give_appnames
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
print()
print("1. open 'app_name' TO OPEN APPLICATIONS")
print("2. close 'app_name' TO CLOSE APPLICATIONS")
print()
while True:
    inp = input("ENTER APPNAME: ").strip()
    if "open " in inp:
        app_name = inp.replace("open ","")
        open(app_name,output=False,match_closest=True)
    if "close " in inp:
        app_name = inp.replace("close ","")
        close(app_name,output=False)

