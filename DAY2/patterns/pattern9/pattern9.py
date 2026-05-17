'''
   *
  ***
 *****
*******
*******
 *****
  ***
   *
'''

n=int(input())

for i in range(n):
    #space 
    for k in range(n-i-1):
        print(" ",end="")
#star
    for j in range(2*i+1):
        print("*",end="")
    print()
for i in range(n):
    #space
    for k in range(i):
        print(" ",end="")
    for j in range(2*n-2*i-1):
        print('*',end="")
    print()