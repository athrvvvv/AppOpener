import os, json, sys, psutil, subprocess, difflib

# COLORSHEET FOR TERMINAL WARNINGS !
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

os.system("")

# Get path of working directory
def get_path():
    if getattr(sys, 'frozen', False):
        main_path = os.path.dirname(sys.executable)
        return main_path
    elif __file__:
        main_path = os.path.dirname(__file__)
        return main_path

main_path = os.path.join(get_path(),"Data")

# FUNCTION FOR OPENING APPLICATIONS
def open_things(self, output=True, open_closest=False):
    with open ((os.path.join(main_path,"data.json")),"r") as f:
        data1 = json.load(f)
        keys = data1.keys()
        try:
            dir01 = data1[self]
            os.system("explorer shell:appsFolder\\"+dir01)
            if output:
                print("OPENING "+self.upper())
        except:
            result = difflib.get_close_matches(self,keys, n=1)
            app_name = ' '.join(result).strip()
            if result:
                if output:
                    print("Closest match to "+self.upper()+" : "+str(result))
                if open_closest:
                    os.system("explorer shell:appsFolder\\"+app_name)
                    if output:
                        print("OPENING "+app_name.upper())
            else:
                if output:
                    print(f"{self.upper()} NOT FOUND... TYPE (LS) for list of applications.")
            pass

# CLOSE SEVERAL THINGS :)
def close_things(self, output=True, close_closest=False):
    if not self.endswith(".exe"):
        self = (self+".exe")
    flag = False
    if not close_closest:
        for pid in psutil.pids():
            try:
                process = psutil.Process(pid)
                if process.name() == self:
                    process.kill()
                    if not flag and output:
                        print("CLOSING "+(self.replace(".exe","")).upper())
                        flag = True
            except: pass
        if not flag and output:
            print((self.replace(".exe","")).upper() +" is not running")
    if close_closest:
        app_jug = []
        for pid in psutil.pids():
            try:
                process = psutil.Process(pid)
                app_jug.append((process.name()))
            except: pass
        result = difflib.get_close_matches(self,app_jug, n=1)
        app_name = ' '.join(result).strip()
        # print(app_jug)
        # print(app_name)
        command = ['taskkill', '/f', '/im',app_name]
        # print(command)
        with open('NUL', 'w') as null:
            process = subprocess.Popen(command, stdout=null, stderr=null)
            process.wait()
            if process.returncode == 0:
                if output:
                    print("CLOSING "+(app_name.replace(".exe","")).upper())
            else:
                if output:
                    print((self.replace(".exe","")).upper() +" is not running")

# FIND APPLICATION IF INSTALLED OR NOT :)
def find_apps(self):
    with open((os.path.join(main_path,"app_names.json")),"r") as f:
        data = json.load(f)
        keys = list(data.keys())
        values = list(data.values())
        for i in keys:
            if self in i or self == i:
                position = keys.index(i)
                app = values[position]
                if app == "":
                    app2 = app.upper()
                elif app != "":
                    app2 = ("("+app.upper()+")")
                print(i.upper()+" "+app2)

# SEE PETANME(s) OF ORIGINAL APP(s)
def change_log(self):
    os.system("")
    if self == "log":
        with open((os.path.join(main_path,"app_names.json")),"r") as f:
            data = json.load(f)
            keys = list(data.keys())
            values = list(data.values())
            for i in values:
                if i != "":
                    position = values.index(i)
                    app = keys[position]
                    print(style.RED+(app.upper())+style.WHITE+" > "+style.GREEN+(i.upper())+style.RESET)
    else:
        with open((os.path.join(main_path,"app_names_temp.json")),"r") as f:
            data = json.load(f)
            keys = list(data.keys())
            values = list(data.values())
            for i in values:
                if i != "":
                    position = values.index(i)
                    app = keys[position]
                    print(style.RED+(app.upper())+style.WHITE+" > "+style.GREEN+(i.upper())+style.RESET)

# LISTING APP(s) LIST - 2
def list_apps():
    print()
    with open((os.path.join(main_path,"data.json")),"r") as file:
        data = json.load(file)
        key = data.keys()
        keys = sorted(key)
        count = 0
        for app in keys:
            if len(app.strip()) == 0 :
                continue
            else:
                count += 1
                print("{}. {}".format(count, app.strip().upper()))
    print()

# Give dictionary of appnames (Uppercase or lowercase)
def give_appnames(upper=False):
    with open((os.path.join(main_path,"data.json")),"r") as file:
        data = json.load(file)
    keys = data.keys()
    if upper == True:
        dict = {}
        for k in keys:
            change = {k.upper() : None}
            dict.update(change)
        keys_upper = dict.keys()
        return keys_upper
    if upper == False:
        return keys