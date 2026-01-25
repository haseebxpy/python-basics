import csv
with open("input10.csv","r") as file:
    context=csv.reader(file)
    header=next(context)
    count=0
    pendingline=[]
    completedline=[]
    pendingorder=0
    completedorder=0
    totalpendingamount=0
    haseebamount=0
    for text in context:
        count+=1
        if text[3].strip().lower()=="pending":
            pendingorder+=1
            pendingline.append(text)
            totalpendingamount+=int(text[2])
        if text[3].strip().lower()=="completed":
            completedorder+=1
            completedline.append(text)
        if text[1].lower()=="haseeb":
            haseebamount+=int(text[2])
    print(f"Total Orders : {count}")
    print(f"Pending Orders : {pendingorder}")
    print(f"Completed Orders : {completedorder}")
    print(f"Total Pending Amount : {totalpendingamount}")
    print(f"Total Amount By Haseeb : {haseebamount}")
with open("output10.csv","w",newline='') as file:
    write=csv.writer(file)
    write.writerow(header)
    write.writerows(completedline)
with open("output10.1.csv","w",newline='') as file:
    write=csv.writer(file)
    write.writerow(header)
    write.writerows(pendingline)