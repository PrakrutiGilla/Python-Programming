#A NameError is raised when you try to use a variable or a function name that is not valid
#The ValueError appears when a value is not the expected type.
#The TypeError object represents an error when an operation could not be performed,
#typically (but not exclusively) when a value is not of the expected type
#ZeroDivisonError occurs when denom is zero
#KeyboardInterrupt error occurs when user presses ctrl+c

try:
    x=input("write")
    print("alright")
except KeyboardInterrupt:
    print("wrong")
finally:     # this block is always executed
    print("yoyo")"""

a,b=map(int,input("enter numbers").split())
try:
    quo=a/b
    print(quo)
except ZeroDivisionError:
    print("division with zero not possible")
try:
    a,b=map(int,input("enter numbers").split())
    print(a+var)#name error
    print(a[1:7])#type error
    #if a or b given values other than int datatype value error is displayed
except ValueError:
    print("value error")
except TypeError:
    print("type error")
except NameError:
    print("name error")
except:
    print("Program Terminating..") #when no exception matches with  the prg generated exception, this block is executed


try:
    a,b=map(int,input("enter numbers").split())
    quo=a/b
    print(quo)
except ZeroDivisionError:
    print("division with zero not possible")    
else:
    print("okay")  #if there is no exception this block is executed


 
   
