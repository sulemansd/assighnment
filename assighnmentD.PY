#1
n=5
for i in range(n):
    for j in range(i,n):
      print(' ',end=' ')
    for j in range(i):
      print('*',end=' ')
    for j in range(i+1):
      print('*',end=' ')
    print()

#number pattern prgm(2)

n=5
p=5
for i in range(n):
  for j in range(i+1):
    print(p,end='')
  p-=1
  print()

#reverse triangle(3)

n=5
for i in range(n):
    for j in range(i+1):
      print(' ',end='')
    for j in range(i,n-1):
      print('*',end='')
    for j in range(i,n):
      print('*',end='')
    print()

    #square(4)
n=5
for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print()

#revers hill(5)

n=5
for i in range(n):
    for j in range (i+1):
      print(' ',end=' ')
    for j in range(i,n-1):
      print('*',end=' ')
    for j in range(i,n):
      print('*',end=' ')
    print()
      
#diamond(6)
n=5
for i in range(n-1):
    for j in range(i,n):
      print(' ',end=' ')
    for j in range(i):
      print('*',end=' ')
    for j in range(i+1):
      print('*',end=' ')
    print()

n=5
for i in range(n):
    for j in range (i+1):
      print(' ',end=' ')
    for j in range(i,n-1):
      print('*',end=' ')
    for j in range(i,n):
      print('*',end=' ')
    print()

#number pattern(7)

n=5
p=0
for i in range(n):
    for j in range(i+1):
      print(p,end=' ')
    p+=2
    print()

#number pattern(8)

n=5
for i in range(n):
    for j in range(i+1):
      if(i%2==0):
        print('1',end='')
      else:
       print('2',end='')
    print()

#number triangle(9)

n=5
p=1
for i in range(n):
   for j in range(i,n):
     print(' ',end=' ')
   for j in range(i):
     print(p,end=' ')
   for j in range(i+1):
      print(p,end=' ')
   p+=1
   print()

#reverse number triangle(10)


n=5
p=1
for i in range(n):
   for j in range(i,n):
     print(' ',end=' ')
   for j in range(i):
     print(p,end=' ')
   for j in range(i+1):
      print(p,end=' ')
   p+=1
   print()


#right sided triangle(11)


n=5
for i in range(n):
    p=1
    for j in range(i+1):
      print(p,end=' ')
      p+=1
    print()

#incresing triangle pattern(12)
n=5
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    print()

#decresing triangle pattern(13)
n=5
for i in range(n):
    for j in range(i,n):
     print('*',end=' ')
    print()

#right sided triangle(14)

n=5
for i in range(n):
    for j in range(i,n):
       print(' ',end=' ')
    for j in range(i+1):
       print('*',end=' ')
    print()

#triangle(15)
n=5
for i in range(5):
    for j in range(i+n):
        print(' ',end=' ')
    for j in range(i,n):
        print('*',end=' ')
    print()

# 1 number triangle(16)
n=5
for i in range(n):
    for j in range(i+1): 
       print('1',end=' ')
    print()

#12345 triangle(17)
n=5
p=1
for i in range(n):
    for j in range(i+1):
      print(p,end=' ')
      p+=1
    print()

#number pattern program(18)

n=5
for i in range(n):
    p=1
    for j in range(i+1):
      print(' ',end=' ')
    for j in range(i,n):
      print(p,end=' ')
      p+=1
    print()

#numbers hill triangle(19)

n=5
for i in range(n):
    p=1
    for j in range(i,n):
      print(' ',end=' ')
    for j in range(i):
      print(p,end=' ')
      p+=1
    for j in range(i+1):
      print(p,end=' ')
      p+=1
    print()

#incresing triangle(20)
n=5
for i in range(n):
    p=5
    for j in range(i+1):
      print(p,end=' ')
      p-=1
    print()

#numbers decresing triangle(21)

n=5
k=5
for i in range(i):
    p=k
    for j in range(i):
      print(' ',end=' ')
    for j in range(i,n):
      print(p,end=' ')
      p-=1
    k-=1
    print()

#pattern hill triangle(22)
n=5
for i in range(n):
    p=1
    for j in range(i,n):
      print(' ',end=' ')
    for j in range(i):
      print(p,end=' ')
      p+=1
    for j in range(i+1):
      print(p,end=' ')
      p-=1
    print()

#floyd triangle(23)
n=4
p=1
for i in range(n):
    for j in range(i+1):
      print(p,end=' ')
      p+=1
    print()

#charecter pattern(24)
n=5
for i in range(n):
    for j in range(i+1):
      print('A',end=' ')
    print()         

#emoji  right side triangle(25)
n=5
p=1
for i in range(n):
    for j in range(i+1):
      print(chr(p),end=' ')
      p=1
    print()

#char (26)
n=5
p=65
for i in range(n):
    for j in range(i+1):
        print(chr(p),end=' ')
    p+=1
    print()

#char (27)
n=5
p=69
for i in range(n):
    for j in range(i,n+1):
        print(chr(p),end=' ')
        p+=1
    print()
