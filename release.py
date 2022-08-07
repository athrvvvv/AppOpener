from __future__ import print_function, unicode_literals, absolute_import

name = 'AppOpener'

branch = ''
version = '1.0'
description = "Open any application by it's name."
a = open("README.md","r")
read = a.read()
long_description = read

license = 'MIT'

authors = {'Athrv' : ('Athrv Chaulkar','athrvchaulkar@gmail.com'),
            'athrvvvv' : ('athrvvvv', 'athrvchaulkar@gmail.com')}

url = 'https://github.com/athrvvvv/AppOpener/tree/module'
download_url = 'https://pypi.python.org/pypi/AppOpner'
platforms = ['Windows 7',
             'Windows 10']

keywords = ['appopener',
            'open apps', 
            'App Ids', 
            'automation']

classifiers = ['Development Status :: 5 - Production/Stable',
               'Environment :: Console',
               'Operating System :: Microsoft :: Windows',
               'License :: OSI Approved :: MIT License',
               'Programming Language :: Python :: 3.5',
               'Programming Language :: Python :: 3.6',
               'Programming Language :: Python :: 3.7',
               'Programming Language :: Python :: 3.8',
               'Programming Language :: Python :: 3.9',
               'Programming Language :: Python :: 3.10'
               ]

install_requires=[
                "setuptools>=61.0.0",
                "wheel",
                "json", 
                "win32gui"
    ]
