---
title: xortsukushift
description: 
author: mmrz
genre: crypto
solver: 0 
point: 0
---

# XorTsukuShift

## 問題文

つくし君とじゃんけんしよう。負けてもチャンスはいっぱいあるよ！
フラグフォーマットは `TsukuCTF25{}` です。

## 難易度

medium

## 解法

``xortsukushift()`` % 3 を乱数としたじゃんけんに、 294 回連続で勝つ必要があるじゃんけん。ただし、300 ラウンド失敗しても良い。
この xorshift を手元で実験すると、どのようなシード値でも周期が 280 しかないことが分かる。

事前に 280 回分のじゃんけんをしておくことで、その後の手を把握することができるので、後は連勝するのみ。

``TsukuCTF25{4_xor5h1ft_15_only_45_good_45_1t5_5h1ft_p4r4m3t3r5}``

```python
from pwn import *

r = remote("challs.tsukuctf.org", 30057)

X = []

r.recvline()
r.recvline()

# 乱数の周期を記録する
for i in range(280):
    for _ in range(2):
        r.recvline()
    
    r.recvuntil("Rock, Paper, Scissors... Go! (Rock: 0, Paper: 1, Scissors: 2): ".encode())
    r.sendline("0".encode())
    result = r.recvline().decode().strip()

    if "win!" in result:
        X.append(0)
    elif "Draw!" in result:
        X.append(1)
    elif "lose!" in result:
        X.append(2)
    else:
        log.error(f"ERR: {result}")
        break

# 適当な値を出力してラウンドを強制終了
r.recvline()
r.recvline()
r.recvuntil("Rock, Paper, Scissors... Go! (Rock: 0, Paper: 1, Scissors: 2): ".encode())
r.sendline(b"5")

assert r.recvline().decode().strip() == "Tsukushi: Hey, you cheated!"

for i in range(294):
    for _ in range(2):
        r.recvline()

    r.recvuntil("Rock, Paper, Scissors... Go! (Rock: 0, Paper: 1, Scissors: 2): ".encode())
    r.sendline(str(X[(i+1) % 280]).encode())
    assert r.recvline().decode().strip() == "Tsukushi: You win!"

assert r.recvline().decode().strip() == "Tsukushi: You won 294 times in a row?! That's incredible!"

final_line = r.recvline().decode().strip()

print(final_line.split()[-1])

r.close()
```
