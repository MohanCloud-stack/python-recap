def new_decorator(original_func):
    def wrap_func():
        print("Some extra Code, Before the original Function!!!")
        original_func()
        print("Some extra Code,After the original Function!!!")
    return wrap_func
@new_decorator
def func_needs_decorator():
    print("I want to be decorated!!!")
func_needs_decorator()