# Welcome to AppOpener's Documentation

<html>
<a href="https://pypi.org/project/AppOpener" target="_blank">AppOpener</a>
</html>
is the python module which helps in opening any application without knowing it's absoulute path. The module works by making use of App name and App Id, we'll discuss this shorty.

**<font size="4">Simplicity ✅</font>**
<br> <br>
AppOpener is simple to use. It is been written in modern python 3.10. Just couple of lines opens any application mentioned.

**<font size="4">Features 🤗</font>**
<br> <br>
AppOpener has plenty of **useful** features. These features make the module more efficient more productive.

**<font size="4">Open Source 😍</font>**
<br> <br>
AppOpener is entirely open source project. The latest development version is always available at the Github <a href="https://github.com/athrvvvv/AppOpener" target="_blank">repositoy</a>.

---

### Quick start ⚡

``` python
from AppOpener import open, close, mklist, give_appnames
open("telegram, whatsapp") # Opens telegram & whatsapp
close("chrome, telegram") # Closes chrome & telegram
mklist(name="app_data.json") # Create list of Apps & Ids
appnames = give_appnames() # Save appnames as dictionary
```

!!! note "Note"

    Running module **first time** may take time as module configures all required files.

### User documentation 📄

Learn installation & use of module [here](Overview.md).

### Devs documentation 💻

Learn how does module works. Learn the working of the module. Learn concept [here](Mechanism.md).

### Examples 🤗

Set of examples covering all the features of AppOpener. You can see all the examples [here](Examples.md).