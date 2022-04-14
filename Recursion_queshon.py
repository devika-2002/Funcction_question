def tri_reun(k):
    if (k>0):
        res=k+tri_reun(k-1)
        print(res)
    else:
        res=0
    return res
tri_reun(6)  


