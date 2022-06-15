from datetime import date; import os, ctypes, platform,time
import dir
import psutil;from error import *;from art import *;from colorama import *

dirs = dir.dir()
help_commds = ["mkdir", "listdir", "mkfile", "date", "clear", "echo", "ver (display windows version)", "cd", "start", "crp (check running program)",
              "crs (check running service)"]
avai_commds = ["mkdir", "listdir", "mkfile", "date", "clear", "echo", "ver", "cd", "start", "crp", "crs"]
init()

class CMD:
    def __init__(self):
        pass
    
    def cmd_handler(self, cmd):
        def cmd_handler(self, cmd):
        match cmd.split()[0]:
            case "help":
                for i in help_commds:
                    print(" CMD available:\n========================")
                    print(f"{i}\n=========================")
            case "mkdir":
                dirs.makeDir(cmd, dirs.curr_dir())
            case "cd":
                dirs.change_dir(cmd)
            case "listdir":
                dirs.listDir(dirs.curr_dir())
            case "mkfile":
                dirs.createFile(cmd, dirs.curr_dir())
            case "date":
                self.date()
            case "clear":
                self.clear_prompt()
            case "echo":
                self.print_text(cmd)
            case "ver":
                self.platform("ver")
            case "crp":
                self.platform("crp")
            case "crs":
                self.platform("crs")
            case "start":
                self.start_program(cmd)
            case i if i not in avai_commds:
                defind_error("CommandNotFoundError")
            
    def Interface(self, isAdmin=False):
        if isAdmin == False:
            print(f"""{Fore.CYAN + text2art("IF Prompt")}
    {Fore.GREEN}
    \tIFP Windows (not run as admin) [{platform.version()}]
    \t(c) IFP CMD by iFanpS <2022>          
    """)
        else:
            print(f"""{Fore.CYAN + text2art("IF Prompt")}
    \tIFP Windows (run as admin) [{platform.version()}]
    \t(c) IFP CMD by iFanpS <2022>          
    """)
    
    def platform(self, arg):
        osname = os.name
        crp_count_program = 0
        crs_count_service = 0
        if arg == "ver":
            if osname == "nt":
                osname = "Windows"
                print(f"<{osname}> {platform.version()}")
            else:
                print(f"<{osname}> {platform.version()}")
        if arg == "crp":
            print(" \n [/] Checking all running program")
            try:
                for i in psutil.process_iter():
                    crp_count_program += 1
                    print(f"[> Name : {i.name()} | PID : {i.pid} </]")
                    time.sleep(0.1)
                if crp_count_program >= 300:
                    print(Fore.RED + f"[warning] {crp_count_program} program is running, its to high." + Fore.GREEN)
                else:
                    print(f"[i] {crp_count_program} program is running.")
            except:
                defind_error("KeyboardInterrupt")
        if arg == "crs":
            print(" \n [/] Checking all running services")
            try:
                for i in psutil.win_service_iter():
                    crs_count_service += 1
                    print(f"Service : {i.name()} | Name : {i.display_name()}")
                    time.sleep(0.1)
                print(f"{crs_count_service} services is running.")
            except:
                defind_error("KeyboardInterrupt")
    
    def start_program(self, name_or_path):
        try:
            return os.startfile(f"{name_or_path.split()[1]}")
        except:
            defind_error("SyntaxError")
    
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
            for i in help_commds: 
                print("[<>] " + i)
                
    def print_text(self, text):
        rmw = text.replace("echo", "")
        text = re.sub("^\s+|\s+$", "", rmw, flags=re.UNICODE)
        print(f"[ECHO] - {text}")
