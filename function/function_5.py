#在函数内部修改修改全局变量
num=100
def testA():
    # num=100
    print(num)
def testB():
    # num=100
    num=500
    print(num)
#通过global可以在函数内部修改全局变量
def testC():
    global num
    num=500
    print(num)
testA()
testB()
testC()
print(num)
