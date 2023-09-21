#Raduis of Circle
x = float(input("Radius of Circle="))

if x<0:
    print("Enter Appropriate Value")

else:
    y=x**2
    print(y*3.14159265359)


#file extension

filename = input("Enter the Filename : ")
extension = filename.split(".")
print("File extension is :", extension[-1] if len(extension) > 1 else "unknown extension")