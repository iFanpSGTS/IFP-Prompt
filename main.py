from colorama import Fore; import dir, cmds; import random;
#IFP = iFanpS Prompt

################## Variable ################################
dirs = dir.dir()
CMDs = cmds.CMD()
rand_ver = random.randint(1000, 2000)
Information_ifNotRunAsAdmin = Fore.GREEN + """
IFP Windows (not run as admin) [11.0.{0}.{1}]
(c) IFP CMD by iFanpS
""".format(rand_ver, rand_ver).strip()
SyntaxOrSymbol = "[IFP] <{0}> />"
############################################################

def Selection_Cmd():
    print(Information_ifNotRunAsAdmin)
    while True:
        cmd = input("\n"+SyntaxOrSymbol.format(dirs.curr_dir()))
        if cmd.startswith("cd"):
            dirs.change_dir(cmd.split()[1])
        if cmd.startswith("listdir"):
            dirs.listDir(dirs.curr_dir())
        if cmd.startswith("mkdir"):
            dirs.makeDir(cmd.split()[1], dirs.curr_dir())
        if cmd.startswith("mkfile"):
            dirs.createFile(cmd.split()[1], dirs.curr_dir())
        if cmd.startswith("date"):
            CMDs.date()
        
Selection_Cmd()