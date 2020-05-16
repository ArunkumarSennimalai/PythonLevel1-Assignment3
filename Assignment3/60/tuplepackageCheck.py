from tuplepackage import *
if __name__ == "__main__":
    try:
        #printing elements in tuple
        tuple1 = ("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")
        printTupleElements(tuple1)
        
        tuple2 = ("January","February","March","April","May","June","July","August","September","October","November","December")
        printTupleElements(tuple2)
        
        
        #finding greater tuple
        tup1 = (34,23,45,12,25,67,89,33,77)
        tup2 = (5,53,65,45,36,67,76,99,10)
        tup3 = (66,55,1,23,9,98,76,45,34,33)    
        findingGreaterTuple(tup1,tup2,tup3)
        
        #trying to delete tuple element and entire tuple
        delTuple(tup1)
        
        #typecating to list 
        list1 = convertToList(tup1)
        
        #inserting value into list
        appendValueToList(list1,123)
        print list1
        
    except Exception as e:
        print(e)
        
        
