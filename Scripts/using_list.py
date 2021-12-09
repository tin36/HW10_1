#spisok pokupok
shoplist = ['apple', 'mango', 'morkov', 'baban']

print('ya dolzhen sdelat', len(shoplist), 'pokupok')

print('pokupki:', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\ntakzhe nuzhno kupit risa')
shoplist.append('ris')

print('sortirovka')
shoplist.sort()
print('sortrovannyi spisok', shoplist)

print('samoe vazhnoe', shoplist[0])
oldoitem = shoplist[0]
del shoplist[0]
print('ya kupil', oldoitem, 'i teper mne ostalos kupit', shoplist)
print('i teper mne ostalos kupit', shoplist)