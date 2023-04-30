# Welcome to AppOpener's Documentation

<html>
<a href="https://pypi.org/project/AppOpener" target="_blank">AppOpener</a>
</html>
is the python module which helps in opening any application without knowing it's absoulute path. The module works by making use of App name and App Id, we'll discuss this shorty.

[![PyPI Downloads](https://img.shields.io/pypi/dm/AppOpener)](https://pypi.org/project/AppOpener/) &nbsp; [![PyPI Downloads](https://img.shields.io/pypi/status/AppOpener)](https://pypi.org/project/AppOpener/) &nbsp; [![PyPI Downloads](https://img.shields.io/pypi/v/AppOpener?label=AppOpener)](https://pypi.org/project/AppOpener/) &nbsp; [![Windows Only](https://img.shields.io/badge/platform-windows-blue.svg)](https://shields.io/)

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

``` { .py .copy }
from AppOpener import open, close, mklist, give_appnames
open("telegram, whatsapp") # Opens telegram and whatsapp
open("APPNAME", throw_error=True) # Raises Exception if App is not found
close("telgrm", match_closest=True) # Closes telegram
mklist(name="app_data.json") # Generates an file having Appnames & AppIds
appnames = give_appnames() # Save appnames as dictionary
```

!!! note "Note"

    Running module **first time** may take time as module configures all required files.

### User documentation 📄

Learn installation & use of module [here](Overview.md).

### Devs documentation 💻

Learn how does module works. Learn the working of the module. Learn concept [here](Build.md).

### Examples 🤗

Set of examples covering all the features of AppOpener. You can see all the examples [here](Examples.md).