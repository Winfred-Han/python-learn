

def func_c():
    print("---3---")
def func_b():
    print("---2---")
    func_c()
def func_a():
    print("---1---")
    func_b()
func_a()