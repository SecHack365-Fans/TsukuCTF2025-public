# easy_kernel

## Description
If you're new to kernel challenges, check out [this guide](https://pawnyable.cafe/linux-kernel/).
You can download the handouts from [here](https://drive.google.com/file/d/1dxELzSknpJ6MsAZhnPXw1_8M-_DHMJsL/view?usp=sharing).
The flag is in /dev/sdb. Good luck and have fun!

## Difficulty
medium

## Flag

TsukuCTF25{n0w_u_learned_h0w_to_turn_UAF_int0_r00t}

## Points
- Initial: `500`
- Last: `497` (solved: `12`)

## Writeup
Use `struct seq_operations` to control RIP and ret2user. See [this article](https://r1ru.github.io/posts/7/) for more details.

## Author
r1ru
