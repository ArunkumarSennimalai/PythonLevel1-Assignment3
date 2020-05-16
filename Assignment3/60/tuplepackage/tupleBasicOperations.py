def compareTuple(tup1,tup2):
    greatertuple=tup2
    if cmp(tup1,tup2)==1:
        greatertuple=tup1
    return greatertuple

def findTupleLength(tup1):
    return len(tup1)

def maximumElement(tup1):
    return max(tup1)

def minimumElement(tup1):
    return min(tup1)

def convertToTuple(list1):
    return tuple(list1)
    
def countElement(tup1,element):
    return tup1.count(element) 

def findIndex(tup1,element):
    return tup1.index(element)
