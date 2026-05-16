'''
    *
   ***
  *****
 *******
'''


n=int(input())

for i in range(n):
    #spaces 
    for j in range(n-i-1):
        print(" ",end="")
    #star
    for k in range(2*i+1):
       
        print("*",end="")
    print()
