'''
*******
 *****
  ***
   *
'''

# first method
n=int(input())
for i in range(n):
    #for spaces 
    for k in range(i):
        print(" ",end="")
    
    for j in range(2*n-2*i-1):
        print("*",end="")
    print()
