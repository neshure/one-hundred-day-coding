"""
A variable is only available from inside the region it is created. This is called scope.

"""

# Example I
# A variable created inside a function is available inside that function:
# def myfunc():
#   x = 300
#   print(x)

# myfunc()


# Example II:

# A local variable can be accessed from a function within the function:
# def myfunc():
#   x = 300
#   def myinnerfunc():
#     print(x)
#   myinnerfunc()

# myfunc()

'''
Global Scope
A variable created in the main body of the Python code is a global variable and belongs to the global scope.

Global variables are available from within any scope, global and local.

Example
A variable created outside of a function is global and can be used by anyone:

x = 300

def myfunc():
  print(x)

myfunc()

print(x)
'''

'''
use the global keyword if you want to make a change to a global variable inside a function.

Example
To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)

'''

