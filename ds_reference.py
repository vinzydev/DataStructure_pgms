print('Simpple refrence example')

shoplist=['apple','banana','orange']

mylist = shoplist

del shoplist[0]

print('Shoplist is',shoplist)
print('mylist is',mylist)

mylist=shoplist[:]
del mylist[1]

print('Shoplist is',shoplist)
print('mylist is',mylist)
