def capitalize(nameInput):
    return ' '.join(word.capitalize() for word in nameInput.split(' '))


# without using string methods
def customCapitalize(nameInput):
    result=''
    for i in range(len(nameInput)):
        if i==0 or nameInput[i-1] == ' ':
            result+=nameInput[i].upper()
        else:
            result+=nameInput[i]
    return result


name='alan walker'
print(capitalize(name))
print(customCapitalize(name))