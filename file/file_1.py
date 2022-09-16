import time

# 打开文件
# f=open("E:/file/测试.txt","r",encoding="utf-8")
# print(type(f))
# 读取文件内容
# print(f"读取十个字节的结果：{f.read()}")
# print(f"读取十个字节的结果：{f.read(10)}")
# print(f"读取文件的一行：{f.readline()}")
# print(f"lines对象的内容：{f.readlines()}")
# print(f"读取文件的第一行：{f.readline()}")
# print(f"读取文件的第二行：{f.readline()}")
# print(f"读取文件的第三行：{f.readline()}")
# for line in f:
#     print(f"每行的数据:{line}")
# 关闭文件,程序会持续占用文件知道文件关闭
# f.close()
# time.sleep(500000)

# with open执行完成后会自动关闭文件
with open("E:/file/测试.txt","r",encoding="utf-8") as f:
    for line in f:
        print(f"每一行的数据是:{line}")

