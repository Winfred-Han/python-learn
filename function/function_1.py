def say_hi(data):
    print(f"hi 大家好,我是{data}")
say_hi("韩晓东")

def add(x,y):
    """
    一个加法函数
    :param x: 加数1
    :param y: 加数2
    :return: 相加的结果
    """
    res=x + y
    print(f"{x}+{y}={res}")
    return res
result=add(1,2)
print(f"结果是{result}")