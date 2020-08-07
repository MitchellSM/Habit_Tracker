string = "Hello"
out = ""
for c in string:
    if ord(c) < 97:
        out += "".join([chr(ord(c)+32)])
    else:
        out += "".join([c])
print(out)


    