a="kingfisher is astrong beer"
print(a[0:26])
#kingfisher is strong beer

a="ram is a good boy"
print(a[0:8])
# ram is a

a="ram is a good boy"
print(a[::3])
# r  gdo

a="ram is a good boy"
print(a[-8:-1])
#good bo

a="ram is a good boy"
print(a[-1:-9:-2])
#ybdo

a="ram is a good boy"
print(a[9:-12])
# blank/empty

a="ram is a good boy"
print(a[9:-12:-1])
# g a

a="ram is a good boy"
print(a[-4:6:-1])
#doog a

a="ram is agood boy"
print(a[12:10])
# blank space

a="ram is agood boy"
print(a[-22:5:3])
#r

s="rangerover is a beast"
a=s.split()
for i in a[::-1]:
    print(i,end=" ")