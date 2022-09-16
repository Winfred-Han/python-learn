

def test_func(compute):
    print(f"参数类型：{type(compute)}")
    result=compute(1,2)
    print(result)

def compute(x,y):
    return x+y

def mul(x,y):
    return x*y

def sum(x,y):
    return x+x+x+x+x+y+y+y

# 计算逻辑的传递
test_func(mul)
test_func(compute)
test_func(sum)

