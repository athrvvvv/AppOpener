Here, we will explore the several Examples of using module for several purposes.

<font size=5>1. Basic 🧐</font>

### `Open application`

``` python
from AppOpener import open
open("telegram")
#This will open telegram if installed else pass it.
```

### `Open multiple applications`

``` python
from AppOpener import open
open("telegram, whatsapp")
#This will open telegram & whatsapp one-by-one if installed else pass the app which is not installed.
```

### `Open application without printing context`

``` python
from AppOpener import open
open("telegram", output=False)
#This will open telegram, without printing any output text.
```

### `Close application without printing context`

``` python
from AppOpener import close
close("telegram", output=False)
#This will close telegram, without printing any output text.
```

<br>

---

<font size=5>2. Open Applications 🔥</font>

[//]: # (Using <u>SUB-COMMANDS</u> of `OPEN` function.)


| Command      | Description                          |
| :---------- | :----------------------------------- |
| `?`       | See this beatiful Documentation.  |
| `VERSION`       | Print AppOpener version.  |
| `LS`       | Print list of applications.  |
| `HELP`    | Print supported commands. |
| `FIND XYZ`       | Find application / applications. |
| `RENAME -M`    | Update petnames manually. |
| `OLDNAME > NEWNAME`    | Update petname via command line. |
| `UPDATE`    | Load new appnames and appids. |
| `DEFAULT`    |Restore sefault appnames. |
| `LOG`    | Print changes in petnames. |
| `Q`    | Exit program. |

| Attribute      | Description                          |
| ----------- | ------------------------------------ |
| `match_closest=True`    | Open application which matches closest to string.                 |
| `output=False`    | Do not print any output text.                   |

### USING ATTRIBUTES 🌟

&nbsp; 1. `USING <OPEN> function`

``` python
from AppOpener import open
open("brave")
#open brave applciation
```

&nbsp; 2. `Using <match_closest> attribute `

``` python
from AppOpener import open
open("barve, telgrm", open_openst=True)
# Here, application detects the closest match of provided string (i.e barve is brave and telgrm is telegram)
```

&nbsp; 3. `Using <output> attribute`

``` python
from AppOpener import open
open("brave", output=False)
# No printing context (like 'OPENING BRAVE')
```


### USING FEATURES ✨
&nbsp; 1. `LS - LISTING APPNAMES`

``` python
from AppOpener import open
open("ls")
#See list of appnames
```

&nbsp; 2. `HELP - QUICK COMMANDS`

``` python
from AppOpener import open
open("help")
#See supported commands
```

&nbsp; 3. `FIND XYZ - SEARCH APPLICATIONS`

Find applications present in data or not. If any mentioned application is not found in data, it will return nothing else it will return what founded.

``` python
from AppOpener import open
open("find whatsapp, telegram")
```

&nbsp; 4. `RENAME -M - RENAME APPNAMES MANUALLY.`

Change names of applications as per your choice. Your default code editor will be opened as soon as the command is entered. **Changes will be done after reloading of module**.

``` python
from AppOpener import open
open("rename -m")
```

&nbsp; 5. `OLDNAME > NEWNAME - RENAME APPLICATIONS VIA CLI`

Consider, updating petnames via command line. Name any application as per your choice.

``` python
from AppOpener import open
open("firefox > fire, brave > bravely")
# Here, firefox & brave will be named as fire & bravely respectively.
```

&nbsp; 6. `UPDATE - FETCH ALL NEW APPLICATIONS`

Assume, you installed some more <u>naughty</u> applications so now, how can you **fetch all new apps??** Simple by **UPDATE command**.

``` python
from AppOpener import open
open("update")
#Fetch all apps, if any.
```

&nbsp; 7. `DEFAULT - RESTORE DEFAULT APPNAMES`

Consider, you wanna make **all** your names changes go brhhhh. You can use **DEAFULT** command.

``` python
from AppOpener import open
open("default")
```

&nbsp; 8. `LOG - SEE PETNAMES`

One fine day you wanna see your renames appnames (PETNAMES). You can simply use **LOG** command, which will show you your current appname changes.

``` python
from AppOpener import open
open("log")
#See petnames
```

Also, to see **all** appnames changes.

``` python
from AppOpener import open
open("log -c")
#See complete petnames even if duplicate petnames are available.
```

<br>

---

<font size=5>3. Closing Applications 😎</font>

[//]: # (Using <u>ATTRIBUTES</u> of `CLOSE` function.)

| Attribute      | Description                          |
| ----------- | ------------------------------------ |
| `match_closest=True`    | Close application which matches closest to string.                 |
| `output=False`    | Do not print any output text.                   |

&nbsp; 1. `USING <CLOSE> function`

``` python
from AppOpener import close
close("brave")
#Close brave applciation
```

&nbsp; 2. `Using <match_closest> attribute `

``` python
from AppOpener import close
close("barve, telgrm", match_closest=True)
# Here, application detects the closest match of provided string (i.e barve is brave and telgrm is telegram)
```

&nbsp; 3. `Using <output> attribute `

``` python
from AppOpener import close
close("brave", output=False)
# No printing context (like 'CLOSING BRAVE')
```

<br>

---

<font size=5>4. Listing 📃</font>

<u>Makelist</u> of **APPNAMES** & **APPIDS**

Sometimes we need list of applications installed in our system. In curiosity if you want list of Appnames or AppIds

You can make use of `MKLIST` function.

MKLIST function accepts 3 attributes.

| Attribute      | Description                          |
| ----------- | ------------------------------------ |
| `filename=`       | Filename of file to be created.                      |
| `path=`       | Path of folder where file is to be created.
| `output=False`    | Do not print any output text.                   |


&nbsp; 1. `GENERAL`

``` python
from AppOpener import mklist
mklist()
```

Here **no attribute** is used so it creates JSON file **'app_data.json'**, in your **orking directory** by <u>default</u>.

&nbsp; 2. `FILENAME=`

Assume, you want the name of list to be generated as per your choice. You can simply use **FILENAME** attribute.

Creating <u>JSON</u> format file.

``` python
from AppOpener import mklist
mklist(filename="data.json")
#data.json file will be created in your working directory.
```

Creating <u>TXT</u> format file.

``` python
from AppOpener import mklist
mklist(filname="data.txt")
#data.txt file will be created in your working directory.
```

&nbsp; 3. `PATH=`

Assume, you want list generated in other directory. You can simply use **PATH**.

``` python
from AppOpener import mklist
mklist(path=r"C:\Users\athar\Documents\projects\AppOpener")
#app_data.json file will be created in the provided directory.
```

&nbsp; 4. `output=`

Assume, you just want module to work without displaying anything. You can simply use **OUTPUT** attribute.

``` python
from AppOpener import mklist
mklist(name="app_names.json", output=False)
#app_names.json file will be created, without printing any output text.
```

&nbsp; 4. `INTEGRATING MKLIST with OPEN function`

Mix baby!!

``` python
from AppOpener import open
open("mklist")
#app_data.json file will be created in your working directory.
```
---

<font size=5>5. Fetching appnames as dictionary 🔡</font>

Making use of `give_appnames` function to fetch appnames as dictionary, that can be used for several purpopses. (Ex. use it for autocomplete)


| Attribute      | Description                          |
| ----------- | ------------------------------------ |
| `upper=`       | Dictionary should be uppercase               |

&nbsp; 1. `GENERAL`

``` python
from AppOpener import give_appnames
apps = give_appnames()
print(apps) # Print appnames as (Dictionary)
```

This can be also used for **Autocompletion** of appnames with the help of <a href="https://pypi.org/project/pyreadline3/" target="_blank">pyreadline3</a>.


&nbsp; 2. `UPPER=`

This attribute is type of **<u>bool</u>**. If you want dictionary in **uppercase** you must use this.

``` python
from AppOpener import give_appnames
apps = give_appnames(upper=True)
print(apps) # Print appnames in uppercase as (Dictionary)
```
Supportive example can be found [here](Applications.md).
