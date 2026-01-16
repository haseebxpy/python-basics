def analysing(inputfile,outputfile):
    count=0
    user=[]
    system=[]
    error=[]
    warning=[]
    with open(inputfile,"r") as file:
        for line in file:
            if line.strip()!="":
                count+=1
                if "user" in line.lower():
                    user.append(line.strip())
                if "system" in line.lower():
                    system.append(line.strip())
                if "error" in line.lower():
                    error.append(line.strip())
                if "warning" in line.lower():
                    warning.append(line.strip())
    with open(outputfile,"w") as file:
        file.write(f"Log Summary\n-----------\nTotal entries:{count}\nUser logs:{len(user)}\nSYSTEM Logs:{len(system)}\nERROR Logs:{len(error)}\nWARNING Logs:{len(warning)}\nERROR Details:\n")
        for index,data in enumerate(error,start=1):
            file.write(f"{index}. {data}\n")
try:
    analysing("input5.txt","output5.txt")
except:
    print("File Not Found")                