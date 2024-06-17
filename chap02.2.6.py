set1=set([1, 2, 3])
print(set1)#{1, 2, 3}

set2=set('banana')
print(set2)#{'b', 'n', 'a'}

s1=set([1, 2, 3, 4])
s2=set([3, 4, 5, 6])
print(s1.union(s2))#{1, 2, 3, 4, 5, 6}
print(s1.intersection(s2))#{3, 4}
print(s1.difference(s2))#{1, 2}