from os import stat
import random as rd
import numpy as np
import copy 
from operator import itemgetter
import time
from numpy.core.fromnumeric import shape, sort
import itertools as iter
import time
start_time = time.time()

no_var = 4 # no of literals
count= 0 # no of states explored
no_clauses= 16 # no of clauses
parent={} #parent of a node
closed= [] # closed list
open_list = [] #open list
formu= [] #list for the clauses.

ffor= open("formula.txt","w+") 

for i in range(no_clauses): 
    temp_list = []
    while(len(temp_list)<3):   
        x= int(np.random.uniform(1,no_var+1)) # generate a number between 1 and no of variables. 
        ch= rd.random()
        if(ch>0.5): # i generate its complements with equal probability.
            x= -x
        if(x not in temp_list and -x not in temp_list): # if the generated literal is not in the current clause, add it
            ffor.write(f"{x}, ")
            temp_list.append(x)
    ffor.write("\n")
    formu.append(temp_list) # add the clause to the list.
    
ffor.close() 

fout= open("output.txt","w")

input_variables= np.random.randint(2,size=(no_var)) # generating the initial value for the literals.
input_variables= list(input_variables)
input_variables = ''.join(map(str, input_variables)) # converting the list into a string.

print(f"the initial guess={input_variables} ")
fout.write(f"the initial guess={input_variables} ")

def evaluate_clause(clause,inpu): # checks whether given clause is true for the given value of the literals.
    for i in clause:
        if(i>0):
            if(inpu[i-1]=='1'): #if anyone of the literal is 1 in the clause, then it is satisfied.
                return 1
        else:
            if(inpu[(-i)-1]=='0'):
                return 1
    return 0

def no_of_clauses(all_clauses,inpu): # This is the heuristic funtion. ie, no of clauses satisfied.
    no= 0
    for i in all_clauses:
        if(evaluate_clause(i,inpu)):
            no += 1
    return no



print(f"its heuristic= {no_of_clauses(formu,input_variables)}")
fout.write(f"its heuristic= {no_of_clauses(formu,input_variables)}")

def movegen(state,bits_toggled): # generate the neighbours by toggling specified no of bits.
    neighbours=[]
    comb= iter.combinations(range(0,len(state)),bits_toggled) # generate all possible combinations of selecting a no between 0, no_of_literals.
    for i in comb: # for each combination given,
        new= state 
        for j in i: 
            j= int(j)
            new= new[:j]+str((int(new[j])+1)%2)+new[j+1:] # change the "j"th bit.
        neighbours.append(new)
    return neighbours  # returns a list of strings.

def goal_state(formula,inpu):
    global no_clauses
    if(no_of_clauses(formula,inpu)==no_clauses): # if no of clauses satisfied = no of clauses, goal state is reached.
        return 1
    return 0



exitrec=0 # used for exiting out of recursion.


#VND
def vnd(formula,inpu,toggle):
    
    global count,exitrec
    global no_clauses,no_var
    if(toggle==no_var+1): # if we toggle all the bits, you cannot reach the goal state at all.
        print(f"you can never reach the goal state\ncount= {count}")
        fout.write(f"you can never reach the goal state\ncount= {count}")
        exitrec=1
        return
    
    print(f"VND with toggle= {toggle}")

    cur = inpu 
    # open_list.append(inpu)
    while(True):
        # closed.append(cur)
        count+=1
        
        # open_list.remove(cur)
        if(goal_state(formula,cur)): # if current state is goal state
            print("you have reached the goal.")
            print(cur,count)
            fout.write(f"You have reached the goal.\nno of states explored={count}\nfinal state={cur} ")
            exitrec=1 
            return
        
        if(exitrec==1):
            return
        
        cur_heu= no_of_clauses(formula,cur) # calculate the heuristic of the current.
        neighbours= movegen(cur,toggle) # generate the neighbours.
        
        
        
        print(f"\nlen= {len(neighbours)} \ntoggle= {toggle}")
        heap= []

        for neighour in neighbours:
           
            heap.append([neighour,no_of_clauses(formula,neighour)])    
            
        #remove the current node from the heap if it has gotten into the heap accidentally.
        cur_list = [cur, cur_heu]
        if cur_list in heap: 
            heap.remove(cur_list)
        
              
        current_heap = copy.deepcopy(max(heap,key=itemgetter(1))) # get the max among the neigbours.
         
        print(f"maximum among the neighbours={current_heap}")

        # if there is a better node than current, its no_of_clauses will be greater than the current then we go there.  else just increase the no of toggling and repeat.
        if(no_of_clauses(formula,cur)>=no_of_clauses(formula,current_heap[0])): 
            if(toggle==no_var): # if the maximum no of toggling is reached, say that there is no solution to the problem.               
                print('\n\n\n')
                print("circuit is not satisfiable")
                exitrec=1
                return

            print(f"couldn't find soln with toggle = {toggle} ie local maxima reached. local maxima is {cur},{no_of_clauses(formula,cur)}")
            vnd(formula,cur,toggle+1)
            if(exitrec==1):
                return 
        else:
            toggle=1 # if the toggling was more since we were not able 
            #to find the solution for some toggling, we would have increase the no of toggling to make it denser.
            # but now we don't need denser one, so just revert back to toggle =1.

        cur = current_heap[0] # go the best node among the neibours and repeat the process.
  

            
def beam_search(formula,inpu,beamwidth):      
    global count,exitrec
    global no_clauses,no_var   
    cur = inpu 
    prevmax=0 # maximum heuristic of the previous states.
    for i in cur:
        print(f"{i}:{no_of_clauses(formula,i)} ",end='')
        prevmax= max(prevmax,no_of_clauses(formula,i))
    print()
    print(prevmax)

    heap= []
    while(True):
        count+=len(cur)
        for j in cur: 
            if(goal_state(formula,j)): # check whether the current state is the goal state.
                print("you have reached the goal.")
                print(j,count)
                exitrec=1
                return
            if(exitrec==1):
                return
            
            neighbours= movegen(j,1) # generate the neighbour of each state before it. 

            for neighour in neighbours:
                heap.append([neighour,no_of_clauses(formula,neighour)]) # append each of the neighbour to the heap along with its heuristic value.

            cur_heu= no_of_clauses(formula,j)
            cur_list = [j, cur_heu]
            if cur_list in heap:
                heap.remove(cur_list)
            
            
        if(exitrec==1):
            return

        next_states=[] # the next best nodes.
        max_heuristic=0 # maximum heuristic among the neighours.

        for _ in range(beamwidth): # we need "beamlength" no of next neighbours.
            if(len(heap)==0):
                break   
            current_heap = copy.deepcopy(max(heap,key=itemgetter(1))[:beamwidth]) # i take the maximum among the neighours and add it to our next states list.
            heap.remove(current_heap) # remove the current max, so that i can get the next maximum in next iteration.
            next_states.append(current_heap[0])

            max_heuristic= max(max_heuristic,current_heap[1])
        
        if(max_heuristic<=prevmax): # if none of the neigbours have a heuristic value that is better than the current maximum, we terminate the search.
            print(f"stuck in a local maxima, couldn't find the solution\n current max={prevmax}, maxstate={cur[-1]} ")
            exitrec=1
            return
        if(exitrec==1):
            return
        
        beam_search(formula,next_states,beamwidth) # repeat the search for the next states.
        if(exitrec==1):
                return





tenure= np.zeros(len(input_variables),dtype=int)

def movegen_tabu(state,t):
    global formu
    global tenure
    best_state = ""
    best_heu = -1
    index=-1
    for i in range(len(state)):
        if(tenure[i] == 0):
            if(state[i] == '1'):
                new_state = state[:i] + "0" + state[i+1:]
            else:
                new_state = state[:i] + "1" + state[i+1:]
            # if(new_state not in closed):
            tenure[i] = t
            h = no_of_clauses(formu,new_state)
            if(h>best_heu):
                index = i
                best_heu = h
                best_state = copy.deepcopy(new_state)
    if(best_state != ""):
        return [best_state,best_heu,index]
    else:
        return 0
    

def movegen_restricted(state,t):
    global tenure,formu
    best_state = ""
    best_heu = -1 
    index = -1
    for i in range(len(state)):
        if(tenure[i] != 0): 
            if(state[i] == '1'):
                new_state = state[:i] + "0" + state[i+1:]
            else:
                new_state = state[:i] + "1" + state[i+1:]
            # if(new_state not in closed):
            h = no_of_clauses(formu,new_state)
            if(h>best_heu):
                index = i
                best_heu = h
                best_state = copy.deepcopy(new_state)
    if(best_state != ""):
        return [best_state,best_heu,index]
    else:
        return 0

def tabu(state,t,formula):
    global closed,ts 
    condition = True
    best_heuristic = -1
    while(condition == True): 
        tf = time.time()
        if(tf-ts > 10):
            print("Goal state can't be reached\n")
            fout.write("Goal state can't be reached\n")
            return state       
        
        closed.append(state)        
        prev_heu = no_of_clauses(formula,state)
        # prev_state = copy.deepcopy(state)
        
        if(prev_heu > best_heuristic):
            # best_state = copy.deepcopy(prev_state)
            best_heuristic = prev_heu

        if(goal_state(formula,state)):
            print("goal state is reached")
            print(len(closed))
            print(state)
            print(no_of_clauses(formula,state))
            return
        next_node = movegen_tabu(state, t)

        if(next_node != 0):
            state = copy.deepcopy(next_node[0])
            prev_heu = next_node[1]
            for i in range(len(tenure)):
                if(tenure[i]!=0):
                    tenure[i]-=1
            tenure[next_node[2]] = t

        else:
            res_node = movegen_restricted(state,t)
            if(res_node != 0 ):
                state = copy.deepcopy(res_node[0])
                prev_heu = res_node[1]
                for i in range(len(tenure)):
                    if(tenure[i]!=0):
                        tenure[i]-=1
                tenure[res_node[2]] =t
            else:
                fout.write("goal state cannot be reached")
                print("goal state cannot be reached")
                return state

    return state
  

print("--- %s seconds ---" % (time.time() - start_time))
fout.write("\n\n\nVND\n")
vnd(formu,input_variables,1)

exitrec= 0
fout.write("\n\n\nBEAM SEARCH\n")
print("\n\n\nBEAM SEARCH\n")
beam_search(formu,[input_variables],2)


fout.write("\n\n\nTABU SEARCH\n")
print("\n\n\nTABU SEARCH\n")
ts= time.time()
tabu(input_variables,6,formu)