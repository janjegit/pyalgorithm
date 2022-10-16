def editdist(w,v):
    if len(w)==0:
        return len(v)
    elif len(v)==0:
        return len(w)
    else:
        ed1 = editdist(w[:len(w)-1],v)+1
        ed2 = editdist(w,v[:len(v)-1])+1
        if w[len(w)-1]==v[len(v)-1]:
            ed3 = editdist(w[:len(w)-1],v[:len(v)-1])
        else:
            ed3 = editdist(w[:len(w)-1],v[:len(v)-1])+1
        return min(ed1,ed2,ed3)

print(editdist('HAUS','BAUM'))
print(editdist('BAUMHAUS','BAGGER'))
print(editdist('BAUMHEUS','BAGGER'))
