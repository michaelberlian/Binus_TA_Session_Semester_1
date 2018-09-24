number= int(input("Input your number : "))

for i in range (1,number+1):
    for p in range (1,i+1):
        print("*",end="")
    print()
print()
for i in range (1,number+1):
    for p in range (1,number+1):
        if ((number-i)>=p):
            print(' ',end="")
        else:
            print('*',end="")
    print()
print()
for i in range (1,number+1):
    for p in range (1,number-i+2):
        print('*',end="")
    print()
print()
for i in range (1,number+1):
    for p in range (1,number+1):
        if (i>p):
            print (' ',end="")
        else:
            print ('*',end="")
    print()
print()
for i in range (1,number+1):
    for p in range (1,2*number):
        if ((p<number-i+1) or (p>number+i-1)):
            print(' ',end="")
        else:
            print('*',end="")
    print()
print()

for i in range (1,number+1):
    for p in range (1,number+i+1):
        if ((p<number-i+1) or (p>number+i-1)):
            print(' ',end="")
        else:
            print('*',end="")
    print()
for i in range (2,number+1):
    print (end=" ")
    for p in range (2,2*number-i+1):
        if ((p>=i) and (p<=(2*number-i))):
            print('*',end="")
        else:
            print(' ',end="")
    print()
print()

for i in range (1,number+1):
    for p in range (1,2*number+i+1):
        if ((p!=number-i+1) and (p!=number+i-1)):
            print(' ',end="")
        else:
            print('*',end="")
    print()
for i in range (2,number+1):
    print (end=" ")
    for p in range (2,2*number-i+1):
        if ((p==i) or (p==(2*number-i))):
            print('*',end="")
        else:
            print(' ',end="")
    print()
print()
