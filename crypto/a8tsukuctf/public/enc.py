import string

plaintext = '[REDACTED]'
key = '[REDACTED]'

#    <plaintext>               <ciphertext>
# ...?? tsukuctf, ??... ->  ...aa tsukuctf, hj...
assert plaintext[30:38] == 'tsukuctf'


# https://ja.wikipedia.org/wiki/%E3%83%B4%E3%82%A3%E3%82%B8%E3%83%A5%E3%83%8D%E3%83%AB%E6%9A%97%E5%8F%B7#%E6%95%B0%E5%BC%8F%E3%81%A7%E3%81%BF%E3%82%8B%E6%9A%97%E5%8F%B7%E5%8C%96%E3%81%A8%E5%BE%A9%E5%8F%B7
def f(p, k):
    p = ord(p) - ord('a')
    k = ord(k) - ord('a')
    ret = (p + k) % 26
    return chr(ord('a') + ret)


def encrypt(plaintext, key):
    assert len(key) <= len(plaintext)

    idx = 0
    ciphertext = []
    cipher_without_symbols = []

    for c in plaintext:
        if c in string.ascii_lowercase:
            if idx < len(key):
                k = key[idx]
            else:
                k = cipher_without_symbols[idx-len(key)]
            cipher_without_symbols.append(f(c, k))
            ciphertext.append(f(c, k))
            idx += 1          
        else:
            ciphertext.append(c)

    ciphertext = ''.join(c for c in ciphertext)

    return ciphertext


ciphertext = encrypt(plaintext=plaintext, key=key)

with open('output.txt', 'w') as f:
    f.write(f'{ciphertext=}\n')
