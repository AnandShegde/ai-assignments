
import time,sys
open_list= set()
from numpy.core.fromnumeric import shape
# I take the input from line 243-257


dfs_stop= False


sys.setrecursionlimit(10**6)

starttime= time.time()

dfs_stop= False    # tells when dfs to stop

goaldfs= (0,0)     # target state to achieve for DFS
goaldfid= (0,0)    # target state to achieve for DFID
statesdfs=0        # no. of states explored during dfs traversal
statesdfid=0       # no. of states explored during dfid traversal
DFIDstop= False    # to break out of recursion

def goal_state(i,j,graph_input):
    # This function determines whether the coordinate (i,j) is the end goal for the pacman or not .
    if(graph_input[i][j]=='*'):
        return True
    else:
        return False



def move_gen(i,j,graph_input):
    # returning all possible moves available to the pacman.
    # if the adjecent block has a space(' ') or astrik('*') 
    # funtion returns its coordinates
    global open_list

    templist=[]
    if(i<n-1):
        if((graph_input[i+1][j]==' ' or graph_input[i+1][j]=='*') and ((i+1,j) not in open_list)):
            templist.append((i+1,j))
    if(i>0):
        if(graph_input[i-1][j]==' 'or graph_input[i-1][j]=='*') and ((i-1,j) not in open_list):
            templist.append((i-1,j))
    if(j<n-1):
        if(graph_input[i][j+1]==' 'or graph_input[i][j+1]=='*')and ((i,j+1) not in open_list):
            templist.append((i,j+1))
    if(j>0):
        if(graph_input[i][j-1]==' 'or graph_input[i][j-1]=='*') and ((i+1,j) not in open_list):
            templist.append((i,j-1))
    return templist
    


# this is the recursive Dfs utility function
def DFSUtil(v, visited,parent,graph_input,open_list):


    global dfs_stop,goaldfs,statesdfs
    if dfs_stop:
        return
    
    visited.add(v)
    
    templist = move_gen(v[0],v[1],graph_input)


    for neighbour in templist: 
        if neighbour not in open_list:
            open_list.add(neighbour)
    statesdfs+=1
    for neighbour in templist:
        if neighbour not in parent:
            

            parent[neighbour]=v
            open_list.add(neighbour)
            

            if goal_state(neighbour[0],neighbour[1],graph_input):
                goaldfs= neighbour
                dfs_stop= True
            if dfs_stop:
                return        
            DFSUtil(neighbour, visited,parent,graph_input,open_list)
            if dfs_stop:
                return

 
# The function to do DFS traversal.
#  It uses recursive DFSUtil()- dfs utility function
def DFS(graph_input,v=(0,0)):
    global goaldfs,statesdfs
    # Create a set to store visited vertices
    visited = set()
    parent= {}
    

    # Call the recursive helper function
    # to print DFS traversal
    DFSUtil(v, visited,parent,graph_input,open_list)  

    path= [v,goaldfs]
    x= goaldfs

    
    while x!=(0,0):
        path.append(parent[x])
        x= parent[x]

    return path,statesdfs 


# The function to do DFID traversal. It uses
# recursive DFSUtil()- dfs utility function
def DFID(graph_input, depth,v=(0,0)):
    global goaldfid,statesdfid
    # Create a set to store visited vertices
    visited = set()

    # to store the parent of each node. this is used for path
    parent= {} 

    # Call the recursive helper function

    DFIDUtil(v, visited,parent,graph_input, depth)   

    # the path list, i have added initial state(v=(0,0)) and goaldfs(*) at first
    path= [v,goaldfs]

    
    x= goaldfs # used for traversing the parent nodes


    
    while x!=(0,0):
        
        path.append(parent[x])
        x= parent[x]
    return path,statesdfid



# this is recursive DFID- utility function
def DFIDUtil(v, visited,parent,graph_input, depth):
    if depth==0: return
    global DFIDstop,goaldfs,statesdfid,open_list
    if DFIDstop:
        return
        


    visited.add(v)
    
    templist = move_gen(v[0],v[1],graph_input)
    for neighbour in templist: 
        if neighbour not in open_list:
            open_list.add(neighbour)


    for neighbour in templist:
        if depth==0: return
        if neighbour not in visited:
            parent[neighbour]=v
            statesdfid+=1
            if goal_state(neighbour[0],neighbour[1],graph_input):
                goaldfs= neighbour
                DFIDstop= True
            if DFIDstop:
                return

            DFIDUtil(neighbour, visited,parent,graph_input, depth-1)
            if DFIDstop or depth==0:
                return


 # main dfid funtion- which calls DFID- which is dfs version for DFID 
 #the extra thing is the depth here
def dfid(graph_input,v=(0,0)):
    depth = 1
    global open_list
    while not DFIDstop:
        path,statesdfid =DFID(graph_input, depth)
        open_list= set()
        depth+=1

    return path,statesdfid
    




# This is simple bfs
def bfs(graph_input,s=(0,0)):   
    visited={}
    end=0
    
    queue = []
    states= 0

    
    Parents= {}
    queue.append(s)
    visited[s] = True
    

    while queue:

        # Dequeue a vertex from
        # queue 
        s = queue.pop(0)
       

        # Get all adjacent vertices of the
        # dequeued vertex s. If a adjacent
        # has not been visited, then mark it
        # visited and enqueue it
        templist= move_gen(s[0],s[1],graph_input)
        
        for i in templist:
            
            if i not in visited:
                states +=1
                queue.append(i)
                Parents[i]=s
               
                visited[i] = True
                if(goal_state(i[0],i[1],graph_input)): 
                    end=1
                    break
        if end==1:
            break
    
    path= [s,i]
    x= i
    
    while x!=(0,0):
        path.append(Parents[x])
        x= Parents[x]
    return path,states

#simple function to deal with the case wise operation to perform bfs, dfs or dfid as per the requirement
def searchmethod(bdd,graph_input):
    if bdd==0 :
        #bfs
        print("bfs")
        path,states = bfs(graph_input)
    elif bdd==1:
        #dfs
        path,states= DFS(graph_input)
        print("dfs")
    else:
        #dfid
        path,states= dfid(graph_input)
        print("dfid")

    for i in path:
        graph_input[i[0]][i[1]]= '0'
    
    
    return graph_input,states,len(path)




################uncomment the following lines to take input from the terminal###############
# graph_input= []
# m=11
# bdd= int(input())
# for i in range(m):
#     graph_input.append(list(input()))
###############################################################################


graph_input= [] #this stores the input given in as a list of lists

#reading file and adding it to graph_input
file = open("input.txt","r")
lines= file.readlines()
m=len(lines)-1 #no of rows substract 1 because 1st line is bdd
bdd= int(lines[0]) #bfs/dfs/dfid
for i in range(1,m+1):
    st = lines[i] 
    graph_input.append(list(st[:len(st)-1]))
    


n=len(graph_input[0]) # no of coloums


# this will give the answer
graph_input,states,pathlength= searchmethod(bdd,graph_input)






f = open("output.txt","w")
f.write(f"states= {states+1}, path length= {pathlength-1} \n")
for i in graph_input:
    ## Uncomment the following line to print the answer in the terminal
    #print(*i,sep='')
    strin= ''.join(map(str,i))
    f.write(strin+"\n")
f.close()


print(f"time taken = {time.time()-starttime} ")

