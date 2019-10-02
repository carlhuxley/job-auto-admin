# def decorator_function(original_function):
#     def wrapper_function(*args, **kwargs):
#         print('wrapper executed this before {}'.format(original_function.__name__))
#         return original_function(*args, **kwargs)
#     return wrapper_function


# #@decorator_function
# def display():
#     print('Display function ran!')


# @decorator_function
# def display_info(name, age):
#     print('display_info has two arguments {}, {}'.format(name, age))


# #display()

# #display_info('John', 25)

# display = decorator_function(display)

# display()

def my_timer(orig_func):
    import time

    #@wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper


import time


@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Tom', 67)