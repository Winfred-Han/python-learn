


def test_func(compute):
    print(f"参数类型：{type(compute)}")
    result=compute(2,3)
    print(result)

def compute(x,y):
    return x+y

# 匿名函数，lambda表达式
test_func(lambda x,y : x+x*y)