print("""this little program is designed to move all files of a certain type to a designated location
a tree depth can also be specified, though it defaults to 10
all files of the type specified will be moved to a lcoation which can also be specfied""")

import subprocess
import os

MAXDEPTH = 10

maxdepth = MAXDEPTH

print("Enter a relative path:")
path = input()
if path[-1] != "\\":
    path += "/"

path = path.replace("/", "\\")
print("Enter a target directory:")
target = input()
print("Enter a file suffix: (.txt, .html, .tex, .pdf, .jpg, .py  ... Don't worry, this is not case sensitive)")
filetype = input()

if input("Would you like to specify a recursion depth? Type y if yes").upper() == "Y":
    maxdepth = int(input("Depth: "))
else:
    maxdepth = MAXDEPTH

dirs = os.listdir(path)

moved = 0

def movestuff(string):
    
    subprocess.run(string, shell = True)
    global moved
    moved += 1


def search(dirs, depth, dir):

    for d in dirs:
        folder = os.path.isdir(dir+d)
        
        file = os.path.isfile(dir + d)
        if folder:
            print("   "*depth + "folder: ", d)
            if depth <= maxdepth:
                search(os.listdir(dir + d + "/"), depth + 1, dir +  d + "/")
            else:
                print("Recursion depth exceeded")
        if file:
            
            
            name,suffix = os.path.splitext(path + dir + d)
            if suffix.upper() == filetype.upper():
                string = "copy " + dir + d + " " + target
                string = string.replace('/','\\')
                movestuff(string)
                
                

search(dirs, moved, path)
print("moved",moved,"files")