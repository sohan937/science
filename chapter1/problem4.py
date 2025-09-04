# write a python program to print the contents of a directory using the os module search online for the function which does that.

import os
path="./chapter1"
entries=os.listdir(path)
print(f"content of the directories: `{path}`")
for entry in entries:
    print(entry)