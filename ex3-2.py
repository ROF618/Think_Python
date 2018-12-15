def do_twice(f, thing):
    f(thing)
    f(thing)

def print_spam():
    return print('spam')



def print_twice(bruce):
    print(bruce)
    print(bruce)

do_twice(print_twice, 'spam')

def do_four(f, thing):
    do_twice(f, thing)
    do_twice(f, thing)

do_four(print_twice, 'win')