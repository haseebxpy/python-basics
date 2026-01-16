try:
    with open("input2.txt","r") as file:
        lines=file.readlines()
    cleaned_lines=[]
    for line in lines:
        if line.strip() !="":
             cleaned_lines.append(line.upper())
    with open("output2.txt","w") as file:
        for line in cleaned_lines:
            file.write(line)
    print(len(cleaned_lines),"lines combined ")
except:
    print("FILE NOT FOUND")