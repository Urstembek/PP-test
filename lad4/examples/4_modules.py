# What is a Module?
# Consider a module to be the same as a code library.

# A file containing a set of functions you want to include in your application.

import my_module

my_module.greeting("danchik")
a = my_module.person1["age"]
print(a)

# Re-naming a Module
# You can create an alias when you import a module, by using the as keyword:
import my_module as mx

a = mx.person1["age"]
print(a)

# Built-in Modules
# Import and use the platform module:

import platform

x = platform.system()
print(x)

# import only person

from my_module import person1

print (person1["age"])