from stringpackage import printEachChar,CountVowels,isPalindrome
        
if __name__ =="__main__":
    try:
        str1 = "Welcome to the class"
        printEachChar(str1)
        CountVowels(str1)
        print isPalindrome(str1)
    except Exception as e:
        print e
