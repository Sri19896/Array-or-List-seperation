
def array_diff(l1, l2):
    l1 = list(l1)
    l2 = list(l2)
    c = 0
    l = len(l1)
    while c != l:
        for i in l1:
            if i in l2:
                l1.remove(i)
        c = c+1
    return(l1)


print(array_diff([1, 2, 2, 3], [2, 3]))
