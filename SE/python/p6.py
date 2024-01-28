'''
Take as input from user aadhar id (last 4 digits), name, age in years and weight in kg
1. Input 3 users data and save in dictionary with aadhar as key
2. Display the orignal data taken from user as single dictonary and in tabular format
3. Modify the name of any user and store it back in the dictionary
4. Enter a new record in the dictionary
5. Delete a specified record from the dictionary

Expected O/P:
C:\\Users\\Administrator\\Downloads\\Python Practs>python p7.py
Enter 3 user's data:
Enter aadhar, name, age and weight for user 1 : 1234 ninad 34 101.5
Enter aadhar, name, age and weight for user 2 : 4321 danin 43 75.8  
Enter aadhar, name, age and weight for user 3 : 4567 pytho 21 45
{1234: ['ninad', '34', '101.5'], 4321: ['danin', '43', '75.8'], 4567: ['pytho', '21', '45']}
Dictionary is :  {1234: ['ninad', '34', '101.5'], 4321: ['danin', '43', '75.8'], 4567: ['pytho', '21', '45']}
Data in tabular format:
Aadhar  Name    Age     Weight
1234     ninad   34      101.5
4321     danin   43      75.8
4567     pytho   21      45
Enter the aadhar number to modify name:4321
Enter the new name:Java
{1234: ['ninad', '34', '101.5'], 4321: ['Java', '43', '75.8'], 4567: ['pytho', '21', '45']}
Enter aadhar, name, age and weight for New User : 7890 Ruby 30 56
{1234: ['ninad', '34', '101.5'], 4321: ['Java', '43', '75.8'], 4567: ['pytho', '21', '45'], 7890: ['Ruby', '30', '56']}
Enter the aadhar number to delete:4567
{1234: ['ninad', '34', '101.5'], 4321: ['Java', '43', '75.8'], 7890: ['Ruby', '30', '56']}
'''
# Create a dictionary from user input
key, data = [],[]
print("Enter 3 user's data:")
for i in range(3):
    a= [a for a in input("Enter aadhar, name, age and weight for user "+str(i+1)+" : ").split()]
    key.append(int(a[0]))
    data.append(a[1:4])
z= zip(key, data)
dict1=(dict(z))
print(dict1)

# Printing the dictionary
print("Dictionary is : ",dict1)
print("Data in tabular format:\nAadhar\tName\tAge\tWeight")
for k, v in dict1.items():
    print(k,"\t", v[0],"\t", v[1],"\t", v[2])

# Modify the name of the second user
adno = int(input("Enter the aadhar number to modify name:"))
if dict1.get(adno,-1) == -1:
    print("record not found")
else:
    name= input("Enter the new name:")
    dict1[adno][0]=name
print(dict1)

# Enter a new record in the dictionary
a= [a for a in input("Enter aadhar, name, age and weight for New User : ").split()]
dict2={int(a[0]):a[1:4]}
dict1.update(dict2)
print(dict1)

# Deleting the specified record from the dictionary
adno = int(input("Enter the aadhar number to delete:"))
dict1.pop(adno)
print(dict1)