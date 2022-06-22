import os
from tkinter.filedialog import askdirectory

directory = askdirectory()
#link_tag = '<link rel="shortcut icon" type="image/x-icon" href="Images/favicon.ico"</link>'

style_line = "</style>\n"

ind = 0
file_string = ""
try:
    for filename in os.listdir(directory):
        if filename[-4:] == ".htm":
            filename2 = filename[:-4]
            link_tag = f"<title>Neo-Adûnaic : {filename2}</title>"
            file = open(directory + "/" + filename, "r")
            file_lines = file.readlines()
            file.close()
            for line in file_lines:
                if line == style_line:
                    ind = file_lines.index(line)
                    file_lines.insert(ind + 1, link_tag)
                    continue
                else:
                    continue
            file = open(directory + "/" + filename, "w")
            file.write("\n".join(file_lines))
            file.close()
        else:
            next
except:
    pass

