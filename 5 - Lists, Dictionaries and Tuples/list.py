list = ['Hi', 'How are you', 'good', 'and you']
list1 = ['123', '234']
nums = [43, 12, 54, 1, 42]
# print(list)

# ---- length of list ----
# print(len(list))

# ---- specific value on index 0 ----
# print(list[0])

# ---- specific value on index -1 (last one) ----
# print(list[-1])

# ---- get values from index 0 to 3 ----
# print(list[0:3])

# ---- get values from start of the list to index 2 ----
# print(list[:2])

# ---- get values from 2 index to the end of the list ----
# print(list[2:])

# ---- append the value "oouch" to last index in the list ----
# list.append("oouch")
# print(list)

# ---- insert value in 1 index ----
# list.insert(1, "Home")
# print(list)

# ---- add intire list1 in specific index to list ----

# list.insert(2, list1)

# print(list)
# print(list[2])

# ---- add values of list1 to list ----
# list.extend(list1)
# print(list)

# ---- append intire list1 to last index in the list ----
# list.append(list1)
# print(list)

# ---- remove items from list ----
# list.remove("Hi")
# print(list)

# ---- remove last value in the list ----
# popped = list.pop()
# print(list)
# print(popped)

# ---- reverse the list ----
# list.reverse()
# print(list)

# ---- sort the list ----
# list.sort()
# print(list)

# sorted_list = sorted(list)

# ---- sort and reverse the values ----

# nums.sort(reverse=True)
# print(nums)

# ---- max number in the list ----
# print(max(nums))

# ---- min number in the list ----
# print(min(nums))

# ---- sum number in the list ----
# print(sum(nums))

# ---- get index of the value ----
# print(list.index('Hi'))
# print(list.index('wfsvarg'))  # ValueError: 'wfsvarg' is not in list
# print("Hi" in list)  # True
# print("wfsvarg" in list)  # False

# ---- Get every value from the list ----
# for item in list:
#     print(item)


# ---- Get every value and index from the list, the index start from 2 ----
# for index, item in enumerate(list, start=2):
#     print(index, item)

# ---- Chenge the space between values in the list ----
# list_str = ' - '.join(list)
# print(list_str)

# ---- return back to list ----
# new_list = list_str.split(" - ")
# print(new_list)

# ---- list_new_2 equal to list_new_1 ----
# list_new_1 = ['Hi', 'How are you', 'good', 'and you']
# list_new_2 = list_new_1

# print(list_new_1)
# print(list_new_2)

# # ---- if we change value in list_new_1, its changes in list_new_2 also ----
# list_new_1[0] = "Sleep"

# print(list_new_1)
# print(list_new_2)

# ---- tuple_2 equal to tuple_1 ----
tuple_1 = ('Hi', 'How are you', 'good', 'and you')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# # ---- if we change value in tuple_1, we will get error ----
tuple_1[0] = "Sleep"

print(tuple_1)  # 'tuple' object does not support item assignment
print(tuple_2)
