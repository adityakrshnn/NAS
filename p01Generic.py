#First line of input is space-separated values in L1
#Second line of input is space-separated values in L2

#For Example:
#a b c d e f g
#b c d

if __name__ == '__main__':
    d={}
    common=[]
    l1=[str(x) for x in input().split()]
    l2 = [str(x) for x in input().split()]
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