print(" my first print statement")
 # varibale 
a=5
b=7
print(a)
print(" ARITHEMATIC OPERATIONS")
#arthematic operations
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)

# booleans 
print(" BOOLEAN")
c=5
d=3
print(c<d)
print(c>d)
print(c>=d)
print(c<=d)
print(c==d)
print(c!=d)
print(" LOGICAL OPERATORS")
#logical operators (AND OR NOT)

print(c<d and c>d and c==d and c>=d)
print(c<d or c>d or c==d or c>=d)#AOR ME 99% FALSE 1 TRUE RESULT TRUE 
print(not(c<d and c>d and c==d and c>=d))#AND ME 99% TRUE 1 FALSE RESULT FALSE 
print(not(c<d or c>d or c==d or c>=d))
print("******************IF STATEMENT **************************")
x=67
y=4
if x>=y:
    print("x is greater than y")
else:
    print("y is less than x")

print("******************NESTED IF STATEMENT **************************")
evennumber=20
oddnumber=33

if evennumber==20:
  if oddnumber==33:
    print("logic is true")
  else:
     print("logic is not true")