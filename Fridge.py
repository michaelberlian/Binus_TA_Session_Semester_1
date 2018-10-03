"""
    http://svn.python.org/projects/stackless/trunk/Lib/encodings/cp720.py
    -> get some ascii number
"""

#do this when wrong input
def trya():
    print ("Do you want to try again?(yes/no)")
    if (input()=="yes"):
        return 1
    elif (input()=="no"):
        return 0
    else:
        return trya()

#Declare things
#save what inside the fridge
fridge ={
    "top"=[],
    "mid"=[],
    "bottom"=[]
}
#save what the value of each item inside the fridge
value ={
    "top"=[],
    "mid"=[],
    "bottom"=[]
}
#help me do the process
slot= ["top","mid","bottom"]
#the current index for me to put something
index ={
    "top"=0,
    "mid"=0,
    "bottom"=0
}
#the current whole value of the fridge section
val ={
    "top"=0
    "mid"=0
    "bottom"=0
}

#Process
while True:
    print (fridge)
    print (value)
    print ("What do you want to do? (put/take/view/exit)")
#Put process
    if (input().lower()=="put"):
        print("Where do you want to put the thing? (top/mid/bottom)")
        place =  input()
        place().lower()
        #so if the input is wrong then it goes back
        if place in slot:
            if (val[place]>15):
                print ("the",place,"fridge is no longer can be filled")
                if trya():continue
                else : exit()
            else:
                print ("What do you want to put?")
                fridge[place].append(input())
                print ("How many space(s) did it take?( 1 -",15-val[place],")")
                value[place].append(input())
                if (value[place][index[place]]+val[place] > 15):
                    del fridge[place][index[place]]
                    del value[place][index[place]]
                    print ("The",place,"fridge can't hold this")
                    if trya():continue
                    else: exit()
                val[place] = val[place]+value[place][index[place]]
                index[place] +=1
        else:
            print ("Wrong input.")
            if trya(): continue
            else: exit()

