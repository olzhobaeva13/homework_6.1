from functools import reduce

palindromes = ['hello', 'sentences where punctuation', 45,'Able was I, ere I saw Elba', 34.0, 78.87, 'found', 'level', '12/11/21', 'radar','stats']

palindromes_lst = list(filter(lambda x: x == x[::-1], list(map(lambda x: str(x).lower().replace(' ', '').replace(',', ''), palindromes))))

result = reduce(lambda x, y: x+y, palindromes_lst)

print(result)




