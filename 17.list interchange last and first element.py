def swaplist(list):
    get=list[-1],list[0]
    list[0],list[-1]=get
    return list
newlist=[22,33,44,5,7,2,88,98]
print(swaplist(newlist))
