#---------------------->DECODE BY SAJU <------------------#
import itertools, threading, time, sys, os
import requests
import rich
import json,os,sys,random,datetime,time,re
from concurrent.futures import ThreadPoolExecutor as speed
from rich.markdown import Markdown as mark
from rich import pretty
from random import choice as choose
import random 
import os,re,random,uuid,subprocess
from os import system
import time, json, string
import os,re,random,uuid,subprocess
import os
import time
import json
import sys
import re
import requests
import random
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
from os import system
import time, json, string
from os import system as sm 
from sys import platform as pf
from time import sleep as sp
from random import choice as ch
from random import randint as rand

P = '\x1b[0;97m'
M = '\x1b[0;91m' 
H = '\x1b[0;92m' 
K = '\x1b[0;93m'
B = '\x1b[0;94m'
U = '\x1b[0;95m' 
O = '\x1b[0;96m' 
N = '\x1b[0m'   
I='\x1b[0;32m'
C='\x1b[0;36m'
M='\x1b[0;31m'
U='\x1b[0;35m'
K='\x1b[0;33m'
P='\x1b[00m'
H='\x1b[0;90m'
Q="\x1b[00m"
i='\x1b[0;32m'
c='\x1b[0;36m'
m='\x1b[0;31m'
u='\x1b[0;35m'
k='\x1b[0;33m'
b='\x1b[0;34m'
p='\x1b[00m'
h='\x1b[0;90m'
q="\x1b[00m"
pretty.install()
ses=requests.Session()
def fileflash(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.04)
        
def fileflashlogo(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
id,uid= [],[]
linex = ('\033[0;97m────────────────────────────────────────────────────────')

P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # mix
m = '\x1b[1;91m' #lal +
k = '\033[93m' # pila +
h = '\x1b[1;92m' # hara +
hh = '\033[32m' # hara2 -
u = '\033[95m' # gulabai
kk = '\033[33m' # pila2 -
b = '\33[1;96m' # surkh -
p = '\x1b[0;34m' # halka nila +
filecolor = random.choice([U,I,K,h,hh,U,u,m,k,h,u,b])



def sz__love(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)

def clear():
    try:
        os.system('clear')
    except KeyError or IOError:
        os.system('cls')

def filelogo():
	clear()
	fileflashlogo(f"{filecolor}   _______    ______   _______   _______  __      __ 
|       \  /      \ |       \ |       \|  \    /  \
| $$$$$$$\|  $$$$$$\| $$$$$$$\| $$$$$$$\\$$\  /  $$
| $$__/ $$| $$__| $$| $$__/ $$| $$__/ $$ \$$\/  $$ 
| $$    $$| $$    $$| $$    $$| $$    $$  \$$  $$  
| $$$$$$$\| $$$$$$$$| $$$$$$$ | $$$$$$$    \$$$$   
| $$__/ $$| $$  | $$| $$      | $$         | $$    
| $$    $$| $$  | $$| $$      | $$         | $$    
 \$$$$$$$  \$$   \$$ \$$       \$$          \$$
	fileflashlogo(f'{linex}\n AUTHOR    : BAPPY VAU\n VERSION   : 4.1 \n DECOE BY BAPPY ERROR \n{linex}\n\t\tMain Menu')

def check_login():
	try:
		token = open('filetoken.txt','r').read()
		cok = open('filecok.txt','r').read()
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+token, cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except :login()
	except requests.exceptions.ConnectionError:
		li = 'Connection Problem'
		lo = mark(li, style='red')
		sol().print(lo, style='purple')
		exit()
	except IOError:
		login()
#===========COOKIE LOGIN===========#
def login():
 try:
  clear()
  print('') 
  ses = requests.Session();filelogo();print(linex)
  cookie = input('\nCookies : ')
  cookies = {'cookie':cookie}
  url = 'https://www.facebook.com/adsmanager/manage/campaigns'
  req = ses.get(url,cookies=cookies)
  set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
  nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
  roq = ses.get(nek,cookies=cookies)
  tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
  tokenw = open("filetoken.txt", "w").write(tok)
  cokiew = open("filecok.txt", "w").write(cookie)
  fileflash(f'{linex}\nLogin Successfully\n ')
  check_login()
 except Exception as e:
  os.system("rm -f filetoken.txt")
  os.system("rm -f filecok.txt")
  print(f' Login Failed (May be Cookies are Expired)')
  exit()	
#===========MENU===========#
def menu(sy2,sy3):
	try:
		tok = open('filetoken.txt','r').read()
		cok = open('filecok.txt','r').read()
	except ValueError:
		print('[×] Expired Cookies ')
		time.sleep(5)
		check_login()
	clear()
	filelogo()
	ip = requests.get("https://api.ipify.org").text
	sz__love(f'{linex}\n\x1b[1;37m>> IP    : {ip}');sz__love(f'\x1b[1;37m>> NAME  : {sy2}');sz__love(f'\x1b[1;37m>> UID   : {sy3}\n{linex}')
	print('[1] Create Super File (Unlimited)')
	print('[2] Remove Double Links')
	print('''[3] Seperate New ID's Links''')
	print('''[4] Removing Part of File''')
	print('''[6] Remove Cookies''')
	print('''[0] Exit''')
	axlpogi = input(f'{linex}\n CHOOSE : ')
	print('')
	if axlpogi in ['1' or '01']:
		filename()
	elif axlpogi in ['2' or '02']:
		remove_double()
	elif axlpogi in ['3' or '03']:
		sorting_file()
	elif axlpogi in ['4'or'04']:
		part_remove()
	elif axlpogi in ['5' or '05']:
		contact_author()
	elif axlpogi in ['6' or '06']:
		rem_login()
	elif axlpogi in ['0' or '00']:
		fileflash('Thanks For Using My Tool')
	else:
		errorz()
def errorz():
	fileflash(f'{k}Please Choose Correct Option {x}')
	time.sleep(3)
	check_login()
def rem_login():
	os.system('rm -rf file*')
	fileflash('Cookies SucessFully Removed')

#===========FILENAME===========#
def filename():
    clear();filelogo()
    fileflash(f'{linex}\nExample : /sdcard/filename.txt')
    filen=input(f'{linex}\nEnter File Path : ')
    superfile(filen)
#===========PUBLIC===========#
def superfile(filen):
	try:token = open('filetoken.txt','r').read();cok = open('filecok.txt','r').read()
	except IOError:exit()
	kil = input(f'{linex}\nEnter Link of Public ID : ');clear();filelogo()
	uid.append(kil);print(f'{linex}\nDumping Started \nPress Ctrl+Z to stop\n{linex}\nFile Will be Saved in {filen}\n{linex}')
	cookie_dict = {}
	for cookie in cok.split(';'):name, value = cookie.strip().split('=', 1);cookie_dict[name] = value
	ciik = json.dumps(cookie_dict)
	headers = {
    'authority': 'graph.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,ar;q=0.7',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
	}
	params = {
    'access_token': token,
    'limit': '5000',
	}	
	for userr in uid:
		try:
			lilis = requests.get(f'https://graph.facebook.com/{kil}/friends',params=params,cookies=cookie_dict,headers=headers)
			linkdump = json.loads(lilis.text)
			for appui in linkdump['data']:
				try:
					fileid = (appui['id']+'|'+appui['name'])
					if fileid in id:pass
					else:id.append(fileid)
					zxx=open(filen, "a+").write(soloid+'\n');zxx.close()
				except:pass
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(' Network Error ')
			exit()
	try:
		with speed(max_workers=20) as (filepogi):
			juma = open(filen,"r").readlines()
			for data in juma:
				data = data.replace("\n","")
				kiky = data.split("|")
				useriid = ("%s"%(kiky[0]))
				nm = ("%s"%(kiky[1]))
				filepogi.submit(multi_file, useriid,filen)
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		fileflash(' Network Error ')
		check_login()
	except (KeyError,IOError):
		fileflash(f'{k}This is Private Account {x}')
		time.sleep(3);check_login()
#============================#
xz = []
def multi_file(useriid,filen):
	try:token = open('filetoken.txt','r').read();cok = open('filecok.txt','r').read()
	except IOError:exit()
	cookie_dict = {}
	for cookie in cok.split(';'):name, value = cookie.strip().split('=', 1);cookie_dict[name] = value
	ciik = json.dumps(cookie_dict)
	headers = {
    'authority': 'graph.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,ar;q=0.7',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
	}
	params = {
    'access_token': token,
    'limit': '5000',
	}
	try:
		li = requests.get(f'https://graph.facebook.com/{useriid}/friends',params=params,cookies=cookie_dict,headers=headers)
		linkdump =json.loads(li.text)
		for appui in linkdump["data"]:
				try:
					fileid = (appui["id"]+'|'+appui["name"])
					if fileid not in id:id.append(fileid);xaz=open(filen,'a+');xaz.write(fileid+'\n');xaz.close()
					else:pass
				except:pass
	except KeyError:pass
	
	sys.stdout.write("\r%s[%sExtracted Accounts ]%s •> %s"%(Q,choose([U,I,K,h,M,C]),Q, len(id))); sys.stdout.flush()
#============================#
def remove_double():
    clear();filelogo()
    fileflash(linex)
    file = input ('\033[0;92m Enter Your File Path : ')
    fileflashlogo(linex)
    os.system(f'sort -u -r -o {file} {file} --quit 2>/dev/null')
    print ('\n[*] SuccessFully Removed Double Links')
    print ('[*] File Saved in : '+file)
    input(f'{linex} \nPress Enter to go back to Main Menu')
    clear()
    check_login()
#============================#
def sorting_file():
    clear();filelogo()
    fileflashlogo(linex)
    try:linkslimit = int(input(' How many links do you want to Seperate : '))
    except:linkslimit = 1
    fileflashlogo(f'{linex}\nPlease Enter File Path\nExample: /sdcard/mfile.txt')
    file = input (f'{linex}\nInput Your File Path : ')
    fileout = input(f'Where Do you want to save the File : ')
    y = 0
    fileflashlogo(f"{linex}\n Links You Want To Keep\nExample : [100088,100089,100090etc]")
    os.system('rm -rf 1.txt');os.system('rm -rf .solo.txt')
    for k in range(linkslimit):y+=1;links=input('Put Links : ');os.system('cat '+file+' | grep "'+links+'" >> '+fileout+' --quiet 2>/dev/null')
    os.system(f'sort -u -r -o {fileout} {fileout} --quit 2>/dev/null')
    fileflashlogo(f'{linex}\n Accounts SuccessFully Extracted');print(' Total Accounts Extraced : '+str(len(open(fileout,'r',encoding='utf-8').read().splitlines())))
    print('\033[0m New Accounts File saved in : \033[0;32m'+fileout)
    input(f'{linex}\nPress Enter to go back to Main Menu')
    clear()
    check_login()
#============================#
def part_remove():
    clear();filelogo()
    fileflashlogo(f'''{linex}\nType (solo) if you want help''')
    fileflashlogo(f'''{linex}\nExaple : newfile.txt''')
    fileinput1 = input(f'{linex}\nEnter The File You Want To Remove Part of :')
    if ('file' or 'File' or '(file)' or 'FILE') in fileinput1:
        contact_author()
    else:
        fileflashlogo(f'{linex}\nExample : If You want to remove first \n1000 lines enter : 1000')
        xasi = input(f'{linex}\nHow Much Lines of File do you want to Remove:')
        os.system('sed -i 1,'+xasi+'d '+soloinput1)
        fileflashlogo(f'{linex}\nYour File is Saved in {fileinput1}\nFirst {xasi} lines are removed')
#============================#
def contact_author():
	fileflashlogo('Wait! You Will Be redirected to author of the tool')
	os.system('xdg-open https://www.facebook.com/AlexanderAxlMontreal.IAmLimitless')
#============================#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('rm -rf ..file.txt')
	except:pass
	try:os.system('rm -rf .file.txt && rm -rf tmp')
	except:pass
	os.system('rm -rf ..ijs.txt')
	check_login()

#>>>>> THANKS BY AXL <<<<<<#

