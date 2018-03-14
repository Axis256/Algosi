from HashTable import HashTable

table = HashTable()
with open('test_data.txt', 'r') as file:
    read_data = file.read().split(';')

for word in read_data:
    table.add(word)

print(table.find('aaa'))
print(table.find('asdf'))
print(table.find('zasf'))
print(table.find('rifnur'))