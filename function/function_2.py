

# 定义函数
def check(degree):
    """
    检查体温是否合格
    :param degree: 体温
    :return: 返回结果
    """
    if(degree>=37.5):
        print(f"你的体温为{degree},过高需要隔离")
    else:
        print(f"你的体温为{degree},体温正常")
check(35)


