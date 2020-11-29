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

a = int(input("Enter The First Number"))
b = int(input("Enter The Second Number"))


print(f" Sum Of Two Numbers is {add(a,b)}")
print(f" Sub Of Two Numbers is {sub(a,b)}")
print(f" Multiplication Of Two Numbers is {mul(a,b)}")
print(f" Division Of Two Numbers is {div(a,b)}")
print(f" Modulus of Two Numbers is {mod(a,b)}")
print(f" Cube Of  Number is {cube(a)}")
