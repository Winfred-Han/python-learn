

def list_while_func():
    """
    用while循环遍历列表
    :return:
    """
    my_list=["传智教育","黑马程序员","python"]
    index=0
    while index<len(my_list):
        element=my_list[index]
        index+=1
        print(f"列表的元素：{element}")


def list_for_func():

    """
    用for循环遍历列表
    :return:
    """
    my_list = [1,2,3,4,5]
    for i in my_list:
        print(i)

# list_while_func()
list_for_func()