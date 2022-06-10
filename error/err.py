import os
errs = {
    "FileNotFoundError":"[i] Cannot find the specified path/file or folder.",
    "FileExistsError":"[i] File/Folder already exist.",
    "AttributeError":"[x] Attribute error.",
    "IndexError":"[i] Cannot process syntax from input.",
    "KeyError":"[x] Key Error.",
    "ModuleNotFoundError":"[i] Module is not available on internal or external.",
    "SyntaxError":"[x] Syntax error.",
    "BaseException":"[x] BaseException error.",
    "AdminError":"[i] Please run as admin.",
    "CDError":"[dir] <{0}>".format(os.getcwd()),
    "CommandNotFoundError":"[x] CMD is not available.",
    "OSError":"[dir] <{0}>".format(os.getcwd())
}
def defind_error(error):
    if error in errs.keys():
        print(errs.get(error))
    else:
        print("[x] Cant proceed the error, from custom errorHandler.")
