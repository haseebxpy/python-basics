import csv
with open("input8.csv","r") as file:
    count=0
    pending=0
    completed=0
    haseebhours=0
    content=csv.reader(file)
    header=next(content)
    for text in content:
        count+=1
        employeedata=text[0]
        projectdata=text[1]
        hoursdata=text[2]
        status=text[3]
        print(f"{employeedata} : {projectdata} : {status}")
        if status.lower()=="pending":
            pending+=1
        if status.lower()=="completed":
            completed+=1
        if employeedata.lower()=="haseeb":
            haseebhours+=int(hoursdata)
    print(f"Total Records : {count}")
    print(f"Pending Tasks : {pending}")
    print(f"Completed Tasks : {completed}")
    print(f"Total Hours Worked By Haseeb : {haseebhours}")
