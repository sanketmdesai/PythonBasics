print("entering main")

i=0

print("Printing for loop")
for i in range(1,10):
    print("i=",i)

print("printing odd number using steps in for loop")
for  i in range(1,10,2):
    print("i=",i)

print("printing multiples of 4 using step size of 4")
for i in range(0,41,4):
    print(i)

print("printing descding order of number ... using negative step size")
for i in range(10,1 , -1):
    print(i)
print("leaving main")
