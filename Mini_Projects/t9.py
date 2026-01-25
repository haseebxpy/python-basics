import csv
with open("input9.csv","r") as file:
    content=csv.reader(file)
    header=next(content)
    filteredata=[]
    for text in content:
        if text[2].strip().lower()=="pending":    
            filteredata.append(text)

with open("output9.csv","w",newline="") as file:
    write=csv.writer(file)
    write.writerow(header)
    write.writerows(filteredata)