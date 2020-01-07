x = int(input("Please enter 4 digit numbers ex:1430: "))
if 1 <= x <= 9999: 
    ascending = "".join(sorted(str(x)))
    descending = "".join(sorted(str(x), reverse=True))
    #print(ascending  + descending)
    #print(int(descending) - int(ascending))
    print(int(descending) - int(ascending))
else:
    print("I SAID 4 NUBERS!!" + "\n" + "RESTART!!")
#if x >= 10000:
    #print("I SAID 4 NUBERS!!" + "\n" + "RESTART!!")
#if x <= 0:
    #print("I SAID 4 NUBERS!!" + "\n" + "RESTART!!")
