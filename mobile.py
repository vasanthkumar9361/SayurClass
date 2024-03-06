a = input("Enter the mobile no: ")
if a.startswith('91')  and len(a) > 12:
    print("Invalid,because the numbers are more then expected input")
elif len(a)<10:
    print("invalid ,because the numbers are less then expected input")
elif a.startswith('91') and len(a) == 12 and a.isdigit():
    print("Valid",a)
elif a.startswith('91') and len(a) < 12 and a.isdigit():
    print("valid",a)
elif a.startswith('0') and len(a)==10:
    print("invalid,because any numbers does not starts with '0'")
elif '91' not in a and len(a) == 10 and a.isdigit():
    print("Valid",a)
elif '91' not in a and len(a) == 12:
    print("inValid,because the '91' not came and your number length was un expected")
else:
    print("oops error,because numbers only")
