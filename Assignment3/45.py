def isPalindrome(str1):
        if str1 == str1[::-1]:
            return True
        return False

if __name__ == '__main__':
    try:
        str1=input("Enter the string:")
        print(isPalindrome(str1))
    except TypeError:
        print "Enter only string input"
    except Exception as e:
        print e
        
