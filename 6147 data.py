import numpy as np
import matplotlib.pyplot as plt
data=[0]*10000
datax=[0]*10000
for x in range(1, 10000):
    y = 10
    time = 0
    x_now = x
    while time < y:
        #ascending number
        z = x_now
        x_now = str(x_now).zfill(4)
        ascending = "".join(sorted(str(x_now)))
        #descending numer
        descending = "".join(sorted(str(x_now), reverse=True))
        #screen part
        x_now = int(descending) - int(ascending)
        # print("The number is " + str(x))
        #print("This is the " + str(time+1) +" time I run this" )
        time += 1
        if x_now == z:
                #print("the " + str(time-1) + " time I ran this program makes the final number which is " + str(x)) 
                time2 = time -1
                data[x] = time2
                datax[x] = x
                time = y
                #print(data[x])     
 
#print("x:" + str(x))
               
plt.plot(datax,data)
plt.show()