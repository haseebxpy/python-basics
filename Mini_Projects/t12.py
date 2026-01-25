import csv
with open("input12.csv","r") as file:
    content=csv.reader(file)
    header=next(content)
    alldata=[]
    count=0
    completedorders=[]
    pendingorders=[]
    totalpendingamount=0
    pendinghaseebamount=0
    for text in content:
        orderid=text[0].strip()
        customer=text[1].strip()
        amount=text[2].strip()
        status=text[3].strip()
        count+=1
        if status.strip().lower()=="pending":
            pendingorders.append(text)
        if status.strip().lower()=="completed":
            completedorders.append(text)
        amount=int(amount)
        if status.strip().lower()=="pending":
            totalpendingamount+=int(amount)
        if customer.strip().lower()=="haseeb":
            pendinghaseebamount+=int(amount)
        print(f"{orderid}:{customer}:{status}")
print(f"Total Orders : {count}")
print(f"Total Pending Orders : {len(pendingorders)}")
print(f"Total Completed Orders : {len(completedorders)}")
print(f"Total Pending Amount : {totalpendingamount}")
print(f"Total Pending Amount By Haseeb : {pendinghaseebamount}")
with open("output12.csv","w",newline="") as file:
    write=csv.writer(file)
    write.writerow(header)
    write.writerows(pendingorders)
with open("output12.1.csv","w",newline="") as file:
    write=csv.writer(file)
    write.writerow(header)
    write.writerows(completedorders)    