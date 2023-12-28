#while loop
count = 10
while count > 0:
    print(count)
    count -= 1

#2
total = 0
num=1
while num<=10:
    total+=num
    num+=1
print("sum of numbers from1 to 10:",)

#4
n = 1
while n<=100:
    c = 0
    i = 2
    while i<=n//2:
        if n%i==1:
            c+=1
            break
        i+=1
    if c==0 and n!=1:
      print(n,end=' ')
n+=1
