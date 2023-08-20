print("Hello world")

a=4
def func():
    """  
    Trial function
    """
    a=5
    print(a)
func()
print(a)    

print("Funtion " + func.__doc__)