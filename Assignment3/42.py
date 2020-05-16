def fib(n):
    a,b=0,1
    while(n>0):
        print a,
        c = a+b
        a=b
        b=c
        n-=1

if __name__ == "__main__":
    try:
        n = int(input("Enter the number of elements in the series: "))
        fib(n)
    except ValueError:
        print "Enter only int values"
    except Exception as e:
        print e






