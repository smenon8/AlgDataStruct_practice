#!/bin/python3

import sys


n = int(input().strip())
s = input().strip()
k = int(input().strip())

k = k%26
l = list(s)
l2 = []
asc_z = ord('z')
asc_Z = ord('Z')
for c in l:
    if c.isalpha():
        new_char_val = ord(c)+k
        if new_char_val > asc_z and c.islower():
            new_char_val -= 26
        else:
            if new_char_val > asc_Z and c.isupper():
                new_char_val -= 26
        l2.append(chr(new_char_val))        
    else:
        l2.append(c)

print("".join(l2))        