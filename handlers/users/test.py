a_kirish = int(input())

n = 1
s = 1
for i in range(a_kirish):
    for j in range(n):
        print(s, end=' ')
        s = s + 1
    n = n + 1
    print()
