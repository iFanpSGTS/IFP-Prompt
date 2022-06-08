from colorama import *; import dir, cmds; import random
#IFP = iFanpS Prompt

################## Variable ################################
init()
dirs = dir.dir()
CMDs = cmds.CMD()
rand_ver = random.randint(1000, 2000)
Information_ifNotRunAsAdmin = Fore.GREEN + """
IFP Windows (not run as admin) [11.0.{0}.{1}]
(c) IFP CMD by iFanpS
""".format(rand_ver, rand_ver).strip()
Information_ifRunasAdmin = Fore.LIGHTGREEN_EX + """
IFP Windows (run as admin) [11.0.{0}.{1}]
(c) IFP CMD by iFanpS
""".format(rand_ver, rand_ver).strip()
SyntaxOrSymbol = "[IFP] <{0}> />"
CMDs.change_title()
############################################################

if CMDs.isAdmin():
    print(Information_ifRunasAdmin)   
    while True:
        CMDs.change_title()
        cmd = input("\n"+SyntaxOrSymbol.format(dirs.curr_dir()))
        if cmd.startswith("cd"):
            dirs.change_dir(cmd)
        if cmd.startswith("listdir"):
            dirs.listDir(dirs.curr_dir())
        if cmd.startswith("mkdir"):
            dirs.makeDir(cmd.split()[1], dirs.curr_dir())
        if cmd.startswith("mkfile"):
            dirs.createFile(cmd.split()[1], dirs.curr_dir())
        if cmd.startswith("date"):
            CMDs.date()
        if cmd.startswith("clear"):
            CMDs.clear_prompt()
        if cmd.startswith("help"):
            CMDs.help_cmd()
        if cmd.startswith("echo"):
            CMDs.print_text(cmd.replace("echo", ""))
        if cmd.startswith("ver"):
            CMDs.platform("ver")
else:
    print(Information_ifNotRunAsAdmin)
    while True:
        CMDs.change_title()
        cmd = input("\n"+SyntaxOrSymbol.format(dirs.curr_dir()))
        if cmd.startswith("cd"):
            dirs.change_dir(cmd)
        if cmd.startswith("listdir"):
            CMDs.change_title("listdir")
            dirs.listDir(dirs.curr_dir())
        if cmd.startswith("mkdir"):
            dirs.makeDir(cmd.split()[1], dirs.curr_dir())
        if cmd.startswith("mkfile"):
            dirs.createFile(cmd.split()[1], dirs.curr_dir())
        if cmd.startswith("date"):
            CMDs.date()
        if cmd.startswith("clear"):
            CMDs.change_title("clear")
            CMDs.clear_prompt()
        if cmd.startswith("help"):
            CMDs.help_cmd()
        if cmd.startswith("echo"):
            CMDs.print_text(cmd.replace("echo", ""))
        if cmd.startswith("ver"):
            CMDs.platform("ver")
