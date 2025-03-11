from datetime import datetime
def runTime(func):
    def wrapper(*args,**kwargs):
        start = datetime.now()
        func(*args,**kwargs)
        end = datetime.now()
        return end-start
    return wrapper
g


@runTime
def doSomething():
    for i in range(0,200):
        print(i)

#print(doSomething())
dictionery={}
def cache(func):
    def wrapper(n):
        if func not in dictionery:
            dictionery[func] = func(n)
        return dictionery[func]
    return wrapper



@runTime
@cache
def Fibonacci(n):
    if n<=1:
       return 1
    return Fibonacci(n-1)+Fibonacci(n-2)
print(Fibonacci(20))
print(Fibonacci(20))



