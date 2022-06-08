import os;from datetime import datetime

class dir:
    def __init__(self):
        pass
    
    def curr_dir(self):
        return os.getcwd()
    
    def change_dir(self, path):
        try:
            return os.chdir(path.split()[1])
        except IndexError:
            print("Path /> <" + os.getcwd() + ">")
        except:
            print("[i] System cannot find the specified path.")

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
        path = os.path.join(curr_path, name_folder)
        os.mkdir(path)
        print(f"\n<{name_folder} (folder)> is Created [date : {datetime.today()}]")
    
    def createFile(self, name_file, curr_path):
        path = os.path.join(curr_path, name_file)
        with open(path, "w") as f:
            f.write("")
            f.close()
        print(f"\n<{name_file} (file)> is Create [date : {datetime.today()}]")
