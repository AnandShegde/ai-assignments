______________________________________________________________________________________________
----------------------------------------------------------------------------------------------

-->> A.I Assignment-2 :
     
    (Team - 14)

    ->> Input Format :

        Algorithm_Mode[0:Best-First-Search,1:Hill-climbing]  Heuristic_Function[0,1,2]

        Start State

        Goal State
    ->> Example :
        0 1

        E B F
        D A 
        C

        A D B
        E F C

    ->> Output Format :
        stack1 stack2 stack3
    ->> Example :
        EB DAC F
        EBF DAC
        EBF DA C

        We are printing the path to the goal state in reverse.
        This means the initial configuration was stack1= E B F, stack2= D A stack3= C
                                        next is: stack1= E B F, stack2= D A C stack3=  (empty)
                                        Final is: stack1= E B , stack2= D A C stack3= F
______________________________________________________________________________________________
----------------------------------------------------------------------------------------------













