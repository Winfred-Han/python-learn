

def say_hi():
    """

    :return:
    """
    print("大家好")
res=say_hi()
print(f"无return函数返回值内容为：{res}")
print(f"无return函数返回值类型为：{type(res)}")

if res:
    print(f"真")
else:
    print(f"假")