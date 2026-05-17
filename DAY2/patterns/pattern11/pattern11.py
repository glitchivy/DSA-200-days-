'''
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
'''

n=int(input())
for i in range(n):
    for j in range(i+1):
        if (i+j)%2==1:
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()