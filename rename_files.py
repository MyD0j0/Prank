import os

def rename_files():
    #(1) get the list of file names we want to rename
    #file_list = os.listdir(r"/home/eric/Documents/Aptana Studio 3 Workspace/Prank/pics")
    #print(file_list)
    saved_path = os.getcwd()
    print(saved_path)
    os.chdir(r"/home/eric/Documents/Aptana Studio 3 Workspace/Prank/pics")
    #(2) for each file, rename the file
    for file_name in file_list:
        os.rename(file_name,  file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
        
rename_files()