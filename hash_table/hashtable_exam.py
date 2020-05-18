from hash_table.Hash import HashTable

ht1 = HashTable(8)
ht1.add('Dave','01044442222')
ht1.add('Andy','01015555452')
ht1.desc()

print(ht1.get('Andy'))

