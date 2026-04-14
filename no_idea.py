def no_idea(arr, liked_set, disliked_set):
    happiness=0
    for num in arr:
        if num in liked_set:
            happiness+=1
        elif num in disliked_set:
            happiness-=1
        
    # for num in liked_set:
    #     if num in arr:
    #         happiness+=1
    # for num in disliked_set:
    #     if num in arr:
    #         happiness-=1
    return happiness


N,M=map(int,input().split())
arr = list(map(int, input().split()))
liked_set = set(map(int, input().split()))
disliked_set = set(map(int, input().split()))
print(no_idea(arr,liked_set,disliked_set))