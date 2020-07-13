"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
print('Command line arguments:')
for arg in sys.argv:
	print(arg + '\n')

# Print out the OS platform you're using:
print(f'Platform:\n{sys.platform}\n')


# Print out the version of Python you're using:
py_ver = sys.version_info

print(f'Python version:\n{py_ver[0]}.{py_ver[1]}.{py_ver[2]}\n')

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print(f'Current proccess ID:\n{os.getpid()}\n')

# Print the current working directory (cwd):
print(f'Current working dir:\n{os.getcwd()}\n')

# Print out your machine's login name
print(f'Current login:\n{os.getlogin()}\n')
