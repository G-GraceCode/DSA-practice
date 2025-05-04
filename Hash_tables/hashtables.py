#Hash Tables: hASH fUNCTIONS, SET, & MAP
#what are hashable / Immutable: strings, integers, tuples || not hashable / mutable; Arrays, dictionary


# hash set: help to store data with unique value.
#time: o(1)

s = set()
#add into hashtable
s.add(3)
s.add(4)
s.add(5)
s.add(6)
s.add("tandu")

print(s)
#remove from the set
if s:
    s.remove(3)
print(s)

# Lookup a particular value
if 4 in s:
   print(True)

#set construction -> o(s)
names="Tandu yanmick"
result = set(names)
result.remove(" ")
print(result)

#Looping over set, it has time: o(n)
for x in s:
    print(x)

#Hashmap: Helps in storing date with a unique values., 
#Has_map - Dictionary
fruits = {
    "mango": 4,
    "peer": 1,
    "banana": 3,
}
if "mango" in fruits:
    print(True)

# looping over a dic - o(n)

for key, val in fruits.items():
    print(f"key: {key} value: {val}")

#Handle Collision in hash_table