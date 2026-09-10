print("<<< Matching by position from left to right – positional args >>>")
def function(x, y, z):  #Matching by position from left to right – positional args
    return x+y+z
res1 = function(3, 4, 5)      #matchng values to args by position
print(res1)

print("<<< Matching by argument name – keyword args >>>")
def function1(x, y, z):    #Matching by argument name – keyword args
    return x+y+z
res2=function1(y=6, z=7, x=8)       #matching values to args by argname(a=8)
print(res2)

print("<<< Specify default values for optional args >>>")
def nut(a, b=8, c= 5, d=-1):         #Specify default values for optional args
    return a+b*c-d
res2 = nut(1)
print(res2)

print("<<< Collect arbitrarily many positional or keyword args >>>")
def gun(*args):                #Collect arbitrarily many positional or keyword args
    print(args)
gun(7)

def gun1(*args):
    print(args)
gun(2, 5, 8, 9)

def sun(**kwargs):
    print(kwargs)
sun(name="python", age=37)

def bat(a, *pargs, b, **kwargs):
    print(a, b, pargs, kwargs, sep='-->>')
bat(1, 2, 3, 4, 5, x=6, y=7, z='python', b= 8)

print("<<< Pass arbitrarily many positional or keyword args >>>")
def cat(a, b, c, d):                #Pass arbitrarily many positional or keyword args
    print(a, b, c, d)
args = (5, 6, 7, 8)
cat(*args)

kargs = {"a": "Python", "b": 37, "c": "HYD", "d": 500038}
cat(**kargs)

