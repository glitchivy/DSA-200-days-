'''
1      1
12    21
123  321
12344321
'''

n=int(input())
for i in range(n):
    #number1
    for j in range(i+1):
        print(j+1,end="")
    #space
    for s in range(2*n-2*i-2):
        print(" ",end="")
    #no2
    for k in range(i+1):
        print(i-k+1,end="")
    print()