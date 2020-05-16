def printEachChar(str1):
   for c in str1:
       print(c)
       
def CountVowels(str1):
   vowels = "aeiouAEIOU"
   count=0
   for c in str1:
       if c in vowels:
           count +=1
   print 'ovals = ', count
