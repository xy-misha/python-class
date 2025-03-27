def greet(name):
    """ 
    this fuunction  greets the person
    using name as a parameter
    """
    print ("hello " , name, "! how are you")
greet("paula")
greet("gew")
greet("alice")
print(greet.__doc__)

# a simple program for addin two num given in paramaters
def add(a,b=0 ):
    """
    simple function for adding two parameters
    passes as two arguments
    returns the sum
    """
    return (a+b)

print(add(2))