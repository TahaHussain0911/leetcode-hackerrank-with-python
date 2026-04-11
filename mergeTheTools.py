def merge_the_tools(string, k):
    n=len(string)
    str_chars=[]
    parts=n//k
    for i in range(parts):
        chunk=string[i*k:(i+1)*k]
        print(''.join(dict.fromkeys(chunk)))

merge_the_tools('AABCAAADA',3)