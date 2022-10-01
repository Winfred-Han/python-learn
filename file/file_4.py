import os


# 向文件中追加内容
# f=open("E:/file1/追加文件.txt","a",encoding="utf-8")
with open("E:/file1/追加文件.txt", 'a',encoding="utf-8") as f:
    f.write("5555")
    f.flush()
