from unittest import result

### Task 1.1. 
# Write a Python program to calculate the length of a string without using the `len` function.
def calculate_lenght_of_string(string):
    n = 0
    for _ in string:
        n+=1
    return n

### Task 1.2.
#  Write a Python program to count the number of characters (character frequency) in a string 
# (ignore case of letters).
def character_frequency(string):
    string = string.lower()
    # Делаем множество из строки, тем самым получая уникальные элементы в ней.
    # Далее для каждого уникально элемента (i) проверяем их количество в исходной строке.
    # Формируем словарь {<уникальный символ>:<количество>}
    res = {i : string.count(i) for i in set(string)}
    return res

### Task 1.3
# Write a Python program that accepts a comma separated sequence of words as input 
# and prints the unique words in sorted form.
def sorting_unique_words(item):
    res = list(set(item))
    res.sort()
    return res

### Task 1.3
# Create a program that asks the user for a number and then prints out a list of all the [divisors]
# (https://en.wikipedia.org/wiki/Divisor) of that number.
def divisor(num):
    res = []
    for i in range(1,num+1):
        if num % i == 0:
            res.append(i)
    return res

### Task 1.4
# Write a Python program to sort a dictionary by key.
def sort_dict_by_key(dictionary):
    # Вывести отсортрованный словарь невозможно, потому что он не несет за собой какую-либо упорядоченность
    # (неупорядоченная коллекция)
    # Вывод будет осуществляться следующим образом: [(),()], т.е. список с вложенными кортежами.
    res = sorted(dictionary.items())
    return res
 
### Task 1.5
# Write a Python program to print all unique values of all dictionaries in a list.
def unique_values_of_dict(dictionary):
    res = []
    for i in dictionary:
        for j in i.values():
            res.append(j)
    res = list(set(res))
    return res

### Task 1.6
# Write a Python program to convert a given tuple of positive integers into an integer. 
def convert_tuple(item):
    result = ""
    for i in item:
        result += str(i)
    return int(result)

### Task 1.7
# Write a program which makes a pretty print of a part of the multiplication table.
def pretty_multiplication_table(a,b,c,d):
    x = [i+c for i in range(d-c+1)]
    y = [i+a for i in range(b-a+1)]
    x.insert(0,1)
    y.insert(0,1)
    table = [[ i * j for j in x] for i in y]
    table[0][0] = ''
    return  table

def print_pretty_multiplication_table(table):
    for i in table:
        for j in i:
            print(j, end=' ')
        print()

  