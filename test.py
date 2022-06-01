n = int(input())

def printChar(n, c):
    for i in range(n):
        print(c, end='')

for i in range(n):
    printChar(n-i-1, ' ')
    printChar(i+1, '#')
    print('\n')


