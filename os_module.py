import os

# get current working directory 
# getcwd()

def current_working_directory():
    c = os.getcwd()
    print("Current working directory is: ",c)

current_working_directory()

# change directory
# chdir("directory_path")

def change_wd():
    ch = os.chdir('C:\\Users\\Omkar\\Desktop\\Python_Programs\\Python')
    print("Successfully change directory")

change_wd()
current_working_directory()

# creating directory
# make directory
# mkdir()  -- use to create new directory
# path specify
# mkdir(path)

# os.mkdir("C:\\Users\\Omkar\\Desktop\\Python_Programs\\Python\\new_mkdir")
print(os.getcwd())
# os.mkdir("without_path")

current_working_directory()

# mkdir return an error for below path
# os.mkdir("C:\\Users\\Omkar\\Desktop\\Python_Programs\\Python\\new\\my_mkdir")

# makedirs() is used in such cases to create multiple directories
# os.makedirs("C:\\Users\\Omkar\\Desktop\\Python_Programs\\Python\\new\\my_mkdir")

# removing directory
# rmdir()
# rmdir(path)

# os.rmdir('C:\\Users\\Omkar\\Desktop\\Python_Programs\\Python\\new\\my_mkdir')

def remove_directory(path):
    os.rmdir(path)
    print("Directory removed successfully")

# remove_directo'C:\\Users\\Omkar\\Desktop\\Python_Programs\\Python\\new\\my_mkdir'ry('C:\\Users\\Omkar\\Desktop\\Python_Programs\\Python\\new')
# remove_directory('C:\\Users\\Omkar\\Desktop\\Python_Programs\\Python\\new_mkdir')
# thorws an error if current directory is not empty
# if you are in current working directory

# removing a file
# remove(path_with_file_name)

# os.remove('C:\\Users\\Omkar\\Desktop\\Python_Programs\\Python\\abc.py')
# FileNotFoundError (file not exist)
# IsADirectoryError (dont mention the file name)

#listdir()
#listdir(given_directory_path)
# returns the list of all the files and directories in the given directory
# if not specify path return list from cwd

x = os.listdir('C:\\Users\\Omkar\\Desktop\\Python_Programs\\Python')
print(x)


# renaming a file
# rename("old_name","new_name")
# old_file, new_file
# path should be in current working directory

# os.rename("rename.py","new_rename.py")


