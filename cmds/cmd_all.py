from datetime import date; import os, ctypes, platform,time

import psutil;from error import *;from art import *;from colorama import *

help_commds = ["mkdir", "listdir", "mkfile", "date", "clear", "echo", "ver (display windows version)", "cd", "start", "crp (check running program)"]
avai_commds = ["mkdir", "listdir", "mkfile", "date", "clear", "echo", "ver", "cd", "help", "start", "crp"]
init()

class CMD:
    def __init__(self):
        pass
    
    def check_available_cmd(self, cmd):
        try:
            if cmd.split()[0] not in avai_commds:
                defind_error("CommandNotFoundError")
            else:
                pass
        except:
            pass
    
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
        if arg == "ver":
            if osname == "nt":
                osname = "Windows"
                print(f"<{osname}> {platform.version()}")
            else:
                print(f"<{osname}> {platform.version()}")
        if arg == "crp":
            print(" \n [/] Checking all running program")
            for i in psutil.win_service_iter():
                crp_count_program += 1
                print(f"[> {i} </]")
                time.sleep(0.1)
            if crp_count_program >= 700:
                print(Fore.RED + f"[warning] {crp_count_program} program is running, its to high." + Fore.GREEN)
            else:
                print(f"[i] {crp_count_program} program is running.")
    
    def start_program(self, name_or_path):
        try:
            return os.startfile(f"{name_or_path.split()[1]}")
        except:
            print("[i] Cannot run the specified program.")
    
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
        print(f"[ECHO]{text}")
