def fib(n):
    a,b=0,1
    while(n>0):
        print a,
        c = a+b
        a=b
        b=c
        n-=1
def oddOrEven(val):
    if(val%2==0):
      return 'Even'
    return 'Odd'


