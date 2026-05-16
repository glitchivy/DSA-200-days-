'''
****
****
****
****
'''

# first method
n=int(input())
for i in range(n):
    print(n*'*')


#second method

print("second method")

for i in range(n):
    for j in range(n):
        print("*",end="")
    print()