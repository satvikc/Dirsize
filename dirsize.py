import os,sys,pdb
from os.path import join, getsize
def walks(x):
    s=0
    f=0
    for root, dirs, files in os.walk(x):
        try:
            try:
                p=sum([getsize(join(root, name)) for name in files])
                s+=p
                f+=len(files)
            except:
                pass
        except:
            print ("\nSome error. I am alo confused. Check user permission or try something else")
            exit(-1)
    return [s,f]
def dirsize(x):
    total_size=0
    direct=['/'.join([os.path.normpath(x),y]) for y in os.listdir(x)]
    root_direct=[d for d in filter(os.path.isdir,direct)]
    files=[f for f in direct if f not in root_direct]
    s=[walks(y) for y in root_direct]
    s=[u+[v] for u,v in zip(s,root_direct)]
    s.extend([[getsize(f)]+[-1,f] for f in files])
    try:
        s.sort(reverse=True)
    except:
        pdb.set_trace()
        pass
    for y in s:
        if y[1]!=-1:
            print("D " ,sizes(y[0])," (%d"%y[1],"files) " ,os.path.basename(y[2]))
        else:
            print("F ",sizes(y[0])," ", os.path.basename(y[2]))

        total_size+=y[0]
    return total_size
def sizes(s):                 # Takes size in Bytes and returns suitable size
    ext="Bytes"
    if s/1024 >=1:
        s=s/1024
        ext= "KB"
    if s/1024 >=1:
        s=s/1024
        ext= "MB"
    if s/1024 >=1:
        s=s/1024
        ext= "GB"
    if s/1024>=1:
        s=s/1024
        ext = "TB"
    return str(round(s,2))+" "+ext
if __name__=="__main__":
    if len(sys.argv)==2:
        size=dirsize(os.path.expanduser(sys.argv[1]))
        print("Total: ", sizes(size))
