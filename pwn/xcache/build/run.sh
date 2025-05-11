#!/bin/sh

LENGTH=9
STRENGTH=26
challenge=`dd bs=32 count=1 if=/dev/urandom 2>/dev/null | base64 | tr +/ _. | cut -c -$LENGTH`
echo hashcash -mb$STRENGTH $challenge

echo "hashcash token: "
read token
if [ `expr "$token" : "^[a-zA-Z0-9\_\+\.\:\/]\{52\}$"` -eq 52 ]; then
    hashcash -cdb$STRENGTH -f /tmp/hashcash.sdb -r $challenge $token 2> /dev/null
    if [ $? -eq 0 ]; then
        echo "[+] Correct"
    else
        echo "[-] Wrong"
        exit
    fi
else
    echo "[-] Invalid token"
    exit
fi

cd /home/ctf

timeout --foreground 300 qemu-system-x86_64 \
    -m 64M \
    -cpu qemu64 \
    -kernel bzImage \
    -drive file=rootfs.ext3,format=raw \
    -drive file=flag.txt,format=raw \
    -snapshot \
    -nographic \
    -monitor /dev/null \
    -no-reboot \
    -smp 1 \
    -append "root=/dev/sda rw init=/init console=ttyS0 nokaslr nopti loglevel=0 oops=panic panic=-1"
