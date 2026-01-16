def analysing(inputfile,outputfile):
    count=0
    login=[]
    error=[]
    with open(inputfile,"r") as file:
        for line in file:
            if line.strip()!="":
                count+=1
                if "login" in line.lower():
                    login.append(line.strip())
                if "error" in line.lower():
                    error.append(line.strip())
    with open(outputfile,"w") as file:
        file.write("Activity Report\n---------------\n")
        file.write(f"Total entries: {count}\n")
        file.write(f"Login events: {len(login)}\n")
        file.write(f"Error events: {len(error)}\nError Details: \n")
        for index,data in enumerate (error,start=1):
            file.write(f"{index}. {data}\n")
try:
    analysing("input4.txt","output4.txt")
except:
    print("File Not Found")                