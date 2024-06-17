a=[]
type(a)#list

list_num=[1, 2, 3]
print(list_num)#[1, 2, 3]

list_char=['a', 'b', 'c']
print(list_char)#['a', 'b', 'c']

list_complex=[1, 'a', 2]
print(list_complex)#[1, 'a', 2]

list_nest=[1, 2, ['a', 'b']]
print(list_nest)#[1, 2, ['a', 'b']]



var=[1, 2, ['a', 'b', 'c']]
print(var[0])#1

print(var[2])#['a', 'b', 'c']

print(var[2][0])#a

var_list=[1, 2, 3, 4, 5]
print(var_list[0:2])#[1, 2]

a=[1, 2, 3]
b=[4, 5, 6]

print(a+b)#[1, 2, 3, 4, 5, 6]

print(a*3)#[1, 2, 3, 1, 2, 3, 1, 2, 3]

c=[1, 2, 3]
c.append(4)
print(c)#[1, 2, 3, 4]

d=[1, 2, 3]
d.append([4, 5])
print(d)#[1, 2, 3, [4, 5]]

e=[1, 2, 3]
e.extend([4, 5])
print(e)#[1, 2, 3, 4, 5]

var1=[1, 2, 3, 4, 5]
var1[2]=10
print(var1)#[1, 2, 10, 4, 5]

var1[3]=['a', 'b', 'c']
print(var1)#[1, 2, 10, ['a', 'b', 'c'], 5]

var1[0:2]=['가', '나']
print(var1)#['가', '나', 10, ['a', 'b', 'c'], 5]

var2=[1, 2, 3]
del var2[0]
print(var2)#[2, 3]

var3=[1, 2, 3]
var3[0:1]=[]
print(var3)#[2, 3]

var4=[1, 2, 3, 1, 2, 3]
var4.remove(1)
print(var4)#[2, 3, 1, 2, 3]

var5=[1, 2, 3]
var5.pop()#[1, 2]
print(var5)

var6=[2, 4, 1, 3]
var6.sort()
print(var6)#[1, 2, 3, 4]

