#!/data/data/com.termux/files/usr/bin/bash
pkg update && pkg upgrade -y
pkg install python2 nano
echo ""
echo -n -e """silahkan edit username dan password nya !!!
\t\tPERHATIAN !!!

Dilarang mengubah code tanpa ijin
jika sudah mengerti silahkan lanjut"""
echo ""
sleep 5
mkdir /data/data/com.termux/files/home/.terlogin
mv bin/login.py /data/data/com.termux/files/home/.terlogin
echo 'python2 /data/data/com.termux/files/home/.terlogin/login.py' >> /data/data/com.termux/files/usr/etc/bash.bashrc
nano /data/data/com.termux/files/home/.terlogin/login.py

echo ""
echo -e "\n## Thanks For Using Terlogin ##"
echo -e "silahkan mulai ulang termux\n"
echo ""
sleep 10
