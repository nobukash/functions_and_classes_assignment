#########IMPORT LIBRARIES HERE IF NEEDED#######

################END IMPORTS####################
"""
Write a function that takes a list of integers as input and returns the sum of the even numbers in the list
minus the sum of the odd numbers in the list. The list may contain zeros and negative numbers. For example,
f([0, -4, 2, -3, 6, -1, 8, 6]) should return 22.
"""

def f(l):
    ##########YOUR CODE HERE##########
  b = []
  for l in range(0,n):
    b.append(l)
  
  l1=0
  l2=0
    
  for l in b:
    if(l>0):
      if(l%2==0):
        l1=l1+l
      else:
        l2 = l2+l
    ###########END CODE###############
