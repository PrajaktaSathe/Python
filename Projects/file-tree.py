import os
cwd=os.getcwd()
glodir,spaces=cwd,""
def pr(glodir,spaces):
    for x in os.listdir(glodir):
        if glodir.replace(cwd,"").count("/")==0:
            print(" ",x)
        else:
            print(spaces+"--"+x)
        if os.path.isdir(glodir+"/"+x)==True:
            pr(glodir+"/"+x,spaces+"  |")
pr(glodir,spaces)