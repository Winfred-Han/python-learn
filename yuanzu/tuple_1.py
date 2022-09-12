
# 元组的学习
# 元组定义
t1=(1,"hello",True)
t2=()
t3=tuple()
print(f"t1的类型是：{type(t1)},内容是{t1}")
print(f"t2的类型是：{type(t2)},内容是{t2}")
print(f"t3的类型是：{type(t3)},内容是{t3}")

# 类型就是字符串了
t4=("hello")
# 这样定义类型不是字符串
t4=("hello",)
print(f"t4的类型是：{type(t4)},内容是{t4}")

# 嵌套元组
t5=((1,2,3),(4,5,6))
print(f"t5的类型是：{type(t5)},内容是{t5}")

# 下标索引去取出内容
num=t5[1][2]
print(f"从嵌套元组中取出的数据是:{num}")
