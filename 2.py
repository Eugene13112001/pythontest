a = int(input())
b = int(input())
dif = b - a
dif2 = dif
listnomcoins = [ 1, 2, 5, 10, 50, 100, 200, 500, 1000, 2000, 5000 ]
listuescoins = [0 for i in range (11)]
for i in range (10, -1, -1):
    listuescoins[i] = dif // listnomcoins[i]
    dif = dif % listnomcoins[i]
s = ""
for i in range (len(listnomcoins)-1 , -1, -1):
    dif2-=listnomcoins[i]*listuescoins[i]
    if (listuescoins[i] > 0) and (dif2 != 0):
        s+=f"{listnomcoins[i]} руб: {listuescoins[i]} шт., "
    elif (listuescoins[i] > 0) and (dif2 == 0):
        s+=f"{listnomcoins[i]} руб: {listuescoins[i]} шт. "
print(s)  