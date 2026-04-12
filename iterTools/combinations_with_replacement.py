def printCombinationWithReplacement(string,k):
    sortedString=''.join(sorted(string))
    def combination_with_replacement(string,k,current=''):
        if(len(current)==k):
            print(current)
            return
        for i in range(len(string)):
            remaining=string[i:]
            combination_with_replacement(remaining,k,current+string[i])
    
    combination_with_replacement(sortedString,k)
        

printCombinationWithReplacement('HACK',2)
    