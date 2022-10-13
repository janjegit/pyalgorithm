def next_pos(path):
    result=''
    i = len(path)-1
    while i>=0 and path[i]!='l':
        result='l'+result
        i=i-1
    if i<0:
        result='l'+result
    else:
        result=path[0:i]+'r'+result
    return result

def prev_pos(path):
    result=''
    if len(path)>0:
        i=len(path)-1
        while i>=0 and path[i]!='r':
            result='r'+result
            i=i-1
        if i<0:
            result=result[1:]
        else:
            result=path[:i]+'l'+result
    return result
