import string

alphabet = string.ascii_lowercase + '?'

l = int(input())
h = int(input())
t = input().lower()
ascii_art = [input() for i in range(h)]

for i in range(h):
    row = ''
    for letr in t:
        if letr not in alphabet : letr = '?'
        idx = alphabet.index(letr)
        row += ascii_art[i][(idx*l):(idx*l+l)]
    print(row)
