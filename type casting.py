#converting one data type to another data type
"aman"
print(int(123.678))
#123

print(int(True))
#1

print(int(0x1010))
#4112

#bytes data type(0-256) only between (immutable)
x=[10,20,30,40,50]
b=bytes(x)
for i in b:
    print(i)
#10
#20
#30
#40
#50

#bytes array (mutable)
x=[20,30,40,50]
a=bytearray(x)
for i in a:
    print(i)