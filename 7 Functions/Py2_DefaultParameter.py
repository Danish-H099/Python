# Default Parameter is used when we don't pass any arguments to the function 

def greet(name="Stranger"):
    print("Good Morning!",name)
    return

greet("Dash") #op-> Good Morning! Dash
greet() #op-> Good Morning! Stranger