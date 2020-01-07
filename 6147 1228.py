time = 0
y = 10
x = 1000
while time < y:
    #ascending number
    str(x).zfill(4)
    ascending = "".join(sorted(str(x)))
#descending numer
    descending = "".join(sorted(str(x)), reverse=True)
#screen part
    x = int(descending) - int(ascending)
    print("This is the " + str(time+1) +" time I run this" )
    print("The number is " + str(x))
    time += 1