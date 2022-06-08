import os, re;from datetime import datetime

class dir:
    def __init__(self):
        pass
    
    def curr_dir(self):
        return os.getcwd()
    
    def change_dir(self, path):
        try:
            rmw = path.replace("cd", "")
            paths = re.sub("^\s+|\s+$", "", rmw, flags=re.UNICODE)
            return os.chdir(paths)
        except FileNotFoundError:
            print("[i] System cannot find the specified path.")
        except:
            print("Path /> <" + os.getcwd() + ">")

    def listDir(self, curr_path):
        print(f"\n Listing Directories {curr_path}")
        for i in os.listdir(curr_path):
            dirs = os.path.join(curr_path, i)
            if os.path.isdir(dirs):
                isdir = "(dir) " + i
            else:
                isdir = i
            print(f"[Find] > {isdir}")
            
    def makeDir(self, name_folder, curr_path):
        try:
            path = os.path.join(curr_path, name_folder.split()[1])
            os.mkdir(path)
            print(f"\n<{name_folder} (folder)> is Created [date : {datetime.today()}]")
        except IndexError:
            print("[x] Syntax is incorrect!")
    
    def createFile(self, name_file, curr_path):
        try:
            path = os.path.join(curr_path, name_file.split()[1])
            with open(path, "w") as f:
                f.write("")
                f.close()
            print(f"\n<{name_file} (file)> is Create [date : {datetime.today()}]")
        except IndexError:
            print("[x] Syntax is incorrect!")
