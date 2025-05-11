---
title: hidden_wpath
description:
author: xryuseix
genre: osint
solver: 0
point: 0
---

# hidden_wpath

## 問題文

新しいブログサイトを作成したので、ぜひ見に来てください！
ちなみに隠されたページがあり、そこにフラグがあります 😎

注意点: ツールの使用は許可されていますが、短期間で大量にリクエストを送信しないでください。隠されたページのリンクは 100 文字以上あり、かつ推測不可能です。

## 難易度

Hard

## 解法

1. [WPScan](https://github.com/wpscanteam/wpscan)を用いてページの情報を色々取得します。`--throttle 1000`をつけてリクエスト間に遅延を挟んでいただけると助かります。
   1. `wpscan --url http://challs.tsukuctf.org:9000/ --throttle 1000`
2. すると、デバッグログが露出していることがわかります。
   1. `[+] Debug Log found: http://challs.tsukuctf.org:9000/wp-content/debug.log`
3. デバッグログを開くと、[`404-solution`](https://github.com/aaron13100/404solution)というプラグインが使われていることがわかる
   1. `Translation loading for the <code>404-solution</code> domain was triggered too early.`
4. WPScan の公式サイトから、`404-solution`の脆弱性を調べます。
   1. [https://wpscan.com/plugins/?page=4&get](https://wpscan.com/plugins/?page=4&get)にアクセス
   2. すると、[これ](https://wpscan.com/vulnerability/1dcd384c-21d1-4fa1-90d8-5ad35425cf92/)が見つかります。
5. 公式レポジトリから[修正コミット](https://github.com/aaron13100/404solution/commit/036b8a8d42a5af7387476febe2a9e443219aeb4b)を探します。
   1. デバッグログが露出している時、プラグインなどの設定も露出しているらしいです。
   2. `includes/SynchronizationUtils.php`の[`uniqidReal()`関数](https://github.com/aaron13100/404solution/blob/036b8a8d42a5af7387476febe2a9e443219aeb4b/includes/SynchronizationUtils.php#L265)と`includes/Logging.php`の[`getDebugFilePath`関数](https://github.com/aaron13100/404solution/blob/036b8a8d42a5af7387476febe2a9e443219aeb4b/includes/Logging.php#L342)がこれの修正になります。
   3. `404-solution.php`の[`abj404_getUploadsDir`関数](https://github.com/aaron13100/404solution/blob/036b8a8d42a5af7387476febe2a9e443219aeb4b/404-solution.php#L164)と組み合わせて、デバッグログは`/temp_abj404_solution/abj404_debug.txt`に保存されるということがわかります。
   4. ただし、WordPress のアップロード用ディレクトリは`/wp-content/uploads/`なので、最終的に`/wp-content/uploads/temp_abj404_solution/abj404_debug.txt`に保存されます。
   5. よって、以下の URL にアクセスします。
      1. [`http://challs.tsukuctf.org:9000/wp-content/uploads/temp_abj404_solution/abj404_debug.txt`](http://challs.tsukuctf.org:9000/wp-content/uploads/temp_abj404_solution/abj404_debug.txt)
      2. なお、ログが多い場合は以下のファイルに保存されます。[`http://challs.tsukuctf.org:9000/wp-content/uploads/temp_abj404_solution/abj404_debug.txt_old.txt`](http://challs.tsukuctf.org:9000/wp-content/uploads/temp_abj404_solution/abj404_debug.txt_old.txt)
6. デバッグログに秘密のページへのアクセスログが残っています。
   秘密のページは[Google Docs](https://docs.google.com/document/d/16K84AlbPOBsGpP14qfpOxBQVlc4J5-Aq4QhbVf6OYlg/edit?usp=sharing)へリダイレクトする設定になっています。

`TsukuCTF25{b3_c4r3fu1_w17h_w0rd9r355_91u61n5}`
