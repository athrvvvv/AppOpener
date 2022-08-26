Hello, developers!! here we will explore the working of <a href="https://pypi.org/project/AppOpener/" target="_blank">AppOpener</a>. Learning how is data is generated and how it is used.

The source code is always available at the Github <a href="https://github.com/athrvvvv/AppOpener/" target="_blank">repository</a>.

---

**<font size="6">Ⅰ. Configuration</font>** 

&nbsp; 1. `Fetch Appnames & IDS via Command Line`

``` python
import os, json, win32gui, win32con

def maximize():
    hwnd = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

def check_reference():                               
    maximize()
    os.system("mode 800")
    print("LOADING APPS... (JUST ONCE)")
    os.system("powershell -command "+'"'+"get-StartApps | Out-File -Filepath "+"'"+"reference.txt"+"'"+'"')
    with open("reference.txt","r") as fd:
        lines = fd.read()
        lines2 = str(lines).encode().decode("utf-16le")
    with open("refer.txt","a+",encoding="utf-8") as fp:
        fp.write(lines2)
    with open("refer.txt","r") as f:
        data = ("".join(line for line in f if not line.isspace()))
        # print(data)
    os.remove("reference.txt")
    os.remove("refer.txt")
    with open("reference.txt","w+") as f2:
        f2.write(data)
    fd = open("reference.txt","r") 
    lines = fd.readlines()
    line = []
    with open("reference.txt","w") as fp:
        for number, line in enumerate(lines):
            if number not in [0, 1,2]:
                fp.write(line)
    with open("reference.txt","r") as f, open("reference_temp.txt","w+") as outfile:
        for i in f.readlines():
            if not i.strip():
                continue
            if i:
                outfile.write(i)
    os.system("mode 100")
```

Here, python...

- Maximises console so it gets long length APPIDS (Ex. windows mail)
- Creates **referece.txt** file where APPNAMES & APPIDS are stored but encoded in **utf-16le** by default.
- Convert **utf-16le** to **utf-8** format.
- Create multiple files & remove multiple files.
- Minimises console.

&nbsp; 2. `CONVERT TXT to JSON`

``` python
import os, json, re
def convert_txt_json():
    dictionary ={}
    with open("data.json"),"w") as outfile:
        json.dump(dictionary,outfile,indent = 4)
    file1 = open('reference.txt','r')
    Lines = file1.readlines()
    for line in Lines:
        line1= line.strip()
        index = line1.find('  ')
        # HERE line1[:index] is the APP-NAME
        # HERE line1[index:] is the APP-ID.
        app_name = line1[:index]
        app_id = (line1[index:]).strip()
        is_digit = app_name[:1].isdigit()
        with open ("data.json","r") as f:
                data = json.load(f)
        if is_digit == (False):
            val=(re.compile(r'[^a-z-&]')).sub(" ",(app_name.lower()))
            final_app_name = re.sub(' +', ' ', val).strip()
            change = {final_app_name:app_id}
            data.update(change)
            with open("data.json","a+") as f:
                g = open("data.json"),"r+")
                g.truncate(0)
                json.dump(data,f,indent=4)
        elif is_digit == (True):
            val=(re.compile(r'[^a-z-&^0-9]')).sub(" ",(app_name.lower()))
            final_app_name = re.sub(' +', ' ', val).strip()
            change = {final_app_name:app_id}
            data.update(change)
            with open("data.json"),"a+") as f:
                g = open("data.json","r+")
                g.truncate(0)
                json.dump(data,f,indent=4)
```

Here, python..

- Makes **"data.json"** file where appnames & appids are stored as values & keys respectively.
- Filters out multiple words program to short names.
- Runs condition for appname starting with number or ending with number. (Ex. 7-Zip, Notepad3, ect.)

&nbsp; 3. `Use data for running apps`

``` python
import os, json
from difflib import get_close_matches
def open_things(self):
    with open ("data.json","r") as f:
        data1 = json.load(f)
        keys = data1.keys()
        try:
            dir01 = data1[self]
            os.system("explorer shell:appsFolder\\"+dir01)
            print("OPENING "+self.upper())
        except:
            result = get_close_matches(self,keys)
            if bool(result) == (True):
                print("Closest match to "+self.upper()+" : "+str(result))
            else:
                print(f"{self.upper()} NOT FOUND... TYPE (LS) for list of applications.")
            pass
open_things("whatsapp")
```

Here, python...

- Load AppNames as keys and use those to find their AppIds.
- Run applications via os command `explorer shell:appsFolder\\"+appid`

--- 

**<font size="6">Ⅱ. Features</font>** 

| Command      | Description                          |
| :---------- | :----------------------------------- |
| `LS`       | Print list of applications.  |
| `HELP`    | Print supported commands. |
| `FIND XYZ`       | Search application / applications. |
| `RENAME -M`    | Update petnames manually. |
| `OLDNAME > NEWNAME`    | Update petname via command line. |
| `UPDATE`    | Load new appnames and appids. |
| `DEFAULT`    |Restore sefault appnames. |
| `LOG`    | Print changes in petnames. |


&nbsp; 1. `LS - LISTING OF APPNAMES`

``` python
import json
def list_apps():
    print()
    with open("data.json"),"r") as file:
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
list_apps()
```

Here, python...

- Prints keys (AppNames) in UPPERCASE.

&nbsp; 2. `HELP - Quick Commands`

``` python
def commands():
    data = [['KEY', 'USE'],
            ['(?)','DOCUMENTATION'],
            ['(LS)','LIST OF APPLICATIONS'],
            ['(FIND XYZ)', "FIND APPLICATION"],
            ['(RENAME -M)','RENAME APPNAMES MANUALLY'],
            ['(UPDATE)','LOAD NEW DATA'],
            ['(OLD > NEW)','UPDATE APP VIA CLI'],
            ['(DEFAULT)','RESTORES DEFAULT APPNAMES'],
            ['(LOG)','SEE CHANGED PETNAME(s)'],
            ['(CLS)','CLEARS SCREEN'],
            ['(Q)','EXIT PROGRAM']      
            ]
    dash = '-' * 35
    for i in range(len(data)):
        if i == 0:
            print(dash)
            print('{:<15s}{:^15s}'.format(data[i][0],data[i][1]))
            print(dash)
        else:
            print('{:<15s}{:^12s}'.format(data[i][0],data[i][1]))
```

Here, python...

- Print Keys and their uses in table format.

&nbsp; 3. `FIND XYZ - Search Applications`

``` python
import json
def find_apps(self):
    with open("app_names.json","r") as f:
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
find_apps("telegram, whatsapp")
```

Here, python...

- Prints if applications present else pass it.

&nbsp; 4. `RENAME -m - Rename appnames manually.`

``` python
os.startfile("app_names.json")
print("RELOAD PROGRAM TO APPEND CHANGES")
```

Here, python...

- Opens `app_names.json` in the default text editor.