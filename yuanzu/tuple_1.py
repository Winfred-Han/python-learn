
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

# 元组的操作：index查找方法
t6=("传智教育","黑马程序员","python")
index=t6.index("黑马程序员")
print(f"元组t6中查找黑马程序员，的下标是：{index}")

# 元组的操作：count统计方法
t7=("传智教育","黑马程序员","黑马程序员","黑马程序员","python")
count=t7.count("黑马程序员")
print(f"元组t7中统计黑马程序员的数量是：{count}")

# 元组的操作：count统计方法
t8=("传智教育","黑马程序员","黑马程序员","黑马程序员","python")
count=len(t8)
print(f"元组t8中统计元素的数量是：{count}")
# 元组的遍历：while
index=0
while index<len(t8):
    print(f"元组的元素有：{t8[index]}")
    index+=1
for i in t8:
    print(f"for元组中的元素有：{i}")
# 修改元素中的内容
# t8[0]='sdfsdf'  这样内容是不可以修改的
t9=[1,2,["itheima","itcast"]]
print(f"t9的内容是：{t9}")
t9[2][0]="黑马程序员"
t9[2][1]="传智教育"
print(f"t9的内容是：{t9}")
