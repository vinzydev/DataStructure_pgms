shoplist = ['dal', 'pepper', 'mango', 'jeerge']

print('I have',len(shoplist),' items to shop today')

print('Those items are',)
for item in shoplist:
    print(item,'\b')

shoplist.append('bun')

print("Latest list is",shoplist)
shoplist.sort()
print('lets sort',shoplist)

print('Lets buy',shoplist[1])
olditem=shoplist[1]
del shoplist[1]
print('I bought',olditem)
print('This is current list',shoplist)

