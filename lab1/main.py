from HashTable import HashTable
from data_gen import TxtGenerator

table = HashTable()
gen = TxtGenerator()
#gen.generate(20000)
with open('test_data.txt', 'r') as file:
    read_data = file.read().split(';')

for word in read_data:
    table.add(word)

print(table.find('qjCNtJ'))
print(table.find('4S9n'))
print(table.find('zasf'))

print(table.avg_collisions())
print(table.avg_comp())