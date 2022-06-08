from datetime import date; import os, ctypes, platform

commds = ["mkdir", "listdir", "mkfile", "date", "clear", "echo", "ver (display windows version)"]

class CMD:
    def __init__(self):
        pass
    
    def platform(self, arg):
        if arg == "ver":
            print(f"[Windows] {platform.version()}")
        else:
            pass
    
    def date(self):
        print(f"\nDate : [ Make sure u happy today :D ] <{date.today()}>")
    
    def clear_prompt(self):
        os.system("cls" or "clear")
        
    def isAdmin(self):
        try:
            is_admin = (os.getuid() == 0)
        except AttributeError:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        return is_admin
    
    def change_title(self, cmd=None):
        if cmd == None:
            os.system("title IF Prompt")
        else:
            os.system("title IF Prompt - " + cmd)
        
    def help_cmd(self, comms=None):
        if comms != None:
            pass 
        else:
            print(" CMD Available:\n")
            for i in commds:
                print("[<>] " + i)
                
    def print_text(self, text):
        print(f"[ECHO]{text}")
