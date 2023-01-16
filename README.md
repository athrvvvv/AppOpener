## AppOpener 🔓

AppOpener is the python library to **open/close** any application **without knowing it's absoulute path**. The library works by making use of App Name and App Id.

Library works on python version 3.5 or above python version 3.5+

[![PyPI Downloads](https://img.shields.io/pypi/dm/AppOpener)](https://pypi.org/project/AppOpener/) &nbsp; [![PyPI Downloads](https://img.shields.io/pypi/status/AppOpener)](https://pypi.org/project/AppOpener/) &nbsp; [![PyPI Downloads](https://img.shields.io/pypi/v/AppOpener?label=AppOpener)](https://pypi.org/project/AppOpener/) &nbsp; [![Windows Only](https://img.shields.io/badge/platform-windows-blue.svg)](https://shields.io/)

<!-- > **Note**
> AppOpener is only functional on windows. -->

Visit official documentation of AppOpener [here](https://AppOpener.readthedocs.io/en/latest/).

The latest development version is always available at the [Github](https://github.com/athrvvvv/AppOpener) repository.

---

> ### Features:

1. Open applications
2. Close applicatons
3. Create list of Apps & Ids

---

### Integrating AppOpener

![](docs/img/output.gif)

See [Examples](https://github.com/athrvvvv/AppOpener/tree/module/Examples) for more.
---

> ### Install Package 📦

```
pip install AppOpener
```

> ### Quick start ⚡

``` python
from AppOpener import open, close, mklist
open("telegram, whatsapp")
close("telgrm", match_closest=True) # Closes telegram as "telgrm" is closest to "telegram"
mklist(name="app_data.json")
```

---
> ### Building package 🔨

```
git clone https://github.com/athrvvvv/AppOpener.git
cd AppOpener
python setup.py sdist bdist_wheel
```
The latest release is always available at the Github [releases](https://github.com/athrvvvv/AppOpener/releases).

---
> ### Contributing 🤝

Contributions are welcomed. To know more visit [here](https://github.com/athrvvvv/AppOpener/blob/module/CONTRIBUTING.md).

---

### Links 🔗

- PYPI page - https://pypi.org/project/appopener/
- Official documentation - https://AppOpener.readthedocs.io/en/latest/
- Github releases - https://github.com/athrvvvv/AppOpener/releases/
- Project changelog - https://github.com/athrvvvv/AppOpener/blob/module/CHANGELOG.md/
- Issue tracker - https://github.com/athrvvvv/AppOpener/issues/

### Stay connected 🤗

- [Mail](mailto:athrvchaulkar@gmail.com)
- [Twitter](https://twitter.com/athrvvvvv)
- [YouTube](https://www.youtube.com/c/ACUNBOXING2017)
