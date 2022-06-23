
import os
import tkinter as tk
from tkinter.filedialog import askdirectory
directory = askdirectory()


total = 0
# Calculate total number of files
for root, dirs, files in os.walk(directory):
    for file in files:
        total += 1

# Loop through all the files
for roots, dirs, files in os.walk(directory):

    for filename in files:
        if filename.endswith("jpg"):
            continue
        elif filename[-4:] != "jpg" and os.path.exists(filename) and not os.path.isdir(filename):
                os.remove(filename)
        else:
            continue