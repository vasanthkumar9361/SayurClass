a=input("enter the mobile number:")
b=a.replace('-','')
if len(b)==10 and b.isdigit():
    print("valid number")
else:
    print("invalid number")