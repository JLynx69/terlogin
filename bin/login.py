#termux login
import os, sys
import getpass

# UBAH JADI USERNAME DAN PASSWORD MU


username = 'user'      # ganti 'user' jadi 'sesuka' mu
password = 'password'  # ganti 'password' jadi 'sesuka' mu


# Tekan ctrl+x jika sudah di ubah
# atau vol-down + x

# JANGAN UBAH CODE DI BAWAH !!!

def restart():
	ngulang = sys.executable
	os.execl(ngulang, ngulang, *sys.argv)

def main():
	uname = raw_input("username : ")
	if uname == username:
		pwd = getpass.getpass("password : ")

		if pwd == password:
			print "\n\033[1;34mWelcome to Termux", username
			print "\033[00m"
			sys.exit()

		else:
			print "\n\033[1;31mInvalid Password !!!\033[00m"
			print "Login Ulang\n"
			restart()

	else:
		print "\n\033[1;31mInvalid Username !!!\033[00m"
		print "Login Ulang\n"
		restart()

try:
	main()
except KeyboardInterrupt:
	os.system('clear')
	restart()
