'''
E
D E
C D E
B C D E
A B C D E
'''


n=int(input())
for i in range(n):
    for j in range(i+1):
        print(chr(65+n-i-1+j),end="")
    print()