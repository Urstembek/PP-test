# Scope

def myfunc():
  x = 300
  print(x)

myfunc()


def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()


# Global scope

x = 300

def myfunc():
  print(x)

myfunc()

print(x)


# Naming Variables

x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

# Global keyword

def myfunc():
  global x
  x = 300

myfunc()

print(x)

# -----

x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)