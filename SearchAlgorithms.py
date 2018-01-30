def binarySearch(alist,target):
    maximum=len(alist)-1
    minimum=0
    exist=False

    while minimum<=maximum and not exist:
        mid=(maximum+minimum)//2
        if alist[mid]==target:
             exist=True
        elif alist[mid]<target:
             minimum=mid+1
        else:
             maximum=mid-1
    return exist

def interpolationSearch(alist,lowest,highest,target):
    distance=target-alist[lowest]
    value_range=alist[highest]-alist[lowest]
    ratio=distance/value_range

    found=False
    estimation=lowest+ratio*(highest-lowest)
    estimation=int(estimation)

    if alist[estimation]==target:
        found=True
    elif target<alist[estimation]:
        highest=estimation
    else:
        lowest=estimation

    while lowest<=highest and not found:
        mid=(lowest+highest)//2
        if alist[mid]==target:
             found=True
        elif alist[mid]<target:
             lowest=mid+1
        else:
             highest=mid-1
    return found    

if __name__=="__main__":
    array=[0,4,7,9,12,14,18,25,27,36,46,50,64,79,88]
    print(binarySearch(array,0))
    print(binarySearch(array,1021))
    print(interpolationSearch(array,min(array),len(array)-1,46))
