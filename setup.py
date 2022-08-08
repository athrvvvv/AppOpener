from distutils.core import setup

exec(compile(open('release.py').read(), 'release.py', 'exec'))

try:
    from sphinx.setup_command import BuildDoc
    cmd_class ={'build_sphinx': BuildDoc}
except ImportError:
    cmd_class = {}

from release import *

packages = ['AppOpener']

a = open("README.md","r")
read = a.read()

setup(name=name,
      version          = version,
      description      = description,
      long_description_content_type="text/markdown",
      long_description = read,
      author           = authors["Athrv"][0],
      author_email     = authors["Athrv"][1],
      maintainer       = authors["athrvvvv"][0],
      maintainer_email = authors["athrvvvv"][1],
      license          = license,
      classifiers      = classifiers,
      url              = url,
      download_url     = download_url,
      platforms        = platforms,
      keywords         = keywords,
      py_modules       = ['AppOpener'],
      packages         = packages,
      include_package_data=True,
      install_requires=install_requires,
      dnata_files       = [],
      cmdclass = cmd_class
      )

