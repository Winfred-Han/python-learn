
def user_info(name,age,gender):
    print(f"姓名:{name},年龄：{age},性别：{gender}")
user_info("dawei",6,"男")

# 不定长，参数作为元组
def user_info(*args):
    print(f"args的参数类型：{type(args)},内容:{args}")
user_info(1,2,3,"小明","男孩")

# 参数是key value 类型是dict
def user_info(**kwargs):
    print(f"参数类型：{type(kwargs)},内容：{kwargs}")
user_info(name="小明",age=8,gender="男")