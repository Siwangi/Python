
"""
# Get both keys and values at the same time from 2 dict
for (k, v), (k2, v2) in zip(dict_one.items(), dict_two.items()):
    print(k, v)
    print((k2, v2))
"""
#print same key value from 2 dict

dict_one ={"key1": "value1", "key2": "value2", "key7": "value4"}
dict_two ={"key4": "value4", "key7": "value4", "key5": "value5"}

for key1 in dict_one:
    for key2 in dict_two:
        # print(key1, key2)
        if key1 == key2 and dict_one[key1] == dict_two[key2]:
         print(key1, dict_one[key1])



# for key1 in range(len(dict_one)):
#     if dict_one[key1] == dict_two[key1]:
#         print(key1, dict_one[key1])

# if dict_one.keys() == dict_two.keys():
    #     print(key)
    # print(value)

    # if dict_one.key(k) == dict_two.key(k):
    #     dict(k,v)=
    #     print(key)
    #

    #     range(len(dict_one)):
    # print(dict_one)


#     if dict_one[key, value] == dict_two[key, value]:
#         dict[key, value] = dict_one[key, value]
#         print(dict)
#
#
# >>> for (k,v), (k2,v2) in zip(d.items(), d2.items()):
#

#     dict3[dict1[x]] = dict2[x]
# print(dict3)
#     if v in some_dict.values() and v != some_dict.keys(k):
#         a_list.append(k)