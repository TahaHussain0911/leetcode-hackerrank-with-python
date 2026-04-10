def doorMatDesigner(n,m):
    pattern='.|.'
    separator='-'
    welcome='WELCOME'
    answer=''
    for i in range(1,n,2):
        answer+=(pattern * i).center(m,separator) + '\n'

    answer += welcome.center(m,'-') + '\n'
    for i in range(n -2,0,-2):
        answer+=(pattern * i).center(m,separator) + '\n'
    print(answer)

doorMatDesigner(7,21)
