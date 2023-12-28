#assighnment(program to reverse a string using split function)

s="rengerover is a beast"
r=reversed(s.split(" "))
for x in r:
    print(x,end=" ")  
print()

#program to reverse a string using split function

s="rangerover is a beast"
r=s.split()
for x in r[::-1]:
    print(x[::-1],"",end="")
print()

#program to revse a string using split function
s="rangerover is a beast"
r=s.split(" ")
for x in r[::-1]:
    print(r[::-1]," ",end="")
print()
