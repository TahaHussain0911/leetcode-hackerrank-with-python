def distinct_average(array):
    arraySet=set(array)
    sum=0;
    for num in arraySet:
        sum+=num
    print(sum / len(array))
    return sum / len(array)

distinct_average([161, 167, 170, 171, 174, 176, 182, 154])