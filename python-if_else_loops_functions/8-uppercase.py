#!/usr/bin/python3
def uppercase(str):
    print("".format(*[c if not 'a' <= c <= 'z' else chr(ord(c)-32) for c in str]))
