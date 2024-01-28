'''
Perform following file operations:
1. Store stocks data (name, high, low, open, close) in a csv file
2. Display all the saved data by reading from file
3. Modify data of any record
3. Count the number of stocks (Line count) and overall entries (word count) and characters in the file
4. Make a copy of an image file

Expected Output:
Enter comma seperated 
stock,  high, low, open, close:sbi,100,95,101,90
enter 1 to exit:1
stock,high,low,open,close
sbi,100,95,101,90

Total records:  2       Total entries:  10      Total characters:  44
Image copied
'''

import os

f= open("demo.csv", "w")
f.write("stock,high,low,open,close\n")
ch = 0
while ch != 1:
    stmt = input("Enter comma seperated \nstock,  high, low, open, close:")
    f.write(stmt+"\n")
    ch = int(input("enter 1 to exit:"))
    if ch ==1:
        break
f.close()

f= open("demo.csv", "r")
print(f.read())
f.close()

with open("demo.csv", "r") as f:
    f.seek(0,0)
    nw,nc=0,0
    nr=0

    for l in f:
        nw=nw+len(l.split(","))
        nr=nr+1
        nc=nc+len(l)
        
    print("Total records: ",nr,"\tTotal entries: ",nw,"\tTotal characters: ", nc)

f1 = open('dog.jpg','rb')
f2 = open('new.jpg','wb')
bytes=f1.read()
f2.write(bytes)
f1.close()
f2.close()
print("Image copied")