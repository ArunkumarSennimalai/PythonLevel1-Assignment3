from functionpackage import selectionsort,oddOrEven,isPalindrome

if __name__ == '__main__':
    try:
        str1=input("Enter the string:")
        print(isPalindrome(str1))

        list1 = [2,3,12,34,1,234,23,455,6778,233,22,12,11]
        sortedlist = selectionsort(list1)
        print sortedlist

        val = input('Enter Value: ')
        print(oddOrEven(val))

    except TypeError:
        print "Enter only string input"
    except Exception as e:
        print e
