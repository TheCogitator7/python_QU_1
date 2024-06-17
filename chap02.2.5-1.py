var={'key1' : 1, 'key2' : 2}
print(var)#{'key1' : 1, 'key2' : 2}

var2={'key1' : [1, 2, 3], 'key2' : ('a', 'b', 'c')}
print(var2)#{'key1' : [1, 2, 3], 'key2' : ('a', 'b', 'c')}

var3={'key1' : 1, 'key2' : 2, 'key3' : 3}
print(var3['key1'])#1

var4={'key1' : 1, 'key2' : 2}
var4['key3']=3
print(var4)#{'key1' : 1, 'key2' : 2, 'key3' : 3}

del var4['key1']
print(var4)#{'key2' : 2, 'key3' : 3}

var5={'key1' : 1, 'key2' : 2, 'key3' : 3}
print(var5.keys())#dict_keys(['keys1', 'keys2', 'keys3'])
print(list(var5.keys()))#['keys1', 'keys2', 'keys3']
print(var5.values())#dict_values([1, 2, 3])

