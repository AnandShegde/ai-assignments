from os import stat
import random as rd
import numpy as np
import copy 
from operator import itemgetter
import time
from numpy.core.fromnumeric import shape
import itertools as iter
no_var = 20
count=0
no_clauses= 100
parent={}
closed= []
open_list = []
formu= []

ffor= open("abc.txt","w+")

for i in range(no_clauses): 
    temp_list = []
    while(len(temp_list)<4):   
        x= int(np.random.uniform(1,no_var+1))
        ch= rd.random()
        if(ch>0.5):
            x= -x
        if(x not in temp_list and -x not in temp_list):        
            ffor.write(f"{x}, ")
            temp_list.append(x)
    ffor.write("\n")
    formu.append(temp_list)
    

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




# def movegen(state,bits_toggled):
#     neigbours=[]
    
    
#     if(bits_toggled==1):
#         for i in range(len(state)):
            
#             temp_list= state[:i]+ str((int(state[i])+1)%2)+state[i+1:]
#             neigbours.append(temp_list)
    
    
#     else:
#         for i in range(len(state)):
#             temp_list= state[:i]+ str((int(state[i])+1)%2)+state[i+1:]
#             neigbours.append(temp_list)
#         temp=[]
#         for i in neigbours:
#             temp_list = movegen(i,bits_toggled-1)
#             temp.extend(temp_list)
#         neigbours.extend(temp)
#         neigbours= list(set(neigbours))
#     # print(neigbours)
#     return neigbours
    

def goal_state(formula,inpu):
    global no_clauses
    if(no_of_clauses(formula,inpu)==no_clauses):
        return 1
    return 0






#VND



def vnd(formula,inpu,toggle):
    print(inpu)
    global count
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
            exit()
        
        
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
            print("sodijoije")
            exit()
            if(toggle==no_var):
                print("circuit is not satisfiable")
                exit()
            print("here")
            vnd(formula,cur,toggle+1)


        
        
        current_heap = copy.deepcopy(max(heap,key=itemgetter(1))) 
         
        print(f"current={current_heap}")
        if(no_of_clauses(formula,cur)>=no_of_clauses(formula,current_heap[0])): # if there is a better node than current, its no_of_clauses will be greater than the current then we go there.  # else just 
            if(toggle==no_var):
                print(heap)
                print('\n\n\n')
                print("circuit is not satisfiable")
                exit()
            print(f"couldn't find soln with toggle = {toggle} ie local maxima reached. local maxima is {cur},{no_of_clauses(formula,cur)}")
            vnd(formula,cur,toggle+1)
        else:
            toggle=1

        if(current_heap[0] not in closed):
            cur = current_heap[0]
        else:
            if(toggle==no_var):
                print(heap)
                print('\n\n\n')
                print("circuit is not satisfiable")
                exit()
            print(f"couldn't find soln with toggle = {toggle} ie local maxima reached. local maxima is {cur},{no_of_clauses(formula,cur)}")
            vnd(formula,cur,toggle+1)
            

        

vnd(formu,input_variables,1)