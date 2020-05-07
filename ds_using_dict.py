ab = {  'Swaroop'   : 'swaroop@swaroopch.com',
        'Larry'     : 'larry@wall.org',
        'Matsumoto' : 'matz@ruby-lang.org',
        'Spammer'   : 'spammer@hotmail.com'
     }

print('swaroop address is',ab['Swaroop'])

del ab['Spammer']

print('\n There are {} contacts in the address book\n'.format(len(ab)))

for name,address in ab.items():
    print('Contact {} at {}'.format(name,address))

ab['Vinay'] = 'Vinay@ab.com'
if 'Vinay' in ab:
    print('\n Vinay Address is ',ab['Vinay'])
