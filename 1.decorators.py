def my_decorator1(func):
    def decorated_func():
        print("ASDASD")
        func()
    return decorated_func

def my_decorator2(parm1):
    def my_decorator2_inner(func):
        def decorated_fun():
            print(parm1)
            func()
        return decorated_fun
    return my_decorator2_inner

@my_decorator1
def my_func():
    return 1234

@my_decorator2("Test Arguement")
def my_func2():
    return 4567

def main():
    my_func()
    my_func2()

if __name__ == '__main__':
    main()
