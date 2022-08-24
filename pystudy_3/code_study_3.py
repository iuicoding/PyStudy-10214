
def print3():
    print('hello')
    print('hello')
    print('hello')
print3()

def printn(value, n):
    for  i in range(n):
        print(value)
printn('hi', 5)
def printnzeta(n,*value):
    for i in range(n):
        for valu in value:
            print(valu)
        print()
printnzeta(3,'hi', 'what', 'gp')

def printndoublezeta(value, n=2):
    for i in range(n):
        for val in value:
            print(val)
printndoublezeta('hi???', n=3)
def test(a, b=10, c=100):
    print(a+b+c)
test(10, 20 ,30)
test(a=10,b=100,c=200)
test(10, c=200)
valuee = input(">")
print(valuee)
def return_test():
    print('a')
    return
    print('b')
return_test()
def return_l():
    return 100
valueee = return_l
print(valueee)
def return_t():
    return
balue = return_t()
print(balue)