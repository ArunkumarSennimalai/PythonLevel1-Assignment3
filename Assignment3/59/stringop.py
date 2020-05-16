def selectionsort(templist1):
    for i in range(len(templist1)):
        min=i
        for j in range(i+1,len(templist1)):
            if(templist1[min]>templist1[j]):
                min=j
        templist1[i],templist1[min] = templist1[min],templist1[i]
    return templist1
  
def binarysearch(templist1,x):
    start = 0
    end = len(templist1)-1
    while(start<=end):
        mid = start + (end-start)/2
        if templist1[mid] == x:
            return mid
        elif x > templist1[mid]:
            start = mid+1
        else:
            end = mid-1
    return -1

def reversestring(tempstr):
    return tempstr[::-1]

