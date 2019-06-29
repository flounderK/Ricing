
print("Character Sets\n")

def batch_gen(it, b):
    l = len(it)
    for i in range(0, l, b):
        yield it[i:min(i + b, l)]


for batch in batch_gen(range(0x3040, 0x30ff), 16):
    print(' '.join([chr(i) if i not in {0x3040, 0x3097, 0x3098} else
                    chr(0x25a1) for i in batch]))


