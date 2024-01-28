#convert 254(base 10) into its binary, octal and hex forms. Also, display its type using type function.
a=int(input("enter a number: "))
binaryForm=bin(a)
octalForm=oct(a)
hexadecimalForm= hex(a)
print("binaryForm: ",binaryForm)
print("octalForm: ",octalForm)
print("hexForm: ",hexadecimalForm)
print("type: ", type(a))
