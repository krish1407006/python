# clear the clutter in the folder by creating a new folder and moving all the files in that folder

import os
path=input("os module")
path=path.replace('\\','/')
print(path)
print(os.listdir(path))
def rename():
    i=1
    for filename in os.listdir(path):
        new_name=path+"ghj"+str(i)
        old_name=path+filename
        os.rename(old_name,new_name)
        i = i+1
rename()



