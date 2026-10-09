n = int(input())
name = []
address = []
region = []

for _ in range(n):
    name_value, address_value, region_value = input().split()
    name.append(name_value)
    address.append(address_value)
    region.append(region_value)

# Please write your code here.
class person:
    def __init__ (self, name_value, address_value, region_value):
        self.na = name_value
        self.ad = address_value
        self.ci = region_value
max_name = name[0]
max_idx = 0
for i in range(n):
    if name[i] > max_name:
        max_name = name[i]
        max_idx = i

person1 = person(name[max_idx], address[max_idx], region[max_idx])
print(f'name {person1.na}')
print(f'addr {person1.ad}')
print(f'city {person1.ci}')
