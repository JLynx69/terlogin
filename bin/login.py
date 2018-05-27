#termux login
import os, sys

# UBAH JADI USERNAME DAN PASSWORD MU


username = 'jack'      # ganti 'jack' jadi 'username' mu
password = 'password'  # ganti 'password' jadi 'password' mu


# JANGAN UBAH CODE DI BAWAH !!!

def restart():
	ngulang = sys.executable
	os.execl(ngulang, ngulang, *sys.argv)

def main():
	print "\033[1;32mTermux Login\n\033[00m"
	uname = raw_input("username : ")
	if uname == username:
		pwd = raw_input("password : ")

		if pwd == password:
			print "\n\033[1;34mWelcome to Termux", username
			print "\033[00m"
			os.system('sh')

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
