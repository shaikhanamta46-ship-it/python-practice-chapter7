#chapter 7 flie I/O
#python can be used to perfrom operations on a file (read, write, append etc)
#open a file
#file = open("filename","mode")
 
f = open("demo.txt","r") #oepn a file in read mode
data = f.read() #read the content of the file
print(data)

line1 = f.readline() #read the first line of the file
print(line1)

line2 = f.readline() #read the second line of the file
print(line2)

line3 = f.readline() #read the third line of the file
print(line3)
f.close() #close the file after use

#writing a file

f = open("demo.txt","w") #open a file in the write mode

f.write("hello world")#write a string to the file

f.close()

#append a file
f = open("demo.txt","a") #open a file in the append mode

f.write("welcome to python")#append a string to the file
f.close()

#create a random file
f = open("random.txt","a") #open a file in the append mode

f.write("This is a random file") #write a string to the file
f.close()

#use of with syntax
with open("demo.txt","r") as f:
    data = f.read()
    print(data)

with open("demo.txt","w") as f:
    f.write("hello world")
    print("file written successfully")

#deleting a file
import os
os.remove("random.txt") #delete the file random.txt

#practice question1,2 
with open("practice.txt","r") as f:
    data = f.read()
new_data = data.replace("java","python") #replaces java with python
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)

#practice qeustion 3
#search for a learning keyword in a file
def check_for_word():
    word = "learning"
    with open("practice.txt","r") as f:
        data = f.read()
    if data.find(word) != -1:
        print("word found in the file")
    else:
      print("word not found in the file")
check_for_word()

#practice question4 

def check_for_lines():
   word = "programming"
   data = True
   line_no = 1
   with open("practice.txt","r") as f:
    while data:
            data = f.readline()
            if (word in data):
               print(line_no)
               return
            line_no += 1
    return -1

     
check_for_lines()

#practice question5
#method 1
with open("practice.txt","r") as f: 
    data = f.read()
    print(data)
num = "" 
for i in range(len(data)):
    if(data[i]) == ",":
        print(int(num))
        num = ""
    else:
        num += data[i]
#method 2
count = 0 
nums = data.split(",")#split the data using comma as a delimiter
for val in nums:
    if int(val) % 2 == 0:
        count += 1
print(count)