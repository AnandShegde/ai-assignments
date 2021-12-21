dfs_stop= False    
# tells when dfs to stop

goaldfs= (0,0)
# target state to achieve

statesdfs=0
# no. of states explored during dfs traversal



def goal_state(i,j,graph_input):
    # This function determines whether the coordinate (i,j) is the end goal for the pacman or not .
    if(graph_input[i][j]=='*'):
        return True
    else:
        return False



def move_gen(i,j,graph_input):
    # returning all possible moves available to the pacman .
    templist=[]
    if(i<n-1):
        if(graph_input[i+1][j]==' ' or graph_input[i+1][j]=='*'):
            templist.append((i+1,j))
    if(i>0):
        if(graph_input[i-1][j]==' 'or graph_input[i-1][j]=='*'):
            templist.append((i-1,j))
    if(j<n-1):
        if(graph_input[i][j+1]==' 'or graph_input[i][j+1]=='*'):
            templist.append((i,j+1))
    if(j>0):
        if(graph_input[i][j-1]==' 'or graph_input[i][j-1]=='*'):
            templist.append((i,j-1))
    return templist
    


def DFSUtil(v, visited,parent,graph_input):
    global dfs_stop,goaldfs,statesdfs
    if dfs_stop:
        return

    visited.add(v)
    
    templist = move_gen(v[0],v[1],graph_input)

    statesdfs+=1

    for neighbour in templist:
        if neighbour not in visited:
            parent[neighbour]=v
            if goal_state(neighbour[0],neighbour[1],graph_input):
                goaldfs= neighbour
                dfs_stop= True
            if dfs_stop:
                return

            DFSUtil(neighbour, visited,parent,graph_input)
            if dfs_stop:
                return

 
# The function to do DFS traversal. It uses
# recursive DFSUtil()
def DFS(graph_input,v=(0,0)):
    global goaldfs,statesdfs
    # Create a set to store visited vertices
    visited = set()
    parent= {}
    # Call the recursive helper function
    # to print DFS traversal
    DFSUtil(v, visited,parent,graph_input)  

    path= [v,goaldfs]
    x= goaldfs
    
    while x!=(0,0):
        path.append(parent[x])
        x= parent[x]
    return path,statesdfs  


    
    
    



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
        # queue and print it
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
                print(f"{i}={Parents[i]}")
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


def movegen(bdd,graph_input):  
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
        print("dfid")

    for i in path:
        graph_input[i[0]][i[1]]= '0'
    
    return graph_input,states,len(path)






bdd= int(input())
m = 11
graph_input= []
for i in range(m):
    graph_input.append(list(input()))

n=len(graph_input[0])
current_position=[0,0]
graph_input,states,pathlength= movegen(bdd,graph_input)
f = open("output.txt","w")
for i in graph_input:
    print(*i,sep='')
    strin= ''.join(map(str,i))
    f.write(strin+"\n")
f.close()
print(f"states= {states+1}, path length= {pathlength-1} ")


    
