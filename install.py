#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# ========== ByPa55 ============

# author      : uidops
# email       : uidopsu@gmail.com
# github      : https://github.com/siruidops/sqlinjection-form-bypass
# description : a tool for auto bypassing login page admin and ...

# ==============================
# Telegram: @softhacking
#

import sys
import subprocess
import os
from core.c0l0r import *

def banner():
	print
	print yellow+" -*- Welcome To ByPa55 Installer -*-"+end
	print
	print brown+"   Author"+end+": "+green+"uidops"+end
	print brown+"   Email"+end+" : "+green+"uidopsu@gmail.com"+end
	print brown+"   Github"+end+": "+green+"https://github.com/siruidops/sqlinjection-form-bypass"+end
	print

def install():
	print
	print brown+ " [*] Installing ..."+end
	print
	dep_command = subprocess.call(('pip','install','-r','requirements.txt'))
	print
	print brown+" [*] Please Enter Path a Folder For Copy Files"
	print "     default: /opt/bypa55"+end
	print
	path = raw_input(brown+"ByPa55 > Path >>> "+end)
	if path == "":
		path = "/opt/bypa55"
	else:
		pass
	creat_command = subprocess.call(('mkdir','-p',path))
	if path[len(path)-1] == "/":
		file = open('run.sh',"a")
		file.write("python %s"%(path+"bypass.py"))
		file.close()
	else:
		file = open('run.sh',"a")
		file.write("python %s"%(path+"/bypass.py"))
		file.close()
	copy_command = subprocess.call(('cp','-r','*',path))
	mk_command = subprocess.call(('cp ','run.sh','/usr/bin/bypa55'))
	print
	print green+" [*] Installed in %s , Run With Command 'bypa55'%s"%(path,end)
	print

def main():
	banner()
	print brown+"  1"+end+")"+green+" Install"+end
	print brown+"  2"+end+")"+green+" Exit"+end
	print
	r = raw_input(brown+"ByPa55 > Choice >>> "+end)
	if r == '1':
		install()
	elif r == '2':
		print
		sys.exit()
	else:
		print
		print red+" [-] Not Found Your Command"+end
		print
		raw_input()
		main()

if __name__ == '__main__':
	main()
else:
	pass










