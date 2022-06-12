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
        CMDs.cmd_handler(cmd)
else:
    CMDs.Interface()
    while True:
        CMDs.change_title()
        cmd = input("\n"+SyntaxOrSymbol.format(dirs.curr_dir()))
        CMDs.cmd_handler(cmd)
