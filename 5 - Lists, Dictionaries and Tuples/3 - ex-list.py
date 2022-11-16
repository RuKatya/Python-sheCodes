# https://pynative.com/python-list-exercise-with-solutions/

# ---- 1 ----
# list1 = [100, 200, 300, 400, 500]  # output [500, 400, 300, 200, 100]
# list1.reverse()
# print(list1)

# ---- 6 ----
# output ["Mike", "Emma", "Kelly", "Brad"]
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# res = list(filter(None, list1))
# print(res)

# ---- 7 ----
# output [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# list1[2][2].insert(2, 7000)
# list1[2][2].append(7000)
# print(list1)

# ---- 8 ----
# output ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sub_list = ["h", "i", "j"]

# list1[2][1][2].extend(sub_list)

# print(list1)
# ---- 9 ----
list1 = [5, 10, 15, 20, 25, 50, 20]  # output [5, 10, 15, 200, 25, 50, 20]
# get the first occurrence index
index = list1.index(20)

# update item present at location
list1[index] = 200
# #### or
list1[3] = 200

print(list1)
