from os import stat
import random as rd
import numpy as np
import copy 
from operator import itemgetter
import time
from numpy.core.fromnumeric import shape, sort
import itertools as iter
no_var = 6
count=0
no_clauses= 30
parent={}
closed= []
open_list = []
formu= []

ffor= open("formula.txt","w+")

for i in range(no_clauses): 
    temp_list = []
    while(len(temp_list)<3):   
        x= int(np.random.uniform(1,no_var+1))
        ch= rd.random()
        if(ch>0.5):
            x= -x
        if(x not in temp_list and -x not in temp_list):        
            ffor.write(f"{x}, ")
            temp_list.append(x)
    ffor.write("\n")
    formu.append(temp_list)
    
ffor.close()
input_variables= np.random.randint(2,size=(no_var))
input_variables= list(input_variables)
input_variables = ''.join(map(str, input_variables))

print(input_variables)


def evaluate_clause(clause,inpu):
    for i in clause:
        if(i>0):
            if(inpu[i-1]=='1'):
                return 1
        else:
            if(inpu[(-i)-1]=='0'):
                return 1
    return 0

def no_of_clauses(all_clauses,inpu):
    no= 0
    for i in all_clauses:
        if(evaluate_clause(i,inpu)):
            no += 1
    return no

custom_form= [[]]
custom_clause= [1,2,3,4]
custom_input= [0,0,0,0]

print(no_of_clauses(formu,input_variables))

def movegen(state,bits_toggled):
    neighbours=[]
    comb= iter.combinations(range(0,len(state)),bits_toggled)
    for i in comb:
        new= state
        for j in i:
            j= int(j)
            new= new[:j]+str((int(new[j])+1)%2)+new[j+1:]
        neighbours.append(new)
    return neighbours  

def goal_state(formula,inpu):
    global no_clauses
    if(no_of_clauses(formula,inpu)==no_clauses):
        return 1
    return 0



exitrec=0


#VND
def vnd(formula,inpu,toggle):
    print(inpu)
    global count,exitrec
    global no_clauses,no_var
    if(toggle==no_var+1):
        print(f"you can never reach the goal state\ncount= {count}")
        exit()
    print(f"VND with toggle= {toggle}")
    cur = inpu
    open_list.append(inpu)
    while(True):
        closed.append(cur)
        count+=1
        
        open_list.remove(cur)
        if(goal_state(formula,cur)):
            print("you have reached the goal.")
            print(cur,count)
            exitrec=1
            return
        
        if(exitrec==1):
            return
        
        cur_heu= no_of_clauses(formula,cur)
        neighbours= movegen(cur,toggle)
        
        if cur in neighbours:
            neighbours.remove(cur)
        
        print(f"\nlen= {len(neighbours)} \ntoggle= {toggle}")
        heap= []
        for neighour in neighbours:
            open_list.append(neighour)
            heap.append([neighour,no_of_clauses(formula,neighour)])    
            parent[neighour]=cur
            
        
        cur_list = [cur, cur_heu]
        if cur_list in heap:
            heap.remove(cur_list)
        
        if(len(open_list)==0):
            print("circuit is not satisfiable")
            exit()
                
        current_heap = copy.deepcopy(max(heap,key=itemgetter(1))) 
         
        print(f"current={current_heap}")
        if(no_of_clauses(formula,cur)>=no_of_clauses(formula,current_heap[0])): # if there is a better node than current, its no_of_clauses will be greater than the current then we go there.  # else just 
            if(toggle==no_var):
                print(heap)
                print('\n\n\n')
                print("circuit is not satisfiable")
                exitrec=1
                return
            print(f"couldn't find soln with toggle = {toggle} ie local maxima reached. local maxima is {cur},{no_of_clauses(formula,cur)}")
            vnd(formula,cur,toggle+1)
            if(exitrec==1):
                return 
        else:
            toggle=1

        if(current_heap[0] not in closed):
            cur = current_heap[0]
        else:
            if(toggle==no_var):
                print(heap)
                print('\n\n\n')
                print("circuit is not satisfiable")
                exitrec=1
                return
            print(f"couldn't find soln with toggle = {toggle} ie local maxima reached. local maxima is {cur},{no_of_clauses(formula,cur)}")
            vnd(formula,cur,toggle+1)
            if(exitrec==1):
                return 

            
def beam_search(formula,inpu,beamwidth):
    
    
    global count
    global no_clauses,no_var
    
    cur = inpu
    open_list.extend(inpu)
    prevmax=0
    for i in cur:
        print(f"{i}:{no_of_clauses(formula,i)} ",end='')
        prevmax= max(prevmax,no_of_clauses(formula,i))
    print()
    print(prevmax)

    while(True):
        closed.extend(cur)
        count+=len(cur)
        for j in cur:
            open_list.remove(j)
            
            if(goal_state(formula,j)):
                print("you have reached the goal.")
                print(j,count)
                exit()

            cur_heu= no_of_clauses(formula,j)
            neighbours= movegen(j,1)
            
            if j in neighbours:
                neighbours.remove(j)
            
            
            heap= []
            for neighour in neighbours:
                if neighour not in closed:
                    open_list.append(neighour)
                    heap.append([neighour,no_of_clauses(formula,neighour)])

            cur_list = [j, cur_heu]
            if cur_list in heap:
                heap.remove(cur_list)
            
            
        if(len(open_list)==0):
            print("circuit is not satisfiable")
            exit()
        next_states=[]
        max_heuristic=0
        for _ in range(beamwidth):
            if(len(heap)==0):
                break   
            current_heap = copy.deepcopy(max(heap,key=itemgetter(1))[:beamwidth]) 
            heap.remove(current_heap)

            next_states.append(current_heap[0])
            max_heuristic= max(max_heuristic,current_heap[1])
        
        if(max_heuristic<prevmax):
            print(f"stuck in a local maxima, couldn't find the solution\n current max={prevmax}, maxstate={cur[-1]} ")
            exit()

        
        beam_search(formula,next_states,beamwidth)


tenure = []
def movegen_tabu(state,t):
    global tenure
    best_state = ""
    best_heu = -1 
    index=-1
    for i in range(len()):
        if(tenure[i] == 0):
            if(state[i] == '1'):
                new_state = state[:i] + "0" + state[i+1:]
            else:
                new_state = state[:i] + "1" + state[i+1:]
            if(new_state not in closed):
                tenure[i] = t
                h = heuristic(new_state)
                if(h>best_heu):
                    index = i
                    best_heu = h
                    best_state = copy.deepcopy(new_state)
    if(best_state != ""):
        return [best_state,best_heu,index]
    else:
        return 0
    

def movegen_restricted(state,t):
    global tenure
    best_state = ""
    best_heu = -1 
    index = -1
    for i in range(n):
        if(tenure[i] != 0):
            if(state[i] == '1'):
                new_state = state[:i] + "0" + state[i+1:]
            else:
                new_state = state[:i] + "1" + state[i+1:]
            if(new_state not in closed):
                h = heuristic(new_state)
                if(h>best_heu):
                    index = i
                    best_heu = h
                    best_state = copy.deepcopy(new_state)
    if(best_state != ""):
        return [best_state,best_heu,index]
    else:
        return 0

def tabu(state,t):
    global closed,ts 
    condition = True
    best_state = ""
    best_heuristic = -1
    while(condition == True): 
        tf = time.time()
        if(tf-ts > 10):
            f_out.write("Goal state can't be reached lol\n")
            return state       
        heap = []
        closed.append(state)        
        prev_heu = heuristic(state)
        prev_state = copy.deepcopy(state)
        if(prev_heu > best_heuristic):
            best_state = copy.deepcopy(prev_state)
            best_heuristic = prev_heu

        if(prev_heu == k):
            f_out.write("goal state reached\n")
            return state
        next_node = movegen_tabu(state, t)

        if(next_node != 0):
            state = copy.deepcopy(next_node[0])
            prev_heu = next_node[1]
            tenure[next_node[2]] = tenure[next_node[2]] - 1

        else:
            res_node = movegen_restricted(state,t)
            if(res_node != 0 ):
                state = copy.deepcopy(res_node[0])
                prev_heu = res_node[1]
                tenure[res_node[2]] = tenure[res_node[2]]-1
            else:
                f_out.write("Goal state cannot be reached\n")
                return state

    return state

        


vnd(formu,input_variables,1)
beam_search(formu,[input_variables],6)