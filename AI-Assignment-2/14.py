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
borh= s[0]
heu= s[2]

f.readline()
start=[]
for _ in range(3):
    s= f.readline()
    lis = (s).split()
    start.append(lis)

f.readline()
goal= []

for _ in range(3):
    s= f.readline()
    lis = s.split()
    goal.append(lis)

d_goal = dict((j,(x, y)) for x, i in enumerate(goal) for y, j in enumerate(i))

def stringify(state):
    st=''
    for j in state:
        for k in j:
            st= st+k
        st= st+' '
    return st
    


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
                    # if (temp1 not in closed and temp1 not in open):
                    
                    if(parent.get(stringify(temp1))== None):
                        # curr_heu=heuristic1(temp1)
                        # open_list.append(copy.deepcopy(temp1))
                        neighbors.append(temp1)
                        # list = [temp1, curr_heu]
                        # heap.append(copy.deepcopy(list))
    return neighbors



def goal_state(cur,i):
    global goal  
    if(heuristic(cur,i)==heuristic(goal,i)):
        return 1
    return 0






def heuristic(state,i):
    global goal
    hValue = 0
    
    
    
    if(i=='0'): 
        
        for i in range(3):
            for j in range(len(state[i])):
                if j >= len(goal[i]):
                    hValue = hValue - 1
                    continue
                if goal[i][j] == state[i][j]:
                    hValue = hValue + 1
                else:
                    hValue = hValue - 1
    if (i=='1'):
        # d_cur = dict((j,(x, y)) for x, i in enumerate(state) for y, j in enumerate(i))
        # for i in range(3):
        #     for j in range(len(state[i])):
        #         curx, cury = d_cur[state[i][j]]
        #         goalx, goaly = d_goal[state[i][j]]
        #         hValue += (abs(curx-goalx) + abs(cury-goaly))
        
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
    open.append(cur)
    count=0
    while(True):
        closed.append(cur)
        count+=1
        # print(count)
        open.remove(cur)
        
        if(goal_state(cur,i)):
            print(goal_state(cur,i))
            print("you have reached the goal.")
            return cur ,count
        
        
        cur_heu= heuristic(cur,i)
        neighbours= movegen(cur)
        for neighour in neighbours:
            heap.append([neighour,heuristic(neighour,i)])
            open.append(neighour)
            st=''
            cu=''
            for j in neighour:
                for k in j:
                    st= st+k
                st= st+' '
            
            for j in cur:
                for k in j:
                    cu=cu+k
                cu= cu+' '
            
            parent[st]=cu
        
        cur_list= [cur, cur_heu]
        if cur_list in heap:
            heap.remove(cur_list)
        
        if(len(open)==0):
            print("You cannot reach the goal state")
        if(i=='0' or i=='1'):
            current_heap = copy.deepcopy(max(heap,key=itemgetter(1))) 
        else:
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
            print(goal_state(cur,i))
            print("you have reached the goal.")
            return cur ,count
        
        
        cur_heu= heuristic(cur,i)
        neighbours= movegen(cur)
        heap= []
        for neighour in neighbours:
            
            heap.append([neighour,heuristic(neighour,i)])
            open.append(neighour)
            st=''
            cu=''
            for j in neighour:
                for k in j:
                    st= st+k
                st= st+' '
            
            for j in cur:
                for k in j:
                    cu=cu+k
                cu= cu+' '
            
            parent[st]=cu
        
        cur_list= [cur, cur_heu]
        if cur_list in heap:
            heap.remove(cur_list)
        
        if(len(open)==0):
            print("You cannot reach the goal state")
            print(count)
            exit()
        
        if(i=='0' or i=='1'):
            current_heap = copy.deepcopy(max(heap,key=itemgetter(1))) 
        else:
            current_heap= copy.deepcopy(min(heap,key=itemgetter(1)))  

        if(heuristic(cur,i)==heuristic(current_heap[0],i)):
            print("You cannot reach the goal state")
            print(count)
            exit()


        cur = current_heap[0]
    

starts= ''
for j in start:
    for k in j:
        starts=starts+k
    starts= starts+' '

print(borh)


if(borh=='0'):
    print("sjoe")
    cur,count= bfs(heu)
    print(f"no of states explored= { count }")
    cu=''
    for j in cur:
        for k in j:
            cu=cu+k
        cu= cu+' '
    
    print(cur)
    print("the sequence of moves to reach goal state(read from the end):")
    while(starts!= cu):
        print(f"{cu}")
        cu= parent[cu]
    
    print(starts)
    print("the sequence of moves to reach goal state(read from the end):")
elif(borh=='1'):
    cur,count= hillclimbing(heu)
    print(f"no of states explored= { count }")
    cu=''
    for j in cur:
        for k in j:
            cu=cu+k
        cu= cu+' '
    
    print(cur)
    print("the sequence of moves to reach goal state(read from the end):")
    while(starts!= cu):
        print(f"{cu}")
        cu= parent[cu]
    
    print(starts)
    print("the sequence of moves to reach goal state(read from the end):")

print(f"time taken= {time.time()-starttime}")