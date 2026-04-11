def minion_game(string):
    string = string.upper()
    vowels = 'AEIOU'
    
    kevinScore = 0
    stuartScore = 0
    length = len(string)
    for i in range(length):
        print(string[i],length - i)
        if string[i] in vowels:
            kevinScore += (length - i)
        else:
            stuartScore += (length - i)
            
    if kevinScore > stuartScore:
        print(f"Kevin {kevinScore}")
    elif stuartScore > kevinScore:
        print(f"Stuart {stuartScore}")
    else:
        print("Draw")

if __name__ == '__main__':
    # Test case
    a = 'BNAANA'
    minion_game(a)