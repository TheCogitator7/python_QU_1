print("Hello world!")
print('Hello world!')

multiline="""Life is too short
You need python"""

print(multiline)
#Life is too short 
#You need python

a='Hello'
b=' World'
print(a+b)

c='Quant'
print(c*3)#QuantQuantQuant

name="Young"
birth='1979'
print(f'My name is {name}, my birth is {birth}.')
#My name is Young, my birth is 1979.

a='Life is too short'
len(a)#17

var='Life is too short'
print(var.replace(' ', '_'))
#Life_is_too_short

print(var.split(' '))
#['Life', 'is', 'too', 'short']

var='apple'
print(var[2])#p

print(var[-2])#l

print(var[0:3])#app

print(var[:2])#ap

print(var[3:])#le
