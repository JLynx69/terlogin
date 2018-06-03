#termux login

password = 'password'



# ganti 'password' jadi 'sesuka' mu
# change 'password' to 'whatever'



# Tekan ctrl+x jika sudah di ubah
# atau vol-down + x



# JANGAN UBAH CODE DI BAWAH !!!

import os, sys
import getpass

def restart():
	ngulang = sys.executable
	os.execl(ngulang, ngulang, *sys.argv)

def main():
	pwd = getpass.getpass("\033[1;34mInsert Password \033[0m: ")

	if pwd == password:
		print "\n\033[1;32m\t [+] Welcome to Termux ! [+]"
		print "\033[00m"
		sys.exit()

	else:
		print "\n\033[1;31mInvalid Password !!!\033[00m\n"
		restart()

try:
	main()
except KeyboardInterrupt:
	os.system('clear')
	restart()
