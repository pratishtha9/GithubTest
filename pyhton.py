def recfunc(k):
    if (k>0):
        result=k+recfunc(k-1)
        print(result)
    else:
        result=0
    return result
recfunc(7)

