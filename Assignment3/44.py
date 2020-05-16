import math

add = lambda *args : sum(args)
sub = lambda x,y : x-y
mul = lambda x,y : x*y
div = lambda x,y : x/y
mod = lambda x,y : x%y
floor = lambda x : math.floor(x)

if __name__ == "__main__":
    try:
        print add(6,4)
        print sub(6,4)
        print mul(6,4)
        print div(6,4)
        print mod(6,4)
        print floor(6.82134)
    except Exception as e:
        print e
