from os import close
import copy 
from operator import itemgetter
import time

starttime= time.time()
f = open("input.txt", 'r')

s = f.readline()
open= []
heap= []
closed= []
parent= {}
BorH= s[0] # bfs or hill climbing
heu= s[2] # which heuristic to use

f.readline() 

# reading start and goal node
start=[] # start node
for _ in range(3):
    s= f.readline()
    lis = (s).split()
    start.append(lis)


f.readline()

def stringify(state):
    st=''
    for j in state:
        for k in j:
            st= st+k
        st= st+' '
    return st
goal= []
for _ in range(3):
    s= f.readline()
    lis = s.split()
    goal.append(lis)

print(f"given initial state={stringify(start)}\ngiven end state to be reached= {stringify(goal)} ")
# storing the goal node as a dictionary. This will be used for 3rd heuristic
# which is "Euclidian distance."
d_goal = dict((j,(x, y)) for x, i in enumerate(goal) for y, j in enumerate(i))

# utility function for converting a list to string.

    

# generate the neigbours of a node.
def movegen(curr_state):
    global closed, open,parent
    state = copy.deepcopy(curr_state)
    neighbors = []
    for i in range(len(state)):
        temp = copy.deepcopy(state)
        if len(temp[i]) > 0:
            elem = temp[i].pop()
            for j in range(len(temp)):
                temp1 = copy.deepcopy(temp)
                if j != i:
                    temp1[j] = temp1[j] + [elem]                    
                    if(parent.get(stringify(temp1))== None):
                        neighbors.append(temp1)
    return neighbors



def goal_state(cur,i):
    global goal  
# since the heuristic of the goal state is the best possible and unique, just check for that.
    if(heuristic(cur,i)==heuristic(goal,i)): 
        return 1
    return 0


def heuristic(state,i): ## calculating the heuristics
    global goal
    hValue = 0    
    if(i=='0'): # if the block is in correct position add 1, else -1
        for i in range(3):
            for j in range(len(state[i])):
                if j >= len(goal[i]):
                    hValue = hValue - 1
                    continue
                if goal[i][j] == state[i][j]:
                    hValue = hValue + 1
                else:
                    hValue = hValue - 1

 # if block is in correct position and all the blocks below it are 
 # in correct position, then add the height of the block else substract the height
    if (i=='1'):
        for i in range(3):
            right= 1
            for j in range(len(state[i])):
                if(right==1):
                    if j >= len(goal[i]):
                        hValue = hValue - j
                        continue
                    if goal[i][j] == state[i][j]:
                        hValue = hValue + j
                    else:
                        hValue = hValue - j
                else:
                    hValue -= j

# Euclidian Norm
    if (i=='2'):
        d_cur = dict((j,(x, y)) for x, i in enumerate(state) for y, j in enumerate(i))
        for i in range(3):
            for j in range(len(state[i])):
                curx, cury = d_cur[state[i][j]]
                goalx, goaly = d_goal[state[i][j]]
                hValue += (((curx-goalx)**2 + (cury-goaly)**2)**(1/2))
    return hValue
        



def bfs(i):
    global parent
    print("bfs")
    cur= copy.deepcopy(start)
    open.append(cur) # add start node to the open
    count = 0
    while(True):
        closed.append(cur)
        count+=1 # no of states explored.
        open.remove(cur)
        
        # if goal state is reached return cur and count
        if(goal_state(cur,i)):
            
            print("you have reached the goal.")
            return cur ,count
        
        
        cur_heu= heuristic(cur,i) # find heuristic of current node
        neighbours= movegen(cur)
        for neighour in neighbours:
            heap.append([neighour,heuristic(neighour,i)])
            open.append(neighour)
            st= stringify(neighour)
            cu= stringify(cur)
            
            parent[st]=cu
        
        # remove the current node from the heap.
        cur_list= [cur, cur_heu]
        if cur_list in heap:
            heap.remove(cur_list)
        
        # if open list becomes empty there is no way you can reach the state
        if(len(open)==0):
            print("You cannot reach the goal state")
        

        if(i=='0' or i=='1'): # for first two heuristics, we have to maximise it, so we extract max from heap
            current_heap = copy.deepcopy(max(heap,key=itemgetter(1))) 
        else: # for last one, it is minimizing problem. so extract minimum.
            current_heap= copy.deepcopy(min(heap,key=itemgetter(1)))     
        cur = current_heap[0]


def hillclimbing(i):
    global parent
    print("hill climbing")
    cur= copy.deepcopy(start)
    open.append(cur)
    count=0
    while(True):
        closed.append(cur)
        count+=1
        
        open.remove(cur)
        
        if(goal_state(cur,i)):
            
            print("you have reached the goal.")
            return cur ,count
        
        
        cur_heu= heuristic(cur,i)
        neighbours= movegen(cur)
        heap= []
        for neighour in neighbours:
            open.append(neighour)
            heap.append([neighour,heuristic(neighour,i)])
            
            st= stringify(neighour)
            cu= stringify(cur)
            parent[st]=cu
        
        cur_list= [cur, cur_heu]
        if cur_list in heap:
            heap.remove(cur_list)
        
        if(len(open)==0):
            print("You cannot reach the goal state")
            print(f"no of states explored= {count}")
            exit()
        
        if(i=='0' or i=='1'):
            current_heap = copy.deepcopy(max(heap,key=itemgetter(1))) 
        else:
            current_heap= copy.deepcopy(min(heap,key=itemgetter(1)))  

        if(heuristic(cur,i)==heuristic(current_heap[0],i)): # if there is a better node than current, its heuristic will be greater than the current then we go there.  # else just 
            print("You did not reach the goal state")
            print(f"no of states explored= {count}")
            exit()


        cur = current_heap[0]
    

starts= ''
for j in start:
    for k in j:
        starts=starts+k
    starts= starts+' '




if(BorH=='0'):
    
    cur,count= bfs(heu)
elif(BorH=='1'):
    cur,count= hillclimbing(heu)
print(f"no of states explored= { count }")
cu=''
for j in cur:
    for k in j:
        cu=cu+k
    cu= cu+' '


print("the sequence of moves to reach goal state(read from the end):")
while(starts!= cu):
    print(f"{cu}")
    cu= parent[cu]

print(starts)
print("the sequence of moves to reach goal state(read from the end):")
print(f"time taken= {time.time()-starttime}")