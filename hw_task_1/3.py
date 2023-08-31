def myAppend(list, item):
    return list + [item]

list = [1, 2, 'cat']
item = 3
new_list = myAppend(list, item)
[print(str(i)) for i in new_list]