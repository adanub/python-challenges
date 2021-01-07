from functools import wraps

def prepost(*args, **kwargs):
    if 'prefix' in kwargs:
        print(kwargs['prefix'], end='')
        print(' start')

        def decorator(func):
            @wraps(func)
            def inner(x, y):
                func(x, y)
                print(kwargs['prefix'], end='')
                print(' end')
            return inner
        
        return decorator

    else:
        print(' start')
        func = args[0]

        @wraps(func)
        def inner(x, y):
            func(x, y)
            print(' end')

        return inner

#----------------------------------------------------------------
@prepost(prefix='outer')
@prepost(prefix='inner')
@prepost
def multiplication(x, y):
    print('middle')
    return x * y

multiplication(3, 4)
