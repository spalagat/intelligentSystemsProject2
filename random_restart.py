# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 01:02:08 2019

@author: sunny
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 18:42:17 2019

@author: sunny
"""

import numpy as np
import random as rand
import copy
from queue import PriorityQueue
from operator import itemgetter 
"""This is a class called node,The objects of this node class called node objects represents each n*n matrix
    in object form which stores the matrix and its heuristic value of that particular matrix node"""
class node:
    def __init__(self,state,h):
        self.state = state
        
        self.h = h
    # This method returns h(n) value of that particular matrix node object.
    def get_h(self):
        return self.h
    # This method returns the matrix related to the particular node object.
    def get_state(self):
        return self.state
#This method returns possible child states for each queen    
def child_nodes(i,j,state):
    length=len(state)
    temp=state[i][j]
    #print(i,j)
    temp=state[i][j]
    s=[]
    for w in range(length-1):
        s1=np.copy(state)
        s.append(s1)
    row=0
    row1=0
    while row1<len(s) and row<length:
        temp_state=s[row1]
        #print(temp_state)
        if row!=i:
            #print("row,col",row,j)
            temp_state[i][j]=temp_state[row][j]
            
            temp_state[row][j] = temp
            row+=1
            row1+=1
            #print(state[row][j])
        else:
            row+=1
            #print(row1)
    return s
        
            
            
"""This method returns the heuristic value of each matrix"""                      
def heuristic(state):
    #print(type(state))
    queen=np.where(state==1)
    #print(queen)
    queens=[]
    length=len(state)
    for i in range(length):
        #print(i)
        queens.append((queen[0][i],queen[1][i]))
    #l2=[]
    count=0
    #print(queens)
    for i in range(length-1):
        for j in range(i+1,length):
            if queens[j][0]==queens[i][0]:
                count+=1
                #print('sandeep')
                #print(j,i)
                #print(l1[j],l1[i])
            if queens[j][1]==queens[i][1]:
                count+=1
                #print('sai')
                #print(l1[j],l1[i]) 
            if (queens[j][0]+queens[j][1]==queens[i][0]+queens[i][1]) or (abs(queens[j][0]-queens[i][0])==abs(queens[j][1]-queens[i][1])):
                count+=1
                
    
    return (count)
            
            
            
            
            
        
            
        
            
    
    
"""This method returns the child_nodes of each matrix"""
def find_queen(parent_state):
    state=parent_state.get_state()
    queen=np.where(state==1)
    #print(queen)
    queens=[]
    length=len(state)
    child_list=[]
    children=[]
    for i in range(length):
        #print(i)
        queens.append((queen[0][i],queen[1][i]))
    
    length = len(state)
    
    for pos in range(length):
        i=queens[pos][0]
        j=queens[pos][1]
        children=children+child_nodes(i,j,state)
    for child in children:
        #print("child",child)
        h=heuristic(child)
        child1=node(child,h)
        child_list.append(child1)
    
    #print(len(child_list))    
    return child_list

"This method is used to generate a random state whenever the problem is stuck"""
def Random_restart(length):
    state=np.zeros((length,length),int)
    for i in range(length):
        col=i
        row=rand.randint(0,length-1)
        #print(state)
            
        state[row][col]=1
    
    h = heuristic(state)
    #print(h)
    initial_state = node(state,h)
    return initial_state
"""This method performs the whole hill_climbing algorithm"""        
def hill_climbing(state):
    length = len(state.get_state())
    restart=25
    i=0
    #state1=state
    while True:
        #print(state.get_h())
        if state.get_h()==0:
            #print(state.get_state())
            return i,restart,True
        else:
            child_nodes = find_queen(state)
            
            child_nodes.sort(key=lambda x: x.h)
            nxt_state=child_nodes[0]
            #print(nxt_state.get_state())
            print(nxt_state.get_h())
            if nxt_state.get_h()>=state.get_h():
                restart+=1
                
                nxt_state =Random_restart(length)
            
            #print(nxt_state.get_state())
            state=nxt_state
            i+=1
            
            
    
            
            
            
        
            
            
            
"""This method is used to create the random input_state"""
def get_Input(length,sample_size):
    count=0
    step=[]
    restart_counts=[]
    for j in range(sample_size):
        state=np.zeros((length,length),int)
        for i in range(length):
            col=i
            row=rand.randint(0,length-1)
            #print(state)
            
            state[row][col]=1
        print("state:")
        print(state)
        h = heuristic(state)
        #print(h)
        initial_state = node(state,h)
        steps,restart,result = hill_climbing(initial_state)
        #print(result)
        if result==True:
            restart_counts.append(restart)
            step.append(steps)
            count+=1
    avg_restarts = np.array(restart_counts)
    print("restart"+str(restart))
    print("percent = "+str((count/sample_size)*100)) 
    avg_steps = np.array(step)
    
    print("Avg number of steps",np.average(avg_steps))
    print("Avg number of restarts required"+str(np.average(avg_restarts)))
    
sample_size = int(input("enter the no:of samples to find the solution"))
length = int(input("enter the number of queens"))
print(type(length))
get_Input(length,sample_size)
