number = int(input("Input the number: "))

for i in range (1,number+1):
    print('*' * i)
for i in range (1,number+1):
    print(' ' * (number-i),'*' * i)
for i in range (1,number+1):
    print('*' * (number-i+1))
for i in range (1,number+1):
    print(' ' * (i-1),'*' * (number-i+1))
for i in range (1,number+1):
    print(' ' * (number-i),'*'*(2*i-1))
for i in range (1,number+1):
    print(' ' * (number-i),'*'*(2*i-1))
for i in range (1,number+1):
    print(' ' * i,'*'*(2*number-2*i-1))
