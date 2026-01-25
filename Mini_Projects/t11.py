import csv
with open("input11.csv","r") as file:
    context=csv.reader(file)
    header=next(context)
    alldata=[]
    for text in context:
        student=text[0].strip()
        subject=text[1].strip()
        marks=text[2].strip()
        if int(text[2])>=50:
            result="Pass"
        else:
            result="Fail"
        alldata.append([student,subject,marks,result])
with open("output11.csv","w",newline='') as file:
    write=csv.writer(file)
    write.writerow(["Student","Subject","Marks","Results"])
    write.writerows(alldata)
    
