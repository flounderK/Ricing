#!/usr/bin/python3


def batch_gen(it, b):
    l = len(it)
    for i in range(0, l, b):
        yield it[i:min(i + b, l)]


def printchars(start, stop, exclude=None, alt_exclude=0x25a1):
    exclude_list = {}
    if exclude is not None:
        exclude_list = exclude
    for batch in batch_gen(range(start, stop), 16):
        print(' '.join([chr(i) if i not in exclude_list else
                        chr(alt_exclude) for i in batch]))


if __name__ == "__main__":
    print("Character Sets\n")
    printchars(0x3040, 0x30ff, {0x3040, 0x3097, 0x3098}, 0x25a1)
    printchars(0x1f000, 0x1f8ff)
