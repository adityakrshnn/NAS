if __name__ == '__main__':
    l1=['a','b','c']
    l2=['b','d']
    d={}
    common=[]
    for x in l1:
        if(x not in d):
            d[x] = 1
    for x in l2:
        if(x in d):
            common.append(x)
            d.pop(x)
    print ("Common elements are: "+str(common))
    onlyA = [str(x) for x in d]
    print ("Elements present only in L1 are: "+str(onlyA))
