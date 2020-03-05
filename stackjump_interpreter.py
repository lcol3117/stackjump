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
retloc=-1

cfd=cf.readlines()
cfd.append(" ")

while not done:
    cl=cfd[fline]
    fline+=1
    #print("Current line: "+cl)
    #print("Stack is: "+str(stack))
    #print("Funcs are: "+str(rtns))
    #print("Funcloc is: "+str(fnloc))
    if fnloc==-2:
        if cl.startswith(":"+fname):
            fnloc=-1
        continue
    if cl.startswith("."):
        data=cl[1:].strip()
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
    elif cl.startswith("["):
        totop=stack[0]
        del stack[0]
        stack.append(totop)
    elif cl.startswith("]"):
        stack.append(len(stack))
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
    elif cl.startswith("="):
        numa=stack[len(stack)-1]
        numb=stack[len(stack)-2]
        del stack[len(stack)-1]
        del stack[len(stack)-1]
        stack.append((0,1)[numa==numb])
    elif cl.startswith(">"):
        numa=stack[len(stack)-1]
        numb=stack[len(stack)-2]
        del stack[len(stack)-1]
        del stack[len(stack)-1]
        stack.append((0,1)[numa==numb])
    elif cl.startswith("<"):
        numa=stack[len(stack)-1]
        numb=stack[len(stack)-2]
        del stack[len(stack)-1]
        del stack[len(stack)-1]
        stack.append((0,1)[numa==numb])
    elif cl.startswith("&"):
        numa=stack[len(stack)-1]
        numb=stack[len(stack)-2]
        del stack[len(stack)-1]
        del stack[len(stack)-1]
        stack.append((0,1)[(numa==1) and (numb==1)])
    elif cl.startswith("|"):
        numa=stack[len(stack)-1]
        numb=stack[len(stack)-2]
        del stack[len(stack)-1]
        del stack[len(stack)-1]
        stack.append((0,1)[(numa==1) or (numb==1)])
    elif cl.startswith("!"):
        numa=stack[len(stack)-1]
        del stack[len(stack)-1]
        stack.append((1,0)[numa==1])
    elif cl.startswith("^"):
        numa=stack[len(stack)-1]
        if numa==1:
            retloc=fline
            fname=cl[1:].strip()
            fnloc=rtns[fname]
            fline=rtns[fname]
            #print("Running: "+str(fname)+" at "+str(rtns[fname]))
    elif cl.startswith("$"):
        fname=cl[1:].strip()
        rtns[fname]=fline
        fnloc=-2
    elif cl.startswith(";"):
        retloc=fline
        fname=cl[1:].strip()
        fnloc=rtns[fname]
        fline=rtns[fname]
        #print("Running: "+str(fname)+" at "+str(rtns[fname]))
    elif cl.startswith(":"):
        fnloc=-1
        fline=retloc
        continue
    else:
        if cl.startswith(":"):
                continue
        done=True
cf.close()
