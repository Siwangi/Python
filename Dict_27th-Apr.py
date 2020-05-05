# Add the each values in dict(single )
"""



dict_one ={"key1": 4, "key2": 6, "key7": 8}
sum = 0
for key in dict_one:
    sum = sum + dict_one[key]
print(sum)

"""

"""
# Add the each values in dict( double)

dict_one ={"key1": 4, "key2": 6, "key7": 8}
dict_two ={"key4": 5, "key7": 9, "key5": 3}

for key1 in dict_one:
    for key2 in dict_two:
        sum =  sum + dict_two[key2]
        print(sum)
"""
# merge two dict in one
dict_one ={"key1": 4, "key2": 6, "key3": 8}
dict_two ={"key4": 5, "key5": 9, "key6": 3}

dict_one.update(dict_two)
print(dict_one)

"""

dict_one ={"key1": 4, "key2": 6, "key3": 8}
dict_two ={"key4": 5, "key5": 9, "key6": 3}
dict_three = {**dict_one, **dict_two}
for key, value in dict_three.items():
    if key in dict_one and key in dict_two:
        dict_three[key]=[value, dict_one[key]]
print(dict_three)

"""


