import struct


def shifre(string): 
    list = []
    for i in string:
        print(bin(ord(i)))
        list.append(bin(ord(i))[2:])
    # print(i, bin(i))
    # byte = struct.pack('b', i)
    # print(byte:08b)
    return ' '.join(list)

print(shifre('я тебя люблю'))