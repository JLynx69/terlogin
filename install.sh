#!/data/data/com.termux/files/usr/bin/bash
apt update && apt update
apt install python2 nano
echo -n -e """silahkan edit username dan password nya !!!
\e[1;31m\t\tPERHATIAN !!!
\e[0m
Dilarang mengubah code tanpa ijin
jika sudah mengerti silahkan lanjut"""
sleep 5
mkdir /data/data/com.termux/files/home/.terlogin
mv bin/login.py /data/data/com.termux/files/home/.terlogin
echo 'python2 /data/data/com.termux/files/home/.terlogin/login.py' >> /data/data/com.termux/files/usr/etc/bash.bashrc
nano /data/data/com.termux/files/home/.terlogin/login.py
rm -rf terlogin
echo -e "\n## Thanks For Using Terlogin ##"
echo -e "silahkan mulai ulang termux\n"
sleep 10
