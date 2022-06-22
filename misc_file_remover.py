
import os

directory = os.getcwd()

total = 0
# Calculate total number of files
for root, dirs, files in os.walk(directory):
    for file in files:
        total += 1

# Loop through all the files
for roots, dirs, files in os.walk(directory):

    for filename in files:
        if filename[-4:] != ".jpg":
            os.remove(filename)
        else:
            continue