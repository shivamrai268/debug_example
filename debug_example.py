debug = True
def debug_print(*args):
    if debug:
        print(*args)
def add(n, m):
    debug_print(n + m)
    return (n + m)

if __name__=="__main__":
    add(3, 5)



