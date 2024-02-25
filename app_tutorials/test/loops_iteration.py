   
def my_function(*args, **kwargs):
    for a in args:
        print(f"ARGS: {a}")
    
    for k in kwargs.items():
        print(f"KWARGS: key: {k}")
        
        

my_function(1,2,3,4,5,6,7,8, a=10, b=20, c=30, d='this is test')