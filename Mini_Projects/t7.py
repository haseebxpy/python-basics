import csv
count=0
with open("input7.csv","r") as file:
    reader=csv.reader(file)
    header=next(reader)
    total=0
    for row in reader:
        total+=1
        task=row[0]
        status=row[2]
        print(f"{task}:{status}")
        if status.lower()=="pending":
            count+=1
    print(f"Total Number of Rows:{total}")
    print(f"Total Pending Tasks:{count}")   