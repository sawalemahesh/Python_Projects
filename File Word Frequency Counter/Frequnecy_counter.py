'''
You are given a text file.

Task:
Count frequency of each word
Ignore case sensitivity
Remove punctuation
Print top 5 most frequent words
'''


def count_feq():
    with open('data.txt', 'r') as file:
        data = file.read()
        # print(data)
        list1 = data.split()
        # print(list1)
    freq = {}
    for char in list1:
        freq[char] = freq.get(char,0)+1

    for char in freq:
        if freq[char] <= 2:
            print(freq)
count_feq()
