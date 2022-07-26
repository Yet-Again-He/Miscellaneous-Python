"""
This is a tester for methods and functions within the actual word replacer script.
"""

import json
import os
from tkinter.filedialog import askdirectory

directory = askdirectory()

total = 0
partial = 0
file_string = ""
org_word = "zapo"
org_word_2 = "zapotecs"
new_word = "gondor"
new_word_2 = "gondorians"

for root, dirs, files in os.walk(directory):

    # This is for replacing the information INSIDE the files.
    for filename in files:

        root2 = root.replace("\\", "/")
        if filename.endswith(".json"):  # THIS WON'T FIND ANY JSON FILES FOR SOME REASON!??!

            print("Found one!")
            
            # Get information from file
            # with open(root2 + "/" + filename, "r", errors="ignore") as file:
            #     json_string = json.load(file)
            # print(json_string)

            file = open(root2 + "/" + filename, "r", errors="ignore")
            json_string = json.load(file)
            file.close
            json_string = dict(json_string)
            print(json_string)

            # Replace information
            # for ele in json_string:
            #     if ele == "zapo":
            #         json_string.update("zapo", "gondor")

            for key, value in json_string.items():
                if value == "zapo":
                    json_string.update("zapo", "gondor")

            # file_string = file_string.replace(org_word_2, new_word_2)
            # file_string = file_string.replace(org_word, new_word)
            
            # Input edited information back into file
            file_string = json.dumps(json_string, indent=4)
            print(file_string)

            # Input edited information back into file
            file = open(root2 + "/" + filename, "w")
            file.write(file_string)
            file.close()
        else:
            next


# for root, dirs, files in os.walk(directory):
# # This is for modifying the file names themselves.
#     for dirname in dirs:

#         root2 = root.replace("\\", "/")

#         if dirname == "zapotecs":
#             os.rename(root2 + "/" + dirname, root2 + "/" + new_word_2)
#         elif dirname == "zapo":
#             os.rename(root2 + "/" + dirname, root2 + "/" + new_word)
#         else:
#             next

# for root, dirs, files in os.walk(directory):

#     # This is for modifying the file names themselves.
#     for filename in files:

#         root2 = root.replace("\\", "/")

#         if "zapo" in filename:
#             filename_2 = filename.replace(org_word, new_word)
#             os.rename(root2 + "/" + filename, root2 + "/" + filename_2)
#         elif "zapotecs" in filename:
#             filename_2 = filename.replace(org_word_2, new_word_2)
#             os.rename(root2 + "/" + filename, root2 + "/" + filename_2)
#         else:
#             next