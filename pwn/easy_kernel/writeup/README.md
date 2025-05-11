---
title: easy_kernel
description: 
author: r1ru
genre: pwn
solver: 12
point: 497
---

# easy_kernel

## 問題文
If you're new to kernel challenges, check out [this guide](https://pawnyable.cafe/linux-kernel/).
You can download the handouts from [here](https://drive.google.com/file/d/1dxELzSknpJ6MsAZhnPXw1_8M-_DHMJsL/view?usp=sharing).
The flag is in /dev/sdb. Good luck and have fun!

## 難易度
medium

## 解法
Use `struct seq_operations` to control RIP and ret2user. See [this article](https://r1ru.github.io/posts/7/) for more details.