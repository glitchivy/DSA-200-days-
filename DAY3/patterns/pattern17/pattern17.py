'''
   A
  ABA
 ABCBA
ABCDCBA
'''

n=int(input())
for i in range(n):
    #spaces
    for s in range(n-i-1):
        print(" ",end="")
    #normal
    for j in range(i+1):
        print(chr(65+j),end="")
    #rev
    for j in range(i):
        print(chr(65+i-j-1),end="")
    print()

