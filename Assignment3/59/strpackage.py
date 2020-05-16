from stringop import *
     
if __name__ == "__main__":
    try:
        list1 = [2,3,12,34,1,234,23,455,6778,233,22,12,11]
        sortedlist = selectionsort(list1) #sorting
        
        x = int(input("Enter the value to be found: "))
        position = binarysearch(sortedlist,x) #binary search
        if(position==-1):
            print "Element not found"
        else:
            print "Element found at position", position
    except ValueError:
            print "Enter only int value"
    except Exception as e:
        print e
