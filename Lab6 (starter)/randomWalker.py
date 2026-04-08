

import random  
import time
from tracemalloc import start

def rs():
   
    return random.choice([-1, 1])

def rwpos(start, nsteps):
    
    time.sleep(0.1)
    print('location is', start)
    if nsteps == 0:
        return start
    else:
        newpos = start + rs()  # take one step
        return rwpos(newpos, nsteps - 1)

def rwsteps(start, low, hi):
   
    walkway = "_"*(hi-low)    
    S = (start-low)          

    walkway = walkway[:S] + "S" + walkway[S:]  

    walkway = " " + walkway + " "              

    print(walkway, "    ", start, low, hi)     
    time.sleep(0.05)

    if start <= low or start >= hi:           
        return 0
    
    else:
        newstart = start + rs()               
        return 1 + rwsteps(newstart, low, hi)  

def rwstepsLoop(start, low, hi):
    walkway = "_"*(hi-low)    
    S = (start-low)           
    walkway = walkway[:S] + "S" + walkway[S:] 
    walkway = " " + walkway + " "              
    print(walkway, "    ", start, low, hi)     
    time.sleep(0.05) 
    steps = 0
    while start > low and start < hi:
        newstart = start + rs()                
        steps += 1
        start = newstart
        walkway = "_"*(hi-low)    
        S = (start-low)           
        walkway = walkway[:S] + "S" + walkway[S:]  
        walkway = " " + walkway + " "              
        print(walkway, "    ", start, low, hi)     
        time.sleep(0.05)
    return steps
    pass

if __name__ == '__main__':
   print(rs())
