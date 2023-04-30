# Changelog

All notable changes to this project will be documented in this file.
This changelog is addressed to PyPi module [AppOpener].

---

## [1.7] - 2023-04-30

### Added
- Ability to throw errors when an App is not found
- Made an "old_style.py" where files are created using old method if issues like [#9](https://github.com/athrvvvv/AppOpener/issues/9) and [#10](https://github.com/athrvvvv/AppOpener/issues/10) occur.

### Changed
- Method for finding apps in the `find ` attribute in `open` function
- Fixed `mklist` function Bug for creating file, where user has imported module

### Removed
- `['(CLS)','CLEARS SCREEN']` from `help commands`


---

## [1.6] - 2023-01-16

### Added 
- `UTF-8 ENCODING` while creating the `data.json` file ,
- Better comments for user in vs code (i.e Ex. open("whatsapp")
- Condition for platform checking (If not windows exit)
- More accurate matching for `open` and `close` functions
- Beautiful code highlighting (docs)

### Changed 
- `open_closest` and `close_closest` are now `match_closest` in `open` and `close` functions respectively.
- `git-StartApps` is now  `Get-StartApps` (So no need to maximize window to get complete Appid).
- Fix broken link to the github account (Docs).
- Fix known issue for `MKLIST` function. 
- Fix issue [#5](https://github.com/athrvvvv/AppOpener/issues/5)
- Migrated from `readthedocs` theme to sexy `material` theme.

### Removed
- Minimise the decoration made to README.md
- `pywin32` in dependencies because no need to maximize window to get complete Appids.

---

## [1.5] - 2023-01-03

### Added
- `CLOSE` function to close any application by its name.
- `open_closest=` & `close_closest=` in `OPEN` & `CLOSE` function respectively, to open/close applications which matches closest.
- See `VERSION` through `OPEN` function.
- Attribute `output=` to print context or not to print in all functions.
- `PSUTIL` dependency in `release.py`.

### Changed
- `RUN` function is been replaced by `OPEN` function.

### Removed
- Attributes of `MKLIST` function.
- Install AppOpener via github section in docs.

---

## [1.4] - 2022-12-17

### Added
- Added pywin32 in the build spec as mentioned in [issue](https://github.com/athrvvvv/AppOpener/issues/7)

### Changed
- Fixed [issue](https://github.com/athrvvvv/AppOpener/issues/6) (Now you can use AppOpener in standalone files too)

### Removed
- Install AppOpener via github section in docs

---

## [1.3] - 2022-09-04

### Added
- Added ASCII encoding to powershell command in check.py

### Changed
- space

### Removed
- "refer.txt" step (no more need to fix the encoding problems) in check.py.

---

## [1.2] - 2022-09-03

### Added
- Adding "-encoding ASCII" to the powershell command that extracts to "reference.txt" the app list

### Changed
- space

### Removed
- "refer.txt" step (no more need to fix the encoding problems).

---

## [1.1] - 2022-08-29

### Added
- Added method to fetch AppNames as keys.
- Added documentation & source links in PYPI page.

### Changed
- Fix crash while using a (.bat) files.

### Removed
- Unwanted conditions & functions.

---

## [1.0] - 2022-08-27

### Added
- Features

### Changed
- Fix many many things.

### Removed
- Unwanted conditions & functions.

[1.7]: https://pypi.org/project/AppOpener/1.7/
[1.6]: https://pypi.org/project/AppOpener/1.6/
[1.5]: https://pypi.org/project/AppOpener/1.5/
[1.4]: https://pypi.org/project/AppOpener/1.4/
[1.3]: https://pypi.org/project/AppOpener/1.3/
[1.2]: https://pypi.org/project/AppOpener/1.2/
[1.1]: https://pypi.org/project/AppOpener/1.1/
[1.0]: https://pypi.org/project/AppOpener/1.0/
[AppOpener]: https://pypi.org/project/AppOpener
