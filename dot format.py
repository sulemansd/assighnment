#.format
#input=aman is good
#output=good is aman

s="aman is good"
print("{c} {b} {a}".format(a='aman',b='is',c='good'))

#input=ABCCCDDDEFGGGHHHIIJJJKLLABCDEF
#OUTPUT=ABCDEFGHIJKL
list="ABCCCDDDEFGGGHHHIIJJJKLLABCDEF"
x=[]
y=[]
for i in list:
    if i not in x:
        x.append(i)
for i in x:
    if list.count(i)>1:
        y.append(i)
print(y)