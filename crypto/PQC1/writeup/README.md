---
title: PQC1
description: 
author: hiikunZ
genre: crypto
solver: 0 
point: 0
---

# PQC1

## 問題文
今度は秘密鍵を最初の 128 バイトしかあげません!
## 難易度
medium
## 解法

まずは秘密鍵の中身を確認する方法を示します。以下のコマンドで確認できます。
```sh
openssl pkey -in priv-ml-kem-768.pem -text -noout
```
このコマンドの結果と秘密鍵の base64 decode 結果を比較すると、秘密鍵の最初の 128 バイト分に seed の前半半分 + α のデータが含まれていることがわかります。これを使って秘密鍵を復元できないでしょうか。

[Module-Lattice-Based Key-Encapsulation Mechanism Standard の仕様](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf) の「6.1 Internal Key Generation」を読むと、seed の後半部分(z)は implicit rejection のための乱数で、K-PKE.KeyGen() の中では使われていません。つまり、(この問題を解く上では) z の部分はどんな値でも暗号に影響を与えません。

例えば次のコマンドを用いることで、生成時に用いる乱数を指定して鍵を生成できるので、あとは PQC0 と同様にこの問題を解くことができました。
```sh
openssl genpkey -algorithm ML-KEM-768 -out priv-ml-kem-768.pem -pkeyopt hexseed:(16 進数の seed)
```

```python
# REQUIRED: OpenSSL 3.5.0

import base64
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


# base64 part of private_key[:128]
key = "MIIJvgIBADALBglghkgBZQMEBAIEggmqMIIJpgRAaa2HTyQm2vmmDmw5eheMJp6gJm3scrIloNZZF2eKncQZfPyppNNNOwAV3WY"

key = base64.b64decode(key + "A" * (-len(key) % 4)) # add padding to avoid decoding error

seed_d = key[30 : 30 + 32]

print("seed(d):", seed_d.hex())

# generate key
os.system(
    "openssl genpkey -algorithm ML-KEM-768 -out priv-ml-kem-768.pem -pkeyopt hexseed:"
    + seed_d.hex()
    + "0" * 64  # seed(z) is "0" * 64 in this script, but it can be any value
)

ciphertext = bytes.fromhex("73e322ebc019d4c299e4e270b66d27c96e3cef69834d7fde38c6d7d2f3c3cedeb94f3414b4023e65924b498dc5a314c46390270387001282774702af9482220b92560caa7e304fc499257acefafa860bdd0522239ce7df3b0ecf04fa4dca2697788e2f733576fa1015c7927d6f7a765970e97203fd48a17bf56ba86d23e234100f74092b3a2c8c1a88444a5454174b526121bc1dceeea1d8a1fb2e2b5f88ead8ea03af10d95fe34e6277678b6b907007f256bb12614699109139be3d72ce94b143a3f61cc35fee36b70893153e28b21002df4835af9aff43c36b873a430b049db97b75cea1628984e8dc912e511d9a358621e6d0f9762df7301b6e22d9237deedc1a72a0068ae84d9446827daf59e8e8728e0c46d149a2d4c4fdb67bfe8e39d7acbdc384f560f7f2ea253b350e80124098fc923e5bf9fc5d385858f4ecbb46130e55a2ff704b2d7b69e5d9b3f9fd3c0ef5bf9a7e17e095206de6d8254fae8f5cb5ac1f8fef51a23a65a33ca91d027e2977931f6716320a0f6ad6962a162c456ef9482ea6f59bff0ea264efc1072d9edfb6536b2a7aa67cb618512048fff844e6c82d02fc3e3bcd6896e1e35ab8e47e9abf4de6900850fad7732c4f56553698ce7cfdaa01aa1cae2fc88ca0043c94d22a5c42f1893816571e82d6a3b66b8f835f811a085381388cfe5c36428eaae7a4e664bb0c4c00e0387d9e74f5041c37b349c976e169c9703d4d3c6eea3d26cd43eb38e0661cbd8687056820cb320df5421d5268c2e9645f0492033c713256bdd5e79cebd3efab8c859426bb6989c70aa0639d583c370446a1271c32abd9079e0aa88ede2b158261db39ae5d2d189fced9406a9dc5329a8b959bdd4e245ea1f8be2d5516cbd5777b64e09bd69ba07997e1a72fdb03ba2620a1c90d7a654eff545c49a8196e0ab93218d6cfb36b1cd0125900e26dd6688aa400d3d7684182a6011217469795a381b5bb7fbc805b28acd097a149649cb601ed571d529a9a8d45d3ab4d41e3e3d8e136d3b7fb1d571c44b4848e5b56dee14b0f431a5c4f417af6790f3b6df281974c4f9340b90e3f1880ee9c719ea1b7bd12356045f9ce25cbd24769aa1acabfee8d7c8e57f0d876f45ebefa5871bc0c10e0e706a7703ed856f3da904edf3a6d472321844b681d5f0c98a4b0e178eb6096d36ce90334d6df6f4ed877852a6f45ade4eeadf72cccdcf342eccd8d1b2322b83047fd256e7a7152802efc4577e3a90c714a7b2af352efe9111c149c8fbaa71bca6d515ec4e9529b5a55d9309378e0698c7c33e85e3425bfda177ec1aa1d81e402ce54405700dc7df9d4688cfa98e53657f7e4c8db52bec306a7e07b73fc26ce4a48888e65c80a4af8ec8251abbbd5521f0b098e5a8f43112fe9d96feeb51bcbedc19dd38d0f4def5be292411a5668d329bb0b74cc6a8526291421b9490bf29dcdc8f0072c7391434cf30f29c007c38f3ef31ffe774f4d9460bd743e4ce65b0617aa52a30914e733257f4b6a80e1f6aff06c342f8dd30532621db7df")
encrypted_flag = bytes.fromhex("fd302c76946654e6e469a4656b90a8d60fb3492ed8c2238350e8e833a35b3587")

with open("ciphertext.dat", "wb") as f:
    f.write(ciphertext)

# generate shared secret
os.system("openssl pkeyutl -decap -inkey priv-ml-kem-768.pem -secret shared.dat -in ciphertext.dat")

with open("shared.dat", "rb") as f:
    shared_secret = f.read()

flag = unpad(AES.new(shared_secret, AES.MODE_ECB).decrypt(encrypted_flag), 16)
print(flag.decode())
```