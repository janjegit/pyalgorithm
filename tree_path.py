def next_pos(path):
    result = ''
    i = len(path)-1
    while i>=0 and path[i]!='l':
        result = 'l' + result
        i = i-1
    if i<0:
        result = 'l' + result
    else:
        result = path[0:] + 'r' + result
    return result

def prev_pos(path):
    if len(path)>0:
        result = ''
        i = len(path)-1
        while i>=0 and path[i]!='r':
            result = 'r' + result
            i = i-1
        if i<0:
            result = result[1:] 
        else:
            result = path[0:i] + 'l' + result
        return result
    else:
        return ''

