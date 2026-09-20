def timer(func):
    def wrapper(*args,**kwargs):
        print("Function is start")
        result = func(*args,**kwargs)
        print("Function is called")
        return result
    return wrapper

def repeat(n):
    def decorators(func):
        @timer
        def wrapper(*args,**kwargs):
            for i in range(0,n):
                result = func(*args, **kwargs)
                print(result)

        return  wrapper
    return decorators

@repeat(n = 5)
def say_name(name):
    return f"Hello!! {name}"

say_name("Abdul Rab Khan")