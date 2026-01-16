with open("input1.txt","r") as file:
    context=file.readlines()
    combined=[]
    counter=1
    for line in context:
        if line.strip()!="":
            combined.append((counter,line.lower()))
            counter+=1
with open("output1.txt","w") as file:
    for line,text in combined:
        file.write(f"{line}:{text}")
