import random
arr = [[""]*10 for i in range (0,10)]
x=0
y=0
before = 0
def maps():
    global before
    p = 0
    files = open("maps.txt","r")
    for lines in files : 
        if (len(lines) >5 ):
            pmap = []
            pmap = lines.split(" ")
            pmap[7] = int(pmap[7])
            pmap[7] = str(pmap[7])
            for i in range (0,len(pmap)):
                arr[p][i]=pmap[i]
            p += 1
        else:
            lines = int(lines)
            lines = str(lines)
            before = lines
    files.close
def pmaps():
    global x,y
    for i in range (0,8):
        for p in range (0,8):
            if (arr[i][p] == "0"):
                print ("o",end=" ")
            elif (arr[i][p] == "1"):
                print ("x", end=" ")
                x = i
                y = p
            elif (arr[i][p] == "2"):
                print ("#",end=" ")
        print ()
def write():
    files = open("maps.txt","w")
    temp = ""
    for i in range (0,8):
        for p in range (0,8):
            temp = temp+ arr[i][p]
            if (p !=7):
                temp = temp +" "
            else : 
                temp = temp +"\n" 
    temp = temp + before
    files.write(temp)
    files.close

maps()
while True:
    pmaps()
    print (x,y)
    print ("""
====================
        Menu
====================
[1] Move up
[2] Move down
[3] Move left
[4] Move right
[5] Save & End Game
Choose Menu : [1..5]
    """)
    chose =input()
    if (chose == "1"):
        if (x != 0):
            if (arr[x-1][y]=="2"):
                counter = random.randint(0,1)
                if counter :
                    print ("encounter")
            arr[x][y]=before
            x = x - 1
            before = arr[x][y]
            arr [x][y]="1"
        else:
            print ("you CAN'T GO out from the map!")
    elif (chose == "2"):
        if (x != 7):
            if (arr[x+1][y]=="2"):
                counter = random.randint(0,1)
                if counter :
                    print ("encounter")
            arr[x][y]=before
            x = x + 1
            before = arr[x][y]
            arr [x][y]="1"
        else:
            print ("you CAN'T GO out from the map!")
    elif (chose == "3"):
        if (y != 0):
            if (arr[x][y-1]=="2"):
                counter = random.randint(0,1)
                if counter :
                    print ("encounter")
            arr [x][y]=before
            y = y - 1
            before = arr[x][y]
            arr [x][y]="1"
        else:
            print ("you CAN'T GO out from the map!")
    elif (chose == "4"):
        if (y != 7):
            if (arr[x][y+1]=="2"):
                counter = random.randint(0,1)
                if counter :
                    print ("encounter")
            arr[x][y]=before
            y = y + 1
            before = arr[x][y]
            arr [x][y]="1"
        else:
            print ("you CAN'T GO out from the map!")
    elif (chose == "5"):
        write()
        break