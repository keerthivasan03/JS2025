filepath="C:\\Users\\keerthivasan.a\\practise 19.py"
filepathz="C:\\Users\\keerthivasan.a\\python 20.py"
file=open(filepath,"r")
print(file.read())
file.close()
with open(filepathz,"r") as files:
    print(files.read())

filepaths="C:\\Users\\keerthivasan.a\\practse 19.py"
try:
    with open(filepaths,"r") as fille:
        print(fille.read())
except FileNotFoundError:
    print("File not found")

#iterate lines in file
filepath_i="C:\\Users\\keerthivasan.a\\open file.txt"
with open(filepath_i,"r") as file_iterate:
    for line_iterate in file_iterate:
        print(line_iterate.strip().upper())

filepath_s="C:\\Users\\keerthivasan.a\\open file.txt"
with open(filepath_s,"r") as file_ss:
    lines=file_ss.readlines()
    lines.sort() 
    print(lines)

filepath_w="C:\\Users\\keerthivasan.a\\open file.txt"
with open(filepath_w, "w") as file_w:
    file_w.write("Is a good bug")
filepath_o="C:\\Users\\keerthivasan.a\\iteate.txt"
with open(filepath_o,"a") as file_o:
    file_o.write("Newly added")

import os
os.remove("iteate.txt")
os.rename("csv.py","csv_check.py")
os.path.exists("open file.txt")
k="C:\\Users\\keerthivasan.a\\practise 18.py"
print(os.path.getsize("practise 18.py"))
print(os.path.getatime("practise 18.py"))
print(os.path.getctime("practise 18.py"))
print(os.path.getmtime("practise 18.py"))
print(os.getcwd())#path
#os.mkdir("Keethis")#create path
#print(os.chdir("Keethis"))#change dir
#os.rmdir("keerthis")#remove dir
#create_path=os.path.join(os.getcwd,"practise 99")
"""dir = "website"
for name in os.listdir(dir):
     fullname = os.path.join(dir, name)
     if os.path.isdir(fullname):
          print("{} is a directory".format(fullname))
     else:
          print("{} is a file".format(fullname))
"""
print(os.listdir(path=""))
