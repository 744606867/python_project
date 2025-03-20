def  func(): 
    a = 10 
    def  inner_func():
        a = 20
        print(a)
        return a
    return inner_func

inner = func()
print(inner())