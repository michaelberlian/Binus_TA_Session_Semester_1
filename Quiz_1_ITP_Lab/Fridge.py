# this when the input wrong
def trya():
    print ("Do you want to try again? (yes/no)")
    x=input().lower()
    if (x=="yes"):
        return 1
    elif (x=="no"):
        return 0
    else:
        return trya()
#helps me a lot
index = {"top":0,"mid":0,"bottom":0}
#save the whole value of the fridge
val = {"top":0,"mid":0,"bottom":0}
#what is inside the fridge
arr = {
    "top":[],
    "mid":[],
    "bottom":[]
}
#the value of each thing that is inside the fridge
value = {
    "top":[], 
    "mid":[],
    "bottom":[]
}
#do a bit but useless
maximum = {
    "top":15,
    "mid":15,
    "bottom":15
}
#help me so much at output
slot = ["top","mid","bottom"]
while True:
    print (arr)
    print (value)
    print("what do you want to do? (view/put/take/exit) ")
    todo= input()
    todo.lower()
    #do the put
    if (todo == "put"):
        print ("where do you want to put?(top/mid/bottom) ")
        place= input()
        place.lower()
        #check wether it has the true input
        if place in slot:
            #decline the thing if the fridge is already full
            if (val[place] == maximum[place]):
                print ("top fridge is already full.")
                if trya(): continue
                else: exit()
            arr[place].append (input("What do you want to put ? "))
            print ("Input the size of",arr[place][index[place]],"? (1 -",maximum[place]-val[place],")",end=" ")
            value[place].append (int(input()))
            #decline the thing if has no size
            if (value[place][index[place]]==0):
                del(value[place][index[place]])
                del(arr[place][index[place]])
                print ("the size can't be 0")
                if trya(): continue
                else: exit()
            #decline the thing if the thing doesn't fit in the fridge
            elif (val[place]+value[place][index[place]] > maximum[place]):
                del(value[place][index[place]])
                del(arr[place][index[place]])
                print("the "+ place +" fridge can't hold this.")
                if trya(): continue
                else: exit()
            val[place] = value[place][index[place]]+val[place]
            index[place] += 1
        #if the input is wrong
        else:
            print("Your input is wrong.")
            if trya() : continue
            else : exit()
    #do the take
    elif (todo == "take"):
        fill=0
        #for if there is nothing on the fridge
        for i in range (0,len(slot)):
            if (val[slot[i]] == 0):
                fill=fill+1
        if (fill == 3):
            print("There is nothing in the fridge.")
            if trya() : continue
            else : exit()
        thingtake=[]
        counter=0
        place=input("Where do you want to take? (top/mid/bottom)")
        place.lower()
        #check the input
        if place in slot:
            #if the section of the fridge has nothing
            if (val[place]==0):
                print("There is nothing in the",place,"fridge.")
                if trya() : continue
                else : exit()
            take=input("what do you want to take? ")
            #check the thing that want to be took
            for i in range (0,index[place]):
                if (take == arr[place][i]):
                    counter +=1
                    thingtake.append(i)
            #if it has more than 1 of the thing 
            if (counter > 1):
                print ("which",take,"you want to take:")
                print (thingtake)
                chosen = int(input())
                #checking the chosen input
                if chosen in thingtake :
                    val[place] = val[place] - value[place][chosen]
                    index[place] = index[place] - 1
                    del arr[place][chosen]
                    del value[place][chosen]
                else:
                    print("wrong input.")
                    if trya() : continue
                    else: exit()
            #if it only has 1 of that thing 
            elif(counter==1):
                val[place] = val[place] - value[place][thingtake[0]]
                index[place] = index[place] - 1
                del arr[place][thingtake[0]]
                del value[place][thingtake[0]]
            else:
                print ("there is no",take,"in",place,"fridge.")
                if trya(): continue
                else: exit()    
        #wrong input
        else:
            print ("Your input is wrong.")
            if trya():
                continue
            else:
                exit()
    #do exit
    elif (todo == "exit"):
        exit()
    #do view
    elif (todo == "view"):   
        #for a better view
        for i in range (0,len(slot)):
            seq=[]  
            count = 0
            #if it has nothing on that section of the fridge
            if (val[slot[i]]==0):
                print ("\u2554"+"\u2550"*(count+7)+"\u2557")
                print ("\u255a"+"\u2550"*(count+7)+"\u255d")
            #if it has thing
            else:
                for q in range (0,len(arr[slot[i]])):
                    seq.append(len(arr[slot[i]][q]))
                count=max(seq)
                print ("\u2554"+"\u2550"*(count+7)+"\u2557")
                for p in range (0,len(arr[slot[i]])):
                    amount = str(value[slot[i]][p])
                    amount = ":"+amount
                    print ("\u2551",("{:^"+ str(count) +"s}").format(arr[slot[i]][p]),("{:>4s}").format(amount),"\u2551")
                print ("\u255a"+"\u2550"*(count+7)+"\u255d")
    #wrong input
    else:
        print ("your input are wrong.")
        if trya(): continue
        else: exit()
