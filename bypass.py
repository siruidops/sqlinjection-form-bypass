#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# ========== ByPa55 ============

# author      : uidops
# email       : uidopsu@gmail.com
# github      : https://github.com/siruidops/sqlinjection-form-bypass
# description : a tool for auto by passing login page admin and ...

# ==============================


import sys
import os
import ssl
import getopt

try:
	import core.bypa55 as bypa55
except ImportError:
	print
	print " [-] You are deleted the file core: ./core/bypa55.py"
	print
	sys.exit()

try:
	from core.c0l0r import *
except ImportError:
	print
	print " [-] You are deleted the file core: ./core/c0l0r.py"
	print
	sys.exit()

# -*- SSL Certified -*-
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context
    
logo = yellow+"""
bbbbbbbb  y      y      pppppppppp             555555555 555555555
b       b y      y      p        p             5         5
b       b y      y      p        p             5         5
bbbbbbbb  yyyyyyyy      pppppppppp aaaaaaaa    555555555 555555555
b       b        y      p          a      a            5         5
b       b        y      p          a      aaa          5         5
bbbbbbbb  yyyyyyyy      p          aaaaaaaaa a 555555555 555555555
"""+end

def banner():
	print
	print logo
	print
	print brown+" Author"+end+": "+green+"uidops"+end
	print brown+" Email "+end+": "+green+"uidopssu@gmail.com"+end
	print brown+" Github"+end+": "+green+"https://github.com/siruidops/sqlinjection-form-bypasser"+end
	print
	print brown+"  Usage "+end+"=>"+green+" ./bypass.py [Options]"+end
	print
	print yellow+" Options"+end
	print
	print brown+"   -u "+end+"=> "+green+"Url Page Login"+end
	print brown+"   -l "+end+"=> "+green+"Name Username Field In Form Login , default: username"+end
	print brown+"   -p "+end+"=> "+green+"Name Password Field In Form login , default: password"+end
	print brown+"   -m "+end+"=> "+green+"Type Method Form Login , default: post"+end
	print brown+"   -e "+end+"=> "+green+"Error Text"+end
	print brown+"   -h "+end+"=> "+green+"Show Help Banner"+end
	print
	sys.exit()

def main():

	url_id = False
	u_field = "username"
	p_field = "password"
	method = "post"
	error_id = False

	argv = sys.argv[1:]
	
	if len(sys.argv) == 1:
		banner()
	else:
		pass

	try:
		opts,args = getopt.getopt(argv, "-u:-l:-p:-e:-m:-h")
	except:
		banner()

	for opt,arg in opts:
		if opt == '-u':
			url = arg
			url_id = True
		elif opt == '-l':
			u_field = arg
		elif opt == '-p':
			p_field = arg
		elif opt == '-m':
			method = arg
		elif opt == '-e':
			error = arg
			error_id = True
		else:
			banner()
	
	if url_id == False:
		print
		print red+" [-] You are not send me a url"+end
		print
		sys.exit()
	else:
		if error_id == False:
			print
			print red+" [-] You are not send me a error"+end
			print
			sys.exit()
		else:
			pass

	try:
		print
		bypa55.ByPass().run(url, u_field, p_field, error, method)
		print
	except KeyboardInterrupt:
		sys.exit(red+'[-] Good Bye (^/^)'+end)

if __name__ == "__main__":
	main()
else:
	pass
