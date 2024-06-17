var=()
type(var)

var1=(1, )
print(var1)#(1,)

var2=(1, 2, ('a', 'b'))
print(var2)#(1, 2, ('a', 'b'))

var3=(1, 2)
del var3[0]#error

var4=(1, 2, 3, 4, 5)
print(var4[0])#1