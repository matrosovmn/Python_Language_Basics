my_list = input("Введите через пробел элементы списка: ").split()
my_list[:-1:2], my_list[1::2] = my_list[1::2], my_list[:-1:2]
print(my_list)
