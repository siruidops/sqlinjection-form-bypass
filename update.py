#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# ========== ByPa55 ============

# author      : siruidops
# email       : sir.u1d0p5@gmail.com
# github      : https://github.com/siruidops/bypa55
# description : a tool for auto by passing login page admin and ...

# ==============================
# Telegram: @softhacking
#

from core.c0l0r import *
import urllib
import subprocess
import sys
import os

pt_now = os.getcwd()

def banner():
	print
	print yellow+" -*- Welcome To Updater ByPa55 -*-"+end
	print
	print brown+"     Author"+end+": "+green+"SirUidops"+end
	print brown+"     Email "+end+": "+green+"sir.u1d0p5@gmail.com"+end
	print brown+"     Github"+end+": "+green+"https://github.com/siruidops/ByPa55"+end
	print

def update_bypass():
	url_version = "https://raw.githubusercontent.com/siruidops/ByPa55/master/version.txt"
	url_git = "https://github.com/siruidops/ByPa55.git"
	file = open('version.txt')
	version_now = file.read()
	file.close()
	try:
		u = urllib.urlopen(url_version)
	except:
		print
		print red+" [-] Not Connect Found"+end
		print
		sys.exit()
	name_folder = "ByPa55-%s"%(u.read)
	if version_now == u.read():
		print
		print green+" [*] Your ByPa55 Is Update"+end
		print
		sys.exit()
	else:
		os.chdir('..')
		github_command = subprocess.call(('github','clone',url_git,name_folder))
		os.chdir(name_folder)
		install_command = subprocess.call(('bash','install'))
		os.chdir('..')
		ps = str(os.getcwd())+name_folder
		print
		print green+" [*] Updated ! [PATH=>%s%s"%(ps,end)
		print

def version_bypass():
	os.chdir(pt_now)
	file = open("version.txt")
	version_now = file.read()
	file.close()
	print
	print green+" [*] Version: %s"%(version_now)
	print

def main():
	banner()
	print brown+"  1"+end+") "+green+"Update"+end
	print brown+"  2"+end+") "+green+"Version"+end
	print brown+"  3"+end+") "+green+"Exit"+end
	print
	ch = raw_input(brown+"ByPa55 > Choice >>> "+end)
	if ch == "1":
		update_bypass()
	elif ch == "2":
		version_bypass()
	elif ch == "3":
		print
		sys.exit()
	else:
		print
		print red+" [-] Your Command Not Found [1..3]"+end
		print
		raw_input()
		main()

if __name__ == "__main__":
	main()
else:
	pass




