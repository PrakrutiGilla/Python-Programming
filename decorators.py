#decorators sre used to add extra features/conditions to the existing function without touching it.
#We do this by defining a new function and passing existing function as argument

#here div() - existing function, s_div() - new function

# here we are performing division. we want a to be always greater than b.
#but div doesn't have that condition. so we created s_div.
#in this, we created another func inner(div parameters) to use div() parameters, made changes/ applied condition
#then called div() with changed parameters.

def div(a,b):
    print(a/b)

def s_div(func):

 def inner(a,b):
    if(a<b):
        a,b=b,a

    return func(a,b) #div() changed parameters
 return inner 

d=s_div(div)#passing div() to s_div()
d(2,4)
    
