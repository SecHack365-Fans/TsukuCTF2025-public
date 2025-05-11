---
title: destroyed
description: 
author: xryuseix
genre: osint
solver: 0 
point: 0
---

# destroyed

## 問題文
[このTelegramの投稿](https://t.me/etozp/19319)の写真に写っている学校を特定してください。
フラグフォーマットは、その場所の座標の小数点第4位を四捨五入して、小数第3位までを
`TsukuCTF25{緯度_経度}`の形式で記載してください(例: `TsukuCTF25{12.345_123.456}`)。
注意: この問題を解く過程で、戦争に関わる直接的な画像が表示される場合があります。

## 難易度

- Medium

## 解法

こちらは作問ミスがあり、運営が用意していた解答が間違っていました。ご迷惑をおかけいたしました。

Web上に[様々な方のWriteup](https://www.google.com/search?q=%22TsukuCTF%22+%222025%22+%22destroyed%22)が掲載されているため、そちらを参考にしてください。

`TsukuCTF25{47.806_35.357}`

## 用意していた嘘解法

「Eyes on Russia Map」を使う方法が最も簡単だと思います。

https://eyesonrussia.org

Telegramの投稿の投稿日が2022/12/24であるため、以下の条件でフィルタリングします。

- 日付: 2022/12/24-2022/12/25
- フリーワード: `school`

検索結果として、1件がヒットしました。
https://eyesonrussia.org/?query=school&chosenOption=null%2Cnull%2Cnull&categories=&sectorAffected=&dateRange=1671807600000%2C1671894000000&onlyEventsMapFrame=false

その検索結果の詳細を閲覧すると、座標が記載されています。

https://eyesonrussia.org/event/UW22407

`TsukuCTF25{47.798_35.304}`
