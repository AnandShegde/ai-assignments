from dis import dis
from math import dist
from turtle import distance
import numpy as np
import matplotlib.pyplot as plt
import time
ts= time.time()
def floatconv(l, dtype=float):
    return list(map(dtype, l))

fi= open("euc_100.txt","r")

typ = fi.readline()
no_of_nodes= int(fi.readline())

points= []

for i in range(no_of_nodes):
    points.append(floatconv(fi.readline().split()))




distances= {}
for i in range(no_of_nodes):
    dis= (floatconv(fi.readline().split()))
    dic={}
    for e,j in enumerate(dis):
        dic[e]=j
    distances[i]=dic



# print()
# print(len(distances))

#greedy.
point_pairs= {}
cost= 0

start= 35
i=start
while(True):
    if(len(point_pairs)>98):
        break
    while(True):
        ind = min(distances[i],key=distances[i].get)
        
        mindist= distances[i][ind]        
        
        del distances[i][ind]
        if(ind not in point_pairs and i!= ind and ind!=start):
            if(i in point_pairs):
                if(point_pairs[i]!=ind):
                    point_pairs[ind] = i

                    cost += mindist
                    # print(mindist)
                    # print(cost)
                    i=ind
                    break
            else:

                point_pairs[ind]=i
                cost += mindist
                # print(mindist)
                # print(cost)
                i= ind
                break

point_pairs[start]=i
cost+= distances[i][start]
points= np.array(points)


plt.scatter(points[:,0],points[:,1])
plt.title(f"cost={cost}")
print(cost)

print(point_pairs)

for i in point_pairs:
    j= point_pairs[i]
    plt.plot([points[i,0],points[j,0]],[points[i,1],points[j,1]])
        
print(time.time()-ts)
plt.savefig()

