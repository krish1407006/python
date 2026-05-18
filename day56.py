# Shutil in python

import shutil

# The shutil module in Python provides a higher level interface for file operations.
#  It allows you to perform various file operations such as copying, moving, and deleting files and directories.\

shutil.copy("day56.py", "day57copy.py")  # copy a file


shutil.move("day57copy.py", "day57moved.py")  # move a file

shutil.rmtree("day57moved.py")  # delete a file

shutil.copytree("day56.py", "day57copydir")  # copy a directory



