def binarysearch(list1,x):
    start = 0
    end = len(list1)-1
    while(start<=end):
        mid = start + (end-start)/2
        if list1[mid] == x:
            return mid
        elif x > list1[mid]:
            start = mid+1
        else:
            end = mid-1
    return -1

def search(studentnamelist,name):
    for index in range(len(studentnamelist)):
        if studentnamelist[index] == name:
            return index
    return -1
