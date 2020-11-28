def sub(a,b):
  return a-b

def add(a,b):
  return a+b

def mul(a,b):
  return a*b

def div(a,b):
  return a/b

def mod(a,b):
  return a%b

def cube(a):
  return a**3 

def square(a):
  return a*a

def sqrt(a):
  return  a**(0.5)

def cbrt(a):
  return a**(1/3)

a = int(input("Enter The First Number"))
b = int(input("Enter The Second Number"))


print(f" Sum Of Two Numbers is {add(a,b)}")
print(f" Sub Of Two Numbers is {sub(a,b)}")
print(f" Multiplication Of Two Numbers is {mul(a,b)}")
print(f" Division Of Two Numbers is {div(a,b)}")
print(f" Modulus of Two Numbers is {mod(a,b)}")
print(f" Cube Of  Number is {cube(a)}")
print(f" Square of The Numbers is {square(a)}")
print(f" Sqrt of The Numbers is {sqrt(a)}")
print(f" Cube Root of The Numbers is {cbrt(a)}")

