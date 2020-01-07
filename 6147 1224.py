x = int(input("Please enter 4 digit numbers ex:1430: "))
y = int(input("Please enter the times you want to run: "))
if 1 <= x <= 9999:
    for time in range(y):
#ascending number
        z = x
        ascending = "".join(sorted(str(x)))
#descending numer
        descending = "".join(sorted(str(x), reverse=True))
#screen part
        print("Descending Number- " + str(descending))
        print("Ascending Number- " + str(ascending))
        x = int(descending) - int(ascending)
        print("The number is " + str(x))
        print("This is the " + str(time+1) +" time I run this" )
        if x == z:
            print("this is the " + str(time+1) + " time I run this the final number is " + str(x)) 
            
else:
    print("I SAID 4 NUBERS!!" + "\n" + "RESTART!!")