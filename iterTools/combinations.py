def printCombinations(string,k):
    sortedString=''.join(sorted(string))
    def combinations(string,k,current=''):
        if(len(current)==k):
            print(current)
            return
        for i in range(len(string)):
            remaining=string[i+1:]
            combinations(remaining,k,current+string[i])
    for i in range(k):
        combinations(sortedString,i+1)
        

printCombinations('HACK',2)
    