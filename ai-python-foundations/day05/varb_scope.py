print("<<<<--Local scope variable-->>>>")
def greet():
    x="name"
    print(x)
greet()

print("<<<---Global scope variable--->>>")
name="Mahesh"
def func():
    name="Suresh"
    print(name)
func()
print(name)

print("<<<---Enclosed scope variable--->>>")
X = 45
def outer():
    name, X = "Pavan", 35
    print("Enclosed Func", name, X)
    def inner():
        weight, name, X = 55.23, "Ravan", 25
        print(name, weight, X)
    inner()
outer()
print(X)

print("<<< accesing global var inside local fun >>>")
count = 71
def fun1():
    x = 45
    global count
    print(x, count)
fun1()
print(count)

print("<<< accessing global and local scope var inside enclosed fun >>>")
X = 98
print("Initial X:", X)
def f1():
    global X
    global Y
    name, X, Y = "Forest", 97, 88
    print(name, "Updated value of X:", X, Y)
    def f2():
        global X
        global Y
        global Z
        nonlocal name
        name, X, Y, Z = "Amazon Foest", 96, 87, 76
        print("updated name:", name, "last updated X:", X, "last updated Y:", Y, "Z value:", Z)
    f2()
    print(name, X, Y)
f1()
print(X)