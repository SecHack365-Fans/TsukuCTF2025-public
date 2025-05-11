import time
from pwn import *

r = remote("localhost", 30057)

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
