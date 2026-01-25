count=0
orignal_lines=[]
u=[]
s=[]
e=[]
w=[]
with open("input6.txt","r") as file:
    for line in file:
        if line.strip()!="":
            count+=1
            orignal_lines.append(line.strip())
            if "user" in line.lower():
                u.append(line.strip())
            if "system" in line.lower():
                s.append(line.strip())
            if "error" in line.lower():
                e.append(line.strip())
            if "warning" in line.lower():
                w.append(line.strip())
with open("output6.txt","w") as file:
    file.write("Server Log Analysis Report\n--------------------------")
    file.write(f"\nTotal Records: {count}")
    file.write(f"\nUser Events: {len(u)}")
    file.write(f"\nSystem Events: {len(s)}")
    file.write(f"\nError Events: {len(e)}")
    file.write(f"\nWarning Events: {len(w)}")
    file.write("\nError Event Details:\n")
    errcount=1
    for error in e:
        file.write(f"{errcount}. {error}\n")
        errcount+=1