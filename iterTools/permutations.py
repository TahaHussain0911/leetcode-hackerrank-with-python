def permutations(string, k, current=""):
    if len(current) == k:
        print(current)
        return
    
    # string=ACHK
    for i in range(len(string)):
        # firs titeration i=1
        # string[:1] ='A' and string[1+1:] = HK -> permutations('AHK',2,'A')
        remaining = string[:i] + string[i+1:]
        permutations(remaining, k, current + string[i]) 

permutations("".join(sorted('HACK')), 2)
