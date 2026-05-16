a = 'a0b0c0df0'

res = []
chars = []
for char in a:
    print(char)
    if char.isalpha():
        res.append(char)
    else:
        chars.append(char)
print(res, chars)

b = ("".join(res))
c = (''.join(chars))
print(b+c)