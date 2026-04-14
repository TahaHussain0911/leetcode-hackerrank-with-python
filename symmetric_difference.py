def symmetric_difference(set1,set2):
    result=sorted(set1.symmetric_difference(set2))
    for num in result:
        print(num)

M = int(input())
a=set(map(int,input().split()))
N=int(input())
b=set(map(int,input().split()))
symmetric_difference(a,b)