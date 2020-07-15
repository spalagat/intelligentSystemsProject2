# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 18:42:17 2019

@author: sunny
"""
"""In this n*n queen problem queen is represented as '1'"""
import numpy as np
import random as rand
import copy
 
"""This is a class called node,The objects of this node class called node objects represents each n*n matrix
    in object form which stores the matrix and its heuristic value of that particular matrix node"""
class node:
    def __init__(self,state,h):
        self.state = state
        #self.g = g
        self.h = h
    # This method returns h(n) value of that particular puzzle node object.
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
        
        if row!=i:
            
            temp_state[i][j]=temp_state[row][j]
            
            temp_state[row][j] = temp
            row+=1
            row1+=1
            
        else:
            row+=1
            
    return s
        
            
            
"""This method returns the heuristic value of each matrix"""           
def heuristic(state):
    
    queen=np.where(state==1)
    
    queens=[]
    length=len(state)
    for i in range(length):
        queens.append((queen[0][i],queen[1][i]))
    count=0
    for i in range(length-1):
        for j in range(i+1,length):
            if queens[j][0]==queens[i][0]:
                count+=1
            if queens[j][1]==queens[i][1]:
                count+=1
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
        h=heuristic(child)
        child1=node(child,h)
        child_list.append(child1)
    
    
    return child_list


"""This method performs the whole hill_climbing algorithm"""        
def hill_climbing(state):
    i=0
    while True:
        if state.get_h()==0:
            return i,True
        else:
            child_nodes = find_queen(state)
            
            child_nodes.sort(key=lambda x: x.h)
            nxt_state=child_nodes[0]
            #print(nxt_state.get_state())
            print(nxt_state.get_h())
            if nxt_state.get_h()>=state.get_h():
                return i,False
            
            print(nxt_state.get_state())
            state=nxt_state
            i+=1
            
    
            
            
            
        
            
            
            
"""This method is used to create the random input_state"""
def get_Input(length,sample_size):
    count=0
    success_steps=[]
    failure_steps=[]
    for j in range(sample_size):
        state=np.zeros((length,length),int)
        for i in range(length):
            col=i
            row=rand.randint(0,length-1)
            
            
            state[row][col]=1
        print("state:")
        print(state)
        h = heuristic(state)
        initial_state = node(state,h)
        step,result = hill_climbing(initial_state)
        
        if result==True:
            success_steps.append(step)
            count+=1
        else:
             failure_steps.append(step)
    print(count)
    print(sample_size)
    percent = (count/sample_size)*100
    avg_success_steps = np.array(success_steps)
    avg_failure_steps = np.array(failure_steps)
    
    print("Success_percent = "+str(percent))
    print("Average_success_steps"+str(np.average(avg_success_steps)))
    print("Average_failure_steps"+str(np.average(avg_failure_steps)))
    
    
sample_size = int(input("enter the no:of samples to find the solution "))
length = int(input("enter the size of board "))
get_Input(length,sample_size)
