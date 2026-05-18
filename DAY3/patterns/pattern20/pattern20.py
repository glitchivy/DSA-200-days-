'''
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
'''

n=int(input())
for i in range(n):
    # star
    for j in range(i+1):
        print("*",end="")
    #spaces
    for k in range(2*n-2*i-1):
        print(" ",end="")
    #star
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(n):
    for j in range(n-i-1):
        print('*',end="")
    for k in range(2*i+3):
        print(" ",end="")
    for j in range(n-i-1):
        print("*",end="")
    print()
