alphabets = ' abcdefghijklmnopqrstuvwxyz'

def print_rangoli(size):
    totalCharsInRow = (size - 1) * 4 + 1
    for i in range(size):
        pattern = getPattern(size, i)
        print(pattern.center(totalCharsInRow, '-'))
    for i in range(size - 2, -1, -1):
        pattern = getPattern(size, i)
        print(pattern.center(totalCharsInRow, '-'))


def getPattern(size, row):
    left = []
    for i in range(row + 1):
        left.append(alphabets[size - i])
    # print(left,left[:-1])
    right = left[:-1][::-1]

    return "-".join(left + right)

print_rangoli(5)