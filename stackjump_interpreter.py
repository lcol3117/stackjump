#stackjump interpreter
import re, os, sys

print("Welcome to STACKJUMP")
cfname = input("Enter filename: ")
if ".sjm" in cfname:
    pass
else:
    cfname=cfname+".sjm"

cf = open(cfname,'r')

stack=[None]
rtns={}

done=False
fline=0
fnloc=-1
while not done:
    cl=cf.readline()
    #print("Current line: "+cl)
    #print("Stack is: "+str(stack))
    #print("Funcs are: "+str(rtns))
    #print("Funcloc is: "+str(fnloc))
    fline+=1
    if fnloc==-2:
        if cl.startswith(":"+fname):
            fnloc=-1
        continue
    if cl.startswith("."):
        data=cl[1:]
        if (data == "\\"):
            stack.append(None)
            continue
        try:
            data=int(data)
        except:
            pass
        stack.append(data)
        continue
    elif cl.startswith("~"):
        del stack[len(stack)-1]
        continue
    elif cl.startswith("@"):
        print(stack[len(stack)-1])
        continue
    elif cl.startswith("_"):
        totop=stack[len(stack)-2]
        tosec=stack[len(stack)-1]
        stack[len(stack)-1]=totop
        stack[len(stack)-2]=tosec
        continue
    elif cl.startswith("+"):
        numa=stack[len(stack)-1]
        numb=stack[len(stack)-2]
        del stack[len(stack)-1]
        del stack[len(stack)-1]
        stack.append(numa+numb)
    elif cl.startswith("-"):
        numa=stack[len(stack)-1]
        numb=stack[len(stack)-2]
        del stack[len(stack)-1]
        del stack[len(stack)-1]
        stack.append(numa-numb)
    elif cl.startswith("*"):
        numa=stack[len(stack)-1]
        numb=stack[len(stack)-2]
        del stack[len(stack)-1]
        del stack[len(stack)-1]
        stack.append(numa*numb)
    elif cl.startswith("/"):
        numa=stack[len(stack)-1]
        numb=stack[len(stack)-2]
        del stack[len(stack)-1]
        del stack[len(stack)-1]
        stack.append(numa/numb)
    elif cl.startswith("%"):
        numa=stack[len(stack)-1]
        numb=stack[len(stack)-2]
        del stack[len(stack)-1]
        del stack[len(stack)-1]
        stack.append(numa%numb)
    elif cl.startswith("$"):
        fname=cl[1:].strip()
        rtns[fname]=fline
        fnloc=-2
    elif cl.startswith(";"):
        fname=cl[1:].strip()
        fnloc=rtns[fname]
        cf.seek(rtns[fname])
        fline=rtns[fname]
        #print("Running: "+str(fname)+" at "+str(rtns[fname]))
    else:
        if cl.startswith(":"):
                continue
        done=True
cf.close()
