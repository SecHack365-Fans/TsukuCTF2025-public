FROM ubuntu:25.04@sha256:79efa276fdefa2ee3911db29b0608f8c0561c347ec3f4d4139980d43b168d991

ENV DEBIAN_FRONTEND nointeractive

RUN apt-get -y update --fix-missing && apt-get -y upgrade
RUN apt-get -y install qemu-system xinetd hashcash
RUN groupadd -r ctf && useradd -r -g ctf ctf

COPY init.sh /etc/init.sh
COPY ctf.xinetd /etc/xinetd.d/ctf
RUN chmod 500 /etc/init.sh
RUN chmod 400 /etc/xinetd.d/ctf
RUN chmod 1733 /tmp /var/tmp /dev/shm

WORKDIR /home/ctf

COPY bzImage .
COPY flag.txt .
COPY rootfs.ext3 .
COPY run.sh .

RUN chown -R root:ctf /home/ctf
RUN chmod 550 run.sh
RUN service xinetd restart