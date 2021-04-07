Coding:

n=int(input())
list1 =list(map(int,input().split()))
i = 0       
while(i < len(list1)):
    if list1[i] % 2 != 0:
        print(list1[i], end = " ")
    i += 1
