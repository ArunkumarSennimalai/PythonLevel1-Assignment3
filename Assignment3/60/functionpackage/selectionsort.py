def selectionsort(list1):
    for i in range(len(list1)):
        min=i
        for j in range(i+1,len(list1)):
            if(list1[min]>list1[j]):
                min=j
        list1[i],list1[min] = list1[min],list1[i]
    return list1
