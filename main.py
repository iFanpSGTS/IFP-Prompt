import dir, cmds
#IFP = iFanpS Prompt

################## Variable ################################
dirs = dir.dir()
CMDs = cmds.CMD()
SyntaxOrSymbol = "[IFP] <{0}> />"
############################################################
 
if CMDs.isAdmin():
    CMDs.Interface(True)
    while True:
        CMDs.change_title()
        cmd = input("\n"+SyntaxOrSymbol.format(dirs.curr_dir()))
        CMDs.check_available_cmd(cmd)
        if cmd.startswith("cd"):
            dirs.change_dir(cmd)
        if cmd.startswith("listdir"):
            dirs.listDir(dirs.curr_dir())
        if cmd.startswith("mkdir"):
            dirs.makeDir(cmd, dirs.curr_dir())
        if cmd.startswith("mkfile"):
            dirs.createFile(cmd, dirs.curr_dir())
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
        if cmd.startswith("start"):
            CMDs.start_program(cmd)
        if cmd.startswith("crp"):
            CMDs.platform("crp")
else:
    CMDs.Interface()
    while True:
        CMDs.change_title()
        cmd = input("\n"+SyntaxOrSymbol.format(dirs.curr_dir()))
        CMDs.check_available_cmd(cmd)
        if cmd.startswith("cd"):
            dirs.change_dir(cmd)
        if cmd.startswith("listdir"):
            dirs.listDir(dirs.curr_dir())
        if cmd.startswith("mkdir"):
            dirs.makeDir(cmd, dirs.curr_dir())
        if cmd.startswith("mkfile"):
            dirs.createFile(cmd, dirs.curr_dir())
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
        if cmd.startswith("start"):
            CMDs.start_program(cmd)
        if cmd.startswith("crp"):
            CMDs.platform("crp")
