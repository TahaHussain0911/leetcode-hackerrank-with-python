A=[1,2]
B=[3,4]
def cartesian_product(arr1,arr2):
    answer=[]
    for num1 in arr1:
        for num2 in arr2:
            answer.append((num1,num2))
    print(*answer)

cartesian_product(A,B)
