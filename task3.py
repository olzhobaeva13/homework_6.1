from functools import reduce

numbers = [4, 17, 3, 90, 28, 55]

reduced_nums = reduce(lambda x, y: x*y, numbers)
#TODO что за 3 аргумент
print(reduced_nums)