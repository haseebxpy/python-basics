#with open("D:\Python\Mini_Projects\data.txt","r") as file:
  #  lines=file.readlines()
#with open("output.txt","w") as file:
    #for line in lines:
    #    file.write(line.upper)
#try:
   # with open("output.txt","r") as file:
   #     print(file.read())
#except FileNotFoundError:
   # print("File not found. Please check file name")
with open("D:\Python\Mini_Projects\data.txt","r") as file:
    content=file.readlines()
with open("output.txt","w") as file:
    for line in content:
        file.write(line.lower())