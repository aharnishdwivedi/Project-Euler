import math
import os
import random
import re
import sys
import array



def d(n):
    count=0
    for i in range(1,n):
        if(n%i==0):
            count=count+1
    return count+1       

def M(n,k):
    max = 0
    for i in range(n,n+k):
        if(d(i)>max):
            max=d(i)
    return max
def S(u,k):
    sum=0
    for n in range (1,u-k+2):
        sum = sum+M(n,k)
    return sum
print(S(1000,10))




        
        

