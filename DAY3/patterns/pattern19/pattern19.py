'''

***** *****
****   ****
***     ***
**       **
*         *
*         *
**       **
***     ***
****   ****
***** *****
'''


n=int(input())
#loop 1
for i in range(n):
    #first triangle
    for j in range(n-i):
        print("*",end="")
    #spaces
    for k in range(2*i+1):
        print(" ",end="")
    #star
    for j in range(n-i):
        print("*",end="")
    print()
#loop 2
for i in range(n):
    #first
    for j in range(i+1):
        print("*",end="")
    #space
    for k in range(2*n-2*i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()