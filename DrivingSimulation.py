time = int(input("Time Spent on the road = "))
acc = int(input("Acceleration = "))
distance = int(input("Distance = "))
for i in range (0,time+1):
    done = acc*i*i/20
    done = int(done)
    print("Duration: ",i,"Distance: ","*" * done)
done = acc*i*i/2
if ((acc*i) > 60):
    print ("The person went over the speed limit. (Max speed was ",acc*i," m/s)")
else:
    print ("The person did not go over the speed limit. (Max speed was ",acc*i," m/s)")
if (done >= distance):
    print("The person reached the destination. (Reached ",done," m)")
else:
    print("The person did not reach the destination. (Reached ",done," m)")