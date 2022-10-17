import os

cwd = os.getcwd()
print("CWD is :",cwd)

def current_path():
    print("--->", os.getcwd())

current_path()
os.chdir("../")
current_path()

# directory = "newfolder"
# parent_dir = "D:\Python"
# path = os.path.join(parent_dir,directory)
# os.mkdir(path)
# print("Directory '%s' created"  % directory)

# directory = "newfolder1"
# parent_dir = "D:\Python"
# mode = 0o666
# path = os.path.join(parent_dir,directory)
# os.mkdir(path,mode)
# print("Directory '%s' created"  % directory)

# directory = "newfolder2"
# parent_dir = "D:\Python"
# mode = 0o666
# path = os.path.join(parent_dir,directory)
# os.makedirs(path,mode)
# print("Directory '%s' created"  % directory)

path = "/"
dir_list = os.listdir(path)
print(f" --- files and directories in {path} --- ")
print(dir_list)

# file = "newfolder"
# parent_dir = "D:\Python"
# path = os.path.join(parent_dir,file)
# os.rmdir(path)

print(os.name)