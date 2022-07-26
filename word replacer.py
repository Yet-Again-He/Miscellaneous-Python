"""
This is an improved version of the file-walking attempts of the favicon and hyperlink fixer,
however, the scope of this file is limited to just replacing a certain word in certain, scattered entries.
"""

import os
import json
from tkinter.filedialog import askdirectory

directory = askdirectory()

total = 0
partial = 0
file_string = ""
org_word = "zapo"
org_word_2 = "zapotecs"
new_word = "gondor"
new_word_2 = "gondorians"

# Calculate total number of files
for root, dirs, files in os.walk(directory):
    for file in files:
        if file[-4:] == ".xml" or file[-4:] == ".json":
            total += 1

# Begin walking thorugh the chosen directory
try:
    for root, dirs, files in os.walk(directory):

        # This is for replacing the information INSIDE the files.
        for filename in files:

            root2 = root.replace("\\", "/")
            if filename[-4:] == ".xml":
                
                # Get information from file
                file = open(root2 + "/" + filename, "r", errors="ignore")
                file_string = file.read()
                file.close()

                # Replace information
                file_string = file_string.replace(org_word_2, new_word_2)
                file_string = file_string.replace(org_word, new_word)

                # Input edited information back into file
                file = open(root2 + "/" + filename, "w")
                file.write(file_string)
                file.close()
                # add to the number of files completed
                partial += 1
                print(str(partial) + "/" + str(total) + "completed!")
            else:
                next
            # elif filename[-4:] == ".json":
            #     # Unfortunately (or fortunately, depending on who's asking), you cannot modify json files like normal files, so here's its special code.
                
            #     # Get information from file
            #     file = open(root2 + "/" + filename, "r", errors="ignore")
            #     json_string = file.read()
            #     file.close()
            #     file_string = json.loads(json_string)

            #     # Replace information
            #     file_string = file_string.replace(org_word_2, new_word_2)
            #     file_string = file_string.replace(org_word, new_word)
                
            #     # Input edited information back into file
            #     json_string = json.dumps(file_string)

            #     # Input edited information back into file
            #     file = open(root2 + "/" + filename, "w")
            #     file.write(file_string)
            #     file.close()


    for root, dirs, files in os.walk(directory):

        # This is for modifying the file names.
        for filename in files:

            root2 = root.replace("\\", "/")

            if "zapo" in filename:
                filename_2 = filename.replace(org_word, new_word)
                os.rename(root2 + "/" + filename, root2 + "/" + filename_2)
            elif "zapotecs" in filename:
                filename_2 = filename.replace(org_word_2, new_word_2)
                os.rename(root2 + "/" + filename, root2 + "/" + filename_2)
            else:
                next

    
    for root, dirs, files in os.walk(directory):
    # This is for modifying the folder names.
        for dirname in dirs:

            root2 = root.replace("\\", "/")

            if dirname == "zapotecs":
                os.rename(root2 + "/" + dirname, root2 + "/" + new_word_2)
            elif dirname == "zapo":
                os.rename(root2 + "/" + dirname, root2 + "/" + new_word)
            else:
                next

except:
    print(root2 + "/" + filename)




# init_dr = "../Roots"


# def file_looper(directory):
#     """To detect a file which is giving an error"""

#     total = 0
#     partial = 0

#     for root, dirs, files in os.walk(init_dr):
#         for file in files:
#             total += 1

#     print("Total number of files: " + str(total))

#     for root, dirs, files in os.walk(directory):
#         if "Miscellaneous" in dirs:
#             dirs.remove("Miscellaneous")
#             print("removed!")

#         for file in files:
#             if ".lnk" in file or ".docx" in file:
#                 next
#             else:
#                 root2 = root.replace("\\", "/")
#                 # error_file = open(root2 + '/' + file, 'r', encoding='utf8')  # Can't use w+ (since it empties the file), but it won't accept r+
#                 # error_html = error_file.read()
#                 # error_file.close()
#                 with open(root2 + '/' + file, 'r') as error_file:
#                     error_html = error_file.read()

#                 fixed_html = error_html.replace("crijns", "crijns")

#                 fixed_file = open(root2 + "/" + file, "w+")
#                 fixed_file.write(fixed_html)
#                 fixed_file.close()
#                 partial += 1
#                 print(str(partial) + "/" + str(total) + "completed!")

# try:
#     file_looper(init_dr)
# except IOError:
#                 print(file)
#                 print(root)
#                 # pass  # IT STILL WON'T PASS!  WHY WON'T IT PASS!?
# finally:
#                 pass
