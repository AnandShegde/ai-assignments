from copy import deepcopy
from dis import dis
from math import dist
from turtle import distance
import numpy as np
import matplotlib.pyplot as plt
import time,sys,random
ts= time.time()
def floatconv(l, dtype=float):
    return list(map(dtype, l))


# plt.ion()
# print()
# print(len(distances))

#greedy.
def plot_tour(point_pairs,title= "Tour"):
    global points
    
    
    plt.scatter(points[:,0],points[:,1])
    
    for i in point_pairs:
        j= point_pairs[i]
        plt.plot([points[i,0],points[j,0]],[points[i,1],points[j,1]])   
    plt.title(title)
    plt.show()
    

def greedy(start=35):
    global distanc,points
    distances = deepcopy(distanc)
    point_pairs= {}
    cost= 0
    i = start
    while (True):
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


    for i in point_pairs:
        j= point_pairs[i]
        plt.plot([points[i,0],points[j,0]],[points[i,1],points[j,1]])
    x={}
    x["path"]= point_pairs
    x['cost']= cost
    print(time.time()-ts)
    plt.show()
    return x
 
    #plt.savefig("greedy.jpg")

def update_pheromone(current,paths,costs,evoparation_rate=0.9,Q= 2):
    current = np.array(current)
    current = current*evoparation_rate
    count =0
    for x in paths:
        for i in x:
            j = x[i]
            current[j][i] += Q/costs[count]
        count +=1

    return current 


def aco(alpha=3,beta=3,no_of_ants=0,evoporation_rate=0.1,old=None):
    global distanc,points,path_min
    mincost= None
    
    
    distances= np.array(distanc)  # distances between the cities. 2D matrix 
                                # distances[i,j] denotes distance from i to j.
    
    
    no_of_vertices = len(points)
    
    
    if(no_of_ants==0):
        no_of_ants= int(len(points)/5)
    
    #no_of_ants= 30
        

    pheromone= [] 
    for i in range(no_of_vertices): # initializing the pheromone.
        new=[]
        for j in range(no_of_vertices):
            new.append(0.1) 
        pheromone.append(new)
    if(old!=None):
        pheromone = update_pheromone( pheromone,paths= [old['path']], costs = [old['cost']],Q= 1 )
      
        
    while(time.time()-ts<250): # the ants will make "no_of_iterations" tours
        paths = []
        cost = np.zeros((no_of_ants,), dtype = float)# the tour cost of each ant.
        for i in range(no_of_ants): # for each ant make a tour.
            path= {}
            allowed = list(range(no_of_vertices))
            
            start =  random.choice(allowed)
            allowed.remove(allowed[start])
            
            cur = start
            
            for j in range(no_of_vertices-1): # we have to add n-1 more cities.
                probablity = np.zeros((len(allowed),1),dtype = float) 
                psum = 0
                for k in range(len(allowed)):
                    
                    if(k!=cur):
                        #print((1/distances[cur][allowed[k]]),pheromone[cur][allowed[k]])
                        probablity[k,0] = ((1/distances[cur][allowed[k]])**(beta))*(pheromone[cur][allowed[k]]**(alpha))
                        psum = psum + probablity[k,0]
                    else:
                        probablity[k,0]= 0
                    
                
                probablity = probablity/psum

                new = int(random.choices(allowed,weights=probablity,k= 1)[0])
                
                allowed.remove(new)
                cost[i] += distances[cur][new]
                path[new] = cur
                
                cur = new
            
            path[start]= cur # make the parent of start as the last one.
            paths.append(path)
            pheromone = update_pheromone(pheromone,paths,cost)
        
        values = cost 
        
        index_min = min(range(len(values)), key=values.__getitem__)
        path = paths[index_min]
        if(mincost==None or mincost>=cost[index_min]):
            mincost =  cost[index_min]
            path_min = path
            print("mincost")
            print(mincost)
            plot_tour(path,title= f"ant {index_min} {cost[index_min]}")
        plot_tour(path,title= f"ant {index_min} {cost[index_min]}") 
            
        
        
        print(time.time()-ts)
                
                
            
                
    
    
    
    
    

if __name__=='__main__':
    
    if(len(sys.argv)==2):
        fi= open(sys.argv[1],"r")
    else:
        fi= open("D:/4th sem/ai/ai-assignments/AI-Assignment-4/euc_100.txt","r")
    typ = fi.readline()
    no_of_nodes= int(fi.readline())

    points= []
    for i in range(no_of_nodes):
        points.append(floatconv(fi.readline().split()))




    distanc= []
    for i in range(no_of_nodes):
        dis= (floatconv(fi.readline().split()))
        dic={}
        for e,j in enumerate(dis):
            dic[e]=j
        distanc.append(dic)

    old = greedy()
    

    aco(old = old)





