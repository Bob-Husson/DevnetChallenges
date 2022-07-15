'''
This program checks User Input to see if it is a valid IPv4 Address

Author: Bob Husson

Date: 14 July 2022

All rights reserved
'''
ip4Check = input("Enter IPv4 Address (Type x to End): ")

while ip4Check.upper() != "X":
    valid = True
    if ip4Check.count(".") == 3:
        
        byteList = ip4Check.split(".")
        for byte in byteList:
            if not(byte.isdigit()):
                valid = False
                break
            if not(int(byte) >=0 and int(byte) <= 255):
                valid = False
                break
    else:
        valid = False

    if valid:
        print(ip4Check, "is a Valid IPv4 Address")
    else:
        print(ip4Check, "is not a Valid IPv4 Address")

    ip4Check = input("Enter IPv4 Address (Type x to End): ")