def analyzing(input_file,output_file):
    count=0
    text=[]
    with open(input_file,"r") as file:
       for line in file:
          if line.strip()!="":
             count+=1
             if "python" in line.lower():
                text.append(line.strip())
    with open(output_file,"w") as file:
          file.write(f"Total Lines : {count}\nLines containing 'python':{len(text)} \nMatched Lines:\n")
          for index,data in enumerate(text,start=1):
              file.write(f"{index}. {data}\n")
analyzing("input3.txt","output3.txt")