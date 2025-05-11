---
title: a8tsukuctf
description: 
author: mmrz
genre: crypto
solver: 0 
point: 0
---

# a8tsukuctf

## 問題文

適当な KEY を作って暗号化したはずが、 ``tsukuctf`` の部分が変わらないなぁ...

## 難易度

easy

## 解法

換字式暗号で暗号化された結果を基に、平文を求める問題。

暗号化方式は KEY の長さ周期のストリーム暗号のような形をしている (一般に Autokey Cipher と呼ばれる)。

アルファベット以外を抜いた文字列を考えると

- ``tsukuctf`` は平文と暗号文で共通
- ``tsukuctf`` の直前は ``aaaaaaaa``
- ``tsukuctf`` は 0-indexed で 24 文字目から始まる文字列

であることが分かる。
ここから、 KEY の長さが 8 文字であると仮定する。

暗号化に使われている k は基本的に

``k = cipher_without_symbols[idx-len(key)]`` 

でできており、これは、 $i$ 文字目を暗号化する際は暗号文の $i-8$ 文字目が分かればよい。

```python
def inv_f(p, k):
    p = ord(p) - ord('a')
    k = ord(k) - ord('a')
    ret = (p - k) % 26
    return chr(ord('a') + ret)
```

復号は上のプログラムででき、以上の情報から平文が

``??? ?? ??joy this problem or tsukuctf, or both? the flag is concatenate the seventh word in the first sentence, the third word in the second sentence, and 'fun' with underscores.``

である事が分かる。

ここまで復元できると、 flag に必要な情報は ``tsukuctf_is_fun`` で、Rules に書かれているフラグフォーマットに従うと、 flag は ``TsukuCTF25{tsukuctf_is_fun}`` となる。
