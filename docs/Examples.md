Here, we will explore the several Examples of using module for several purposes.

<font size=5>1. Basic 🧐</font>

### `Run application`

``` python
from AppOpener import run
run("telegram")
#This will open telegram if installed else pass it.
```

### `Run multiple applications`

``` python
from AppOpener import run
run("telegram, whatsapp")
#This will open telegram & whatsapp one-by-one if installed else pass the app which is not installed.
```

<br>

---

<font size=5>2. Features 🔥</font>

[//]: # (Using <u>SUB-COMMANDS</u> of `RUN` function.)


| Command      | Description                          |
| :---------- | :----------------------------------- |
| `LS`       | Print list of applications.  |
| `HELP`    | Print supported commands. |
| `FIND XYZ`       | Find application / applications. |
| `RENAME -M`    | Update petnames manually. |
| `OLDNAME > NEWNAME`    | Update petname via command line. |
| `UPDATE`    | Load new appnames and appids. |
| `DEFAULT`    |Restore sefault appnames. |
| `LOG`    | Print changes in petnames. |


&nbsp; 1. `LS - LISTING APPNAMES`

``` python
from AppOpener import run
run("ls")
#See list of appnames
```

&nbsp; 2. `HELP - QUICK COMMANDS`

``` python
from AppOpener import run
run("help")
#See supported commands
```

&nbsp; 3. `FIND XYZ - SEARCH APPLICATIONS`

Find applications present in data or not. If any mentioned application is not found in data, it will return nothing else it will return what founded.

``` python
from AppOpener import run
run("find whatsapp, telegram")
```

&nbsp; 4. `RENAME -M - RENAME APPNAMES MANUALLY.`

Change names of applications as per your choice. Your default code editor will be opened as soon as the command is entered. **Changes will be done after reloading of module**.

``` python
from AppOpener import run
run("rename -m")
```

&nbsp; 5. `OLDNAME > NEWNAME - RENAME APPLICATIONS VIA CLI`

Consider, updating petnames via command line. Name any application as per your choice.

``` python
from AppOpener import run
run("firefox > fire, brave > bravely")
# Here, firefox & brave will be named as fire & bravely respectively.
```

&nbsp; 6. `UPDATE - FETCH ALL NEW APPLICATIONS`

Assume, you installed some more <u>naughty</u> applications so now, how can you **fetch all new apps??** Simple by **UPDATE command**.

``` python
from AppOpener import run
run("update")
#Fetch all apps, if any.
```

&nbsp; 7. `DEFAULT - RESTORE DEFAULT APPNAMES`

Consider, you wanna make **all** your names changes go brhhhh. You can use **DEAFULT** command.

``` python
from AppOpener import run
run("default")
```

&nbsp; 8. `LOG - SEE PETNAMES`

One fine day you wanna see your renames appnames (PETNAMES). You can simply use **LOG** command, which will show you your current appname changes.

``` python
from AppOpener import run
run("log")
#See petnames
```

Also, to see **all** appnames changes.

``` python
from AppOpener import run
run("log -c")
#See complete petnames even if duplicate petnames are available.
```

<br>

---

<font size=5>3. Listing 📃</font>

<u>Makelist</u> of **APPNAMES** & **APPIDS**

Sometimes we need list of applications installed in our system. In curiosity if you want list of Appnames or AppIds 

You can make use of `MKLIST` function.

MKLIST function accepts 3 attributes.

| Attribute      | Description                          |
| ----------- | ------------------------------------ |
| `filename=`       | Filename of file to be created                      |
| `path=`       | Path of folder where file is to be created                     
| `specific=`    | File content (APPNAMES or APPIDS)                     |


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


!!! warning "warning"
	AppOpener only renders **JSON** & **TXT** files, any other file extension will not be accurately rendered.
	

&nbsp; 3. `PATH=`

Assume, you want list generated in other directory. You can simply use **PATH**.

``` python
from AppOpener import mklist
mklist(path=r"C:\Users\athar\Documents\projects\AppOpener")
#app_data.json file will be created in the provided directory.
```

&nbsp; 4. `SPECIFIC=`

Assume, you just want APPNAMES / APPIDS in the list to be generated. You can simply use **SPECIFIC**.

Following example is supportive for <u>Appnames</u>:

``` python
from AppOpener import mklist
mklist(specific="appnames")
#app_data.json file will be created, which will only contain APPNAMES.
```

Following example is supportive for <u>Appids</u>:

``` python
from AppOpener import mklist
mklist(specific="appids")
#app_data.json file will be created, which will only contain APPIDS.
```

!!! info "Info"
	As json does not support single keys, so AppOpener lists Appnames / Appids and gives each appname / appid null value.
	
&nbsp; 4. `INTEGRATING ATTRIBUTES`

Mixing attributes baby!!

Creating <u>JSON</u> format file.

``` python
from AppOpener import mklist
mklist(filename="data.json",specific="appnames",path=r"C:\Users\athar\Documents\projects\AppOpener")
#data.json file will be created in provided directory, which will only contain APPNAMES.
```

Creating <u>TXT</u> format file.

``` python
from AppOpener import mklist
mklist(filename="data.txt",specific="appids",path=r"C:\Users\athar\Documents\projects\AppOpener")	
#data.json file will be created in provided directory, which will only contain APPIDS.
```
&nbsp; 5. `INTEGRATING MKLIST with RUN function`

Mix baby!!

``` python
from AppOpener import run
run("mklist")
#app_data.json file will be created in your working directory, which will only contain Appnames & Appids.
```