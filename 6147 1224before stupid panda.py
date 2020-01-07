x = int(input("Please enter 4 digit numbers ex:1430: "))
if 1 <= x <= 9999: 
#ascending number
    ascending = "".join(sorted(str(x)))
#descending numer
    descending = "".join(sorted(str(x), reverse=True))
#screen part
    print("Descending Number- " + str(descending))
    print("Ascending Number- " + str(ascending))
    print(int(descending) - int(ascending))
else:
    print("I SAID 4 NUBERS!!" + "\n" + "RESTART!!")
