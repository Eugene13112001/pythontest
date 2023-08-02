n = int(input())
a = [0]*n
for i in range(n):
    a[i]=int(input())
a.sort()
first = 0
second = 1
s = 0
while (second < n):
    s+=1
    if (abs(a[first] - a[second])<3):
        first+=2
        second+=2
    else:
        first+=1
        second+=1
if (first == (n-1)):
    s+=1
print(s)