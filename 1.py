s = 0
n = int(input())
count = [False for i in range (n+1) ]
for i in range (2, n+1):
    if (not count[i]):
        for j in range (i*i, n+1, i):
            count[j]=True
for i in range (1, n+1):
    if (not count[i]): s+=i
print(s)
