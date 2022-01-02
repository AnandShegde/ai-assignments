import copy
import math

class node:
    def __init__(self):
        self.stacks =[ [] , [] , [] ]
        self.parent = -1
        self.hvalue = 0
        
global  openlist
openlist = []

global closedlist
closedlist = []

global y_goal
global x_goal

y_goal = {}
x_goal = {}

global start
start = node()

global goal
goal = node()

file = open("input.txt", "r")
for i in range(3):
    line = file.readline()
    newline = line.replace("\n","")
    if(len(newline) != 0):
        list = newline.split(" ")
        for box in list:
            start.stacks[i].append(box)

for i in range(3):
    line = file.readline()
    newline = line.replace("\n","")
    if(len(newline) != 0):
        list = newline.split(" ")
        for box in list:
            goal.stacks[i].append(box)

def adding_y_goal():
    global y_goal
    global goal
    for i in range(3):
        for j in range(len(goal.stacks[i])):
            y_goal[goal.stacks[i][j]] = j

def adding_x_goal():
    global x_goal
    global goal
    for i in range(3):
        for j in range(len(goal.stacks[i])):
            x_goal[goal.stacks[i][j]] = i

def goaltest(node):
    global goal
    if node.stacks == goal.stacks:
        return 1
    else:
        return 0

def heuristic1(node):
    global goal
    hValue = 0
    for i in range(3):
        for j in range(len(node.stacks[i])):
            if j >= len(goal.stacks[i]):
                hValue = hValue - 1
                continue
            if goal.stacks[i][j] == node.stacks[i][j]:
                hValue = hValue + 1
            else:
                hValue = hValue - 1
    return hValue

def heuristic2(node):
    global y_goal
    hvalue = 0
    for i in range(3):
        for j in range(len(node.stacks[i])):
            if y_goal[node.stacks[i][j]] == j:
                hvalue = hvalue + 1
            else:
                hvalue = hvalue - 1
    return hvalue

def heuristic3(node):
    global x_goal
    hvalue = 0
    for i in range(3):
        for j in range(len(node.stacks[i])):
            if x_goal[node.stacks[i][j]] == i:
                hvalue = hvalue + 1
            else:
                hvalue = hvalue - 1
    return hvalue

def moveGen1(node):
    global openlist
    global closedlist
    if len(node.stacks[0]) != 0:
        child1 = copy.deepcopy(node)
        child2 = copy.deepcopy(node)
        val = node.stacks[0].pop()
        node.stacks[0].append(val)
        child1.stacks[0].pop()
        child2.stacks[0].pop()
        child1.stacks[1].append(val)
        child2.stacks[2].append(val)
        if closedlist.count(child1.stacks) == 0:
            h = heuristic1(child1)
            child1.hvalue = h
            openlist.append(child1)
        if closedlist.count(child2.stacks) == 0:
            h = heuristic1(child2)
            child2.hvalue = h
            openlist.append(child2)
    if len(node.stacks[1]) != 0:
        child1 = copy.deepcopy(node)
        child2 = copy.deepcopy(node)
        val = node.stacks[1].pop()
        node.stacks[1].append(val)
        child1.stacks[1].pop()
        child2.stacks[1].pop()
        child1.stacks[0].append(val)
        child2.stacks[2].append(val)
        if closedlist.count(child1.stacks) == 0:
            h = heuristic1(child1)
            child1.hvalue = h
            openlist.append(child1)
        if closedlist.count(child2.stacks) == 0:
            h = heuristic1(child2)
            child2.hvalue = h
            openlist.append(child2)
    if len(node.stacks[2]) != 0:
        child1 = copy.deepcopy(node)
        child2 = copy.deepcopy(node)
        val = node.stacks[2].pop()
        node.stacks[2].append(val)
        child1.stacks[2].pop()
        child2.stacks[2].pop()
        child1.stacks[0].append(val)
        child2.stacks[1].append(val)
        if closedlist.count(child1.stacks) == 0:
            h = heuristic1(child1)
            child1.hvalue = h
            openlist.append(child1)
        if closedlist.count(child2.stacks) == 0:
            h = heuristic1(child2)
            child2.hvalue = h
            openlist.append(child2)

def moveGen2(node):
    global openlist
    global closedlist
    if len(node.stacks[0]) != 0:
        child1 = copy.deepcopy(node)
        child2 = copy.deepcopy(node)
        val = node.stacks[0].pop()
        node.stacks[0].append(val)
        child1.stacks[0].pop()
        child2.stacks[0].pop()
        child1.stacks[1].append(val)
        child2.stacks[2].append(val)
        if closedlist.count(child1.stacks) == 0:
            h = heuristic2(child1)
            child1.hvalue = h
            openlist.append(child1)
        if closedlist.count(child2.stacks) == 0:
            h = heuristic2(child2)
            child2.hvalue = h
            openlist.append(child2)
    if len(node.stacks[1]) != 0:
        child1 = copy.deepcopy(node)
        child2 = copy.deepcopy(node)
        val = node.stacks[1].pop()
        node.stacks[1].append(val)
        child1.stacks[1].pop()
        child2.stacks[1].pop()
        child1.stacks[0].append(val)
        child2.stacks[2].append(val)
        if closedlist.count(child1.stacks) == 0:
            h = heuristic2(child1)
            child1.hvalue = h
            openlist.append(child1)
        if closedlist.count(child2.stacks) == 0:
            h = heuristic2(child2)
            child2.hvalue = h
            openlist.append(child2)
    if len(node.stacks[2]) != 0:
        child1 = copy.deepcopy(node)
        child2 = copy.deepcopy(node)
        val = node.stacks[2].pop()
        node.stacks[2].append(val)
        child1.stacks[2].pop()
        child2.stacks[2].pop()
        child1.stacks[0].append(val)
        child2.stacks[1].append(val)
        if closedlist.count(child1.stacks) == 0:
            h = heuristic2(child1)
            child1.hvalue = h
            openlist.append(child1)
        if closedlist.count(child2.stacks) == 0:
            h = heuristic2(child2)
            child2.hvalue = h
            openlist.append(child2)

def moveGen3(node):
    global openlist
    global closedlist
    if len(node.stacks[0]) != 0:
        child1 = copy.deepcopy(node)
        child2 = copy.deepcopy(node)
        val = node.stacks[0].pop()
        node.stacks[0].append(val)
        child1.stacks[0].pop()
        child2.stacks[0].pop()
        child1.stacks[1].append(val)
        child2.stacks[2].append(val)
        if closedlist.count(child1.stacks) == 0:
            h = heuristic3(child1)
            child1.hvalue = h
            openlist.append(child1)
        if closedlist.count(child2.stacks) == 0:
            h = heuristic3(child2)
            child2.hvalue = h
            openlist.append(child2)
    if len(node.stacks[1]) != 0:
        child1 = copy.deepcopy(node)
        child2 = copy.deepcopy(node)
        val = node.stacks[1].pop()
        node.stacks[1].append(val)
        child1.stacks[1].pop()
        child2.stacks[1].pop()
        child1.stacks[0].append(val)
        child2.stacks[2].append(val)
        if closedlist.count(child1.stacks) == 0:
            h = heuristic3(child1)
            child1.hvalue = h
            openlist.append(child1)
        if closedlist.count(child2.stacks) == 0:
            h = heuristic3(child2)
            child2.hvalue = h
            openlist.append(child2)
    if len(node.stacks[2]) != 0:
        child1 = copy.deepcopy(node)
        child2 = copy.deepcopy(node)
        val = node.stacks[2].pop()
        node.stacks[2].append(val)
        child1.stacks[2].pop()
        child2.stacks[2].pop()
        child1.stacks[0].append(val)
        child2.stacks[1].append(val)
        if closedlist.count(child1.stacks) == 0:
            h = heuristic3(child1)
            child1.hvalue = h
            openlist.append(child1)
        if closedlist.count(child2.stacks) == 0:
            h = heuristic3(child2)
            child2.hvalue = h
            openlist.append(child2)


def bfs1():
    global start
    global openlist
    global closedlist
    h = heuristic1(start)
    start.hvalue = h
    openlist.append(start)
    while True:
        openlist.sort(key=lambda x: x.hvalue)
        currentnode = openlist.pop()
        closedlist.append(currentnode.stacks)
        success = goaltest(currentnode)
        if success == 1:
            print("\n=>> Goal reached!")
            print("=>> Number of states explored: "+str(len(closedlist)))
            print("=>> The final state is goal state:")
            print(currentnode.stacks)
            return
        moveGen1(currentnode)

def bfs2():
    global start
    global openlist
    global closedlist
    h = heuristic2(start)
    start.hvalue = h
    openlist.append(start)
    while True:
        openlist.sort(key=lambda x: x.hvalue)
        currentnode = openlist.pop()
        closedlist.append(currentnode.stacks)
        success = goaltest(currentnode)
        if success == 1:
            print("\n=>> Goal reached!")
            print("=>> Number of states explored: "+str(len(closedlist)))
            print("=>> The final state is goal state:")
            print(currentnode.stacks)
            return
        moveGen2(currentnode)

def bfs3():
    global start
    global openlist
    global closedlist
    h = heuristic3(start)
    start.hvalue = h
    openlist.append(start)
    while True:
        openlist.sort(key=lambda x: x.hvalue)
        currentnode = openlist.pop()
        closedlist.append(currentnode.stacks)
        success = goaltest(currentnode)
        if success == 1:
            print("\n=>> Goal reached!")
            print("=>> Number of states explored: "+str(len(closedlist)))
            print("=>> The final state is goal state:")
            print(currentnode.stacks)
            return
        moveGen3(currentnode)

def moveGenHC1(node):
    childNodes = []
    if len(node.stacks[0]) != 0:
        child1 = copy.deepcopy(node)
        child2 = copy.deepcopy(node)
        val = node.stacks[0].pop()
        node.stacks[0].append(val)
        child1.stacks[0].pop()
        child2.stacks[0].pop()
        child1.stacks[1].append(val)
        child2.stacks[2].append(val)
        child1.hvalue = heuristic1(child1)
        childNodes.append(child1)
        child2.hvalue = heuristic1(child2)
        childNodes.append(child2)
    if len(node.stacks[1]) != 0:
        child1 = copy.deepcopy(node)
        child2 = copy.deepcopy(node)
        val = node.stacks[1].pop()
        node.stacks[1].append(val)
        child1.stacks[1].pop()
        child2.stacks[1].pop()
        child1.stacks[0].append(val)
        child2.stacks[2].append(val)
        child1.hvalue = heuristic1(child1)
        childNodes.append(child1)
        child2.hvalue = heuristic1(child2)
        childNodes.append(child2)
    if len(node.stacks[2]) != 0:
        child1 = copy.deepcopy(node)
        child2 = copy.deepcopy(node)
        val = node.stacks[2].pop()
        node.stacks[2].append(val)
        child1.stacks[2].pop()
        child2.stacks[2].pop()
        child1.stacks[0].append(val)
        child2.stacks[1].append(val)
        child1.hvalue = heuristic1(child1)
        childNodes.append(child1)
        child2.hvalue = heuristic1(child2)
        childNodes.append(child2)
    return childNodes

def moveGenHC2(node):
    childNodes = []
    if len(node.stacks[0]) != 0:
        child1 = copy.deepcopy(node)
        child2 = copy.deepcopy(node)
        val = node.stacks[0].pop()
        node.stacks[0].append(val)
        child1.stacks[0].pop()
        child2.stacks[0].pop()
        child1.stacks[1].append(val)
        child2.stacks[2].append(val)
        child1.hvalue = heuristic2(child1)
        childNodes.append(child1)
        child2.hvalue = heuristic2(child2)
        childNodes.append(child2)
    if len(node.stacks[1]) != 0:
        child1 = copy.deepcopy(node)
        child2 = copy.deepcopy(node)
        val = node.stacks[1].pop()
        node.stacks[1].append(val)
        child1.stacks[1].pop()
        child2.stacks[1].pop()
        child1.stacks[0].append(val)
        child2.stacks[2].append(val)
        child1.hvalue = heuristic2(child1)
        childNodes.append(child1)
        child2.hvalue = heuristic2(child2)
        childNodes.append(child2)
    if len(node.stacks[2]) != 0:
        child1 = copy.deepcopy(node)
        child2 = copy.deepcopy(node)
        val = node.stacks[2].pop()
        node.stacks[2].append(val)
        child1.stacks[2].pop()
        child2.stacks[2].pop()
        child1.stacks[0].append(val)
        child2.stacks[1].append(val)
        child1.hvalue = heuristic2(child1)
        childNodes.append(child1)
        child2.hvalue = heuristic2(child2)
        childNodes.append(child2)
    return childNodes

def moveGenHC3(node):
    childNodes = []
    if len(node.stacks[0]) != 0:
        child1 = copy.deepcopy(node)
        child2 = copy.deepcopy(node)
        val = node.stacks[0].pop()
        node.stacks[0].append(val)
        child1.stacks[0].pop()
        child2.stacks[0].pop()
        child1.stacks[1].append(val)
        child2.stacks[2].append(val)
        child1.hvalue = heuristic3(child1)
        childNodes.append(child1)
        child2.hvalue = heuristic3(child2)
        childNodes.append(child2)
    if len(node.stacks[1]) != 0:
        child1 = copy.deepcopy(node)
        child2 = copy.deepcopy(node)
        val = node.stacks[1].pop()
        node.stacks[1].append(val)
        child1.stacks[1].pop()
        child2.stacks[1].pop()
        child1.stacks[0].append(val)
        child2.stacks[2].append(val)
        child1.hvalue = heuristic3(child1)
        childNodes.append(child1)
        child2.hvalue = heuristic3(child2)
        childNodes.append(child2)
    if len(node.stacks[2]) != 0:
        child1 = copy.deepcopy(node)
        child2 = copy.deepcopy(node)
        val = node.stacks[2].pop()
        node.stacks[2].append(val)
        child1.stacks[2].pop()
        child2.stacks[2].pop()
        child1.stacks[0].append(val)
        child2.stacks[1].append(val)
        child1.hvalue = heuristic3(child1)
        childNodes.append(child1)
        child2.hvalue = heuristic3(child2)
        childNodes.append(child2)
    return childNodes

def hillClimbing1():
    global start
    statesexplored = 0
    start.hvalue = heuristic1(start)
    currentnode = start
    while True:
        statesexplored = statesexplored + 1
        success = goaltest(currentnode)
        if success == 1:
            print("\n=>> Goal reached!")
            print("=>> Number of states explored: "+str(statesexplored))
            print("=>> The final state is goal state:")
            print(currentnode.stacks)
            return
        nextStates =  moveGenHC1(currentnode)
        nextStates.sort(key=lambda x: x.hvalue)
        bestChild = nextStates.pop()
        if bestChild.hvalue <= currentnode.hvalue:
            print("\n=>> Goal not reached!")
            print("=>> Number of states explored: "+str(statesexplored))
            print("=>> The final state reached is:")
            print(currentnode.stacks)
            return
        currentnode = bestChild
       
def hillClimbing2():
    global start
    start.hvalue = heuristic2(start)
    currentnode = start
    statesexplored = 0
    while True:
        statesexplored = statesexplored + 1
        success = goaltest(currentnode)
        if success == 1:
            print("=>> Goal reached!")
            print("=>> Number of states explored: "+str(statesexplored))
            print("=>> The final state is goal state:")
            print(currentnode.stacks)
            return
        nextStates =  moveGenHC2(currentnode)
        nextStates.sort(key=lambda x: x.hvalue)
        bestChild = nextStates.pop()
        if bestChild.hvalue <= currentnode.hvalue:
            print("\n=>> Goal not reached!")
            print("=>> Number of states explored: "+str(statesexplored))
            print("=>> The final state reached is:")
            print(currentnode.stacks)
            return
        currentnode = bestChild
       
def hillClimbing3():
    global start
    start.hvalue = heuristic3(start)
    currentnode = start
    statesexplored = 0
    while True:
        statesexplored = statesexplored + 1
        success = goaltest(currentnode)
        if success == 1:
            print("=>> Goal reached!")
            print("=>> Number of states explored: "+str(statesexplored))
            print("=>> The final state is goal state:")
            print(currentnode.stacks)
            return
        nextStates =  moveGenHC3(currentnode)
        nextStates.sort(key=lambda x: x.hvalue)
        bestChild = nextStates.pop()
        if bestChild.hvalue <= currentnode.hvalue:
            print("\n=>> Goal not reached!")
            print("=>> Number of states explored: "+str(statesexplored))
            print("=>> The final state reached is:")
            print(currentnode.stacks)
            return
        currentnode = bestChild

print("Choose option: ")
print("1.Best first search \n2.Hill climbing ")
print("\n1 for BFS and 2 for Hill climbing")
choice = input("Enter the choice: ")
if choice == '1':
    print("Type 1 for Heuristic1 function\nType 2 for Heuristic2 function\nType 3 for Heuristic3 function")
    run = input("\n Enter the number: ")
    if run == '1':
        bfs1()
    elif run == '2':
        adding_y_goal()
        bfs2()
    elif run == '3':
        adding_x_goal()
        bfs3()
    else :
        print("/*Run the program again, Error: Enter valid number*/")
elif choice == '2': 
    print("Type 1 for Heuristic1 function\nType 2 for Heuristic2 function\nType 3 for Heuristic3 function")
    run = input("\n Enter the number: ")
    if run == '1':
        hillClimbing1()
    elif run == '2':
        adding_y_goal()
        hillClimbing2()
    elif run == '3':
        adding_x_goal()
        hillClimbing3()
    else :
        print("/*Run the program again, Error: Enter valid number*/")
else:
    print("/*Run the program again, Error: Enter valid number*/")