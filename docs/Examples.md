Here, we will explore the several Examples of using module for several purposes.

## Basics

### a. Open application

``` { .py .copy }
from AppOpener import open
open("telegram") # Opens telegram if installed
open("telegram, whatsapp") # Opens telegram & whatsapp 
open("telgrm, whutspp", match_closest=True) # Opens telegram and whatsapp
```

### b. Close application

``` { .py .copy }
from AppOpener import close
close("telegram") # Closes telegram if it is running
close("telegram, whatsapp") # Closes telegram & whatsapp
close("telgrm, whutspp", match_closest=True) # Closes telegram and whatsapp
```

### c. Do not print context

``` { .py .copy }
from AppOpener import open, close
open("telegram", output=False) #Opens telegram without printing anything (i.e OPENING TELEGRAM).
close("whatsapp", output=False) #Same thing
```

---

## Functions of AppOpener:

### 1. Open

> Attributes

| Attribute      | Description                          |
| ----------- | ------------------------------------ |
| `<match_closest>`    | Open application which matches closest to string.                 |
| `<output>`    | Do not print any output text.         |

> Examples:

**a. Using `<match_closest>` attribute.**

``` { .py .copy }
from AppOpener import open
open("barve, telgrm", match_closest=True)
# Here, module detects the closest match of provided string (i.e barve is brave and telgrm is telegram)
```

**b. Using `<output>` attribute**

``` { .py .copy }
from AppOpener import open
open("brave", output=False)
# No printing context (like 'OPENING BRAVE')
```

> Commands

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
| `DEFAULT`    |Restore default appnames. |
| `LOG`    | Print changes in petnames. |
| `LOG -C`    | Print complete changes in petnames. |


Commands can be accessed through `OPEN` function

> Example: 

``` { .py .copy}
from AppOpener import open
open("version") # Prints version of AppOpener
open("ls") # Lists installed applications
``` 

### 2. Close

> Attributes

| Attribute      | Description                          |
| ----------- | ------------------------------------ |
| `<match_closest>`    | Close application which matches closest to string.                 |
| `<output>`    | Do not print any output text.              |


> Examples:

**a. Using `<match_closest>` attribute**

``` { .py .copy}
from AppOpener import close
close("barve, telgrm", match_closest=True)
# Here, module detects the closest match of provided string (i.e barve is brave and telgrm is telegram)
```

**b. Using `<output>` attribute**

``` { .py .copy }
from AppOpener import close
close("brave", output=False)
# No printing context (like 'CLOSING BRAVE')
```
  
### 3. Mklist

Sometimes we need list of applications installed in our system. In curiosity if you want list of Appnames or AppIds

You can make use of `MKLIST` function.

> Attributes

| Attribute      | Description                          |
| ----------- | ------------------------------------ |
| <filename>       | Filename of file to be created.       |
| <path>      | Path of folder where file is to be created.
| <output>    | Do not print any output text.                   |

> Examples:

a. General

``` { .py .copy }
from AppOpener import mklist
mklist()
```

Here **no attribute** is used so it creates JSON file **'app_data.json'**, in your **orking directory** by <u>default</u>.

b. Using `<filename>` attributes

Creating <u>JSON</u> format file.

``` { .py .copy }
from AppOpener import mklist
mklist(filename="data.json")
#data.json file will be created in your working directory.
```

Creating <u>TXT</u> format file.

``` { .py .copy }
from AppOpener import mklist
mklist(filname="data.txt")
#data.txt file will be created in your working directory.
```

c. Using `<path>` attribute

``` python
from AppOpener import mklist
mklist(path=r"C:\Users\athar\Documents\projects\AppOpener")
#app_data.json file will be created in the provided directory.
```
  
d. Using `<output>` attribute

``` { .py .copy }
from AppOpener import mklist
mklist(name="app_names.json", output=False)
#app_names.json file will be created, without printing any output text.
```
  
e. Integrating `mklist` with `open` function

Mix it baby!!

``` { .py .copy }
from AppOpener import open
open("mklist")
#app_data.json file will be created in your working directory.
```

### 4. Give Appnames

Making use of `give_appnames` function to fetch appnames as dictionary, that can be used for several purpopses. (Ex. use it for autocomplete)

> Attribute

| Attribute      | Description                          |
| ----------- | ------------------------------------ |
| <upper>       | Dictionary should be uppercase               |

**a. General**

``` { .py .copy }
from AppOpener import give_appnames
apps = give_appnames()
print(apps) # Print appnames as (Dictionary)
```

**b. Using <upper> attribute**

``` { .py .copy }
from AppOpener import give_appnames
apps = give_appnames(upper=True)
print(apps) # Print appnames in uppercase as (Dictionary)
```
  
Supportive examples can be found [here](Applications.md).
