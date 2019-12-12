# # 1
# a = [29, 36.6, 'hello', True, "world!"]
# print(a)
# print(type(a))
#
# for i in range(len(a)):
#     print(type(a[i]))
#     print(a[i])

# 2
list =[]

i = int(input('Сколько элементов вы хотите внести в список?:\n'))
for a in range(i):
    a = input('Введите элемент:\n')
    list.append(a)
print(list)
new_list = list.split(',':2)
print(new_list)