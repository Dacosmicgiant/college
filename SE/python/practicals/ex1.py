import sys
name=sys.argv[1]
marks=int(sys.argv[2])

print("Hello"+name)
print("Your marks in various formats")

print("Integer: ",marks,"\tOctal",oct(marks),"\tHexadecimal: ",
hex(marks),"\tFloat: ",float(marks),"\tComplex: ",complex(marks))

if(marks>=40):
    print("you have Passed")
else:
    print("You have Failed")
