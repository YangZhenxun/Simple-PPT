import sys
from cx_Freeze import setup, Executable

build_exe_options = {'packages': [], 'excludes': []}

setup(  name = 'make-PPT-b1.py',
        version = 'v0.0.1-b1',
        description = 'It can make a PPT for you',
        options = {'build_exe': build_exe_options},
        executables = [Executable('./b1.py')])
